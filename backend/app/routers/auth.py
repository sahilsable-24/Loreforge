from fastapi import APIRouter, Depends, HTTPException, status
from datetime import datetime, timedelta, timezone
from sqlalchemy import select, update
from sqlalchemy.orm import Session
from app.core.config import settings
from app.core.deps import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserOut
from app.core.security import hash_password, create_access_token, hash_refresh_token, new_refresh_token, verify_password
from app.models.refresh_token import RefreshToken
from app.schemas.user import LoginRequest, RefreshRequest, TokenPair

router = APIRouter(prefix="/auth", tags=['auth'])

def issue_tokens(db: Session, user_id) -> TokenPair:
    raw = new_refresh_token()
    db.add(RefreshToken(
        user_id=user_id,
        token_hash=hash_refresh_token(raw),
        expires_at=datetime.now(timezone.utc) + timedelta(days=settings.refresh_token_days)
    ))
    db.commit()
    return TokenPair(access_token=create_access_token(user_id), refresh_token=raw)

# Regestering the User
@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    
    if db.scalar(select(User).where(User.email == user_in.email.lower())):
        raise HTTPException(status_code=409, detail="User already exist")

    hashed_password = hash_password(user_in.password)

    new_user = User(
        email=user_in.email,
        hashed_password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

# User Login endpoint
@router.post("/login", response_model=TokenPair)
def login(body: LoginRequest, db: Session = Depends(get_db)):
    user = db.scalar(select(User).where(User.email == body.email))

    if user is None or not verify_password(body.password, user.hashed_password):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid Email or Password")

    return issue_tokens(db, user.id)


# Refresh endpoint
@router.post("/refresh", response_model=TokenPair)
def refresh(body: RefreshRequest, db: Session=Depends(get_db)):
    now = datetime.now(timezone.utc)
    row = db.scalar(
        select(RefreshToken).where(RefreshToken.token_hash == hash_refresh_token(body.refresh_token))
    )

    if row is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid refresh token")

    if row.revoked_at is not None:
        db.execute(
            update(RefreshToken)
            .where(RefreshToken.user_id == row.user_id, RefreshToken.revoked_at.is_(None))
            .values(revoked_at=now)
        )

        db.commit()
        raise HTTPException(status.HTTP_401_UNAUTHORIZED,"Invalid Refresh Token")

    if row.expires_at < now:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid Refresh Token")

    row.revoked_at = now
    return issue_tokens(db, row.user_id)


# current user
@router.get("/me", response_model=UserOut)
def me(user: User = Depends(get_current_user)):
    return user
