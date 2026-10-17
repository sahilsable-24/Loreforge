from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserOut
from app.core.security import hash_password

router = APIRouter(prefix="/auth", tags=['auth'])

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
