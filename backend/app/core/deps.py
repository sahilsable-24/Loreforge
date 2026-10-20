import uuid, jwt
from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session
from app.core.security import decode_access_token
from app.db.session import get_db
from app.models.user import User


bearer = HTTPBearer()

def get_current_user(
    creds : HTTPAuthorizationCredentials = Depends(bearer),
    db: Session = Depends(get_db)
) -> User:

    unauthorized = HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid or expired token")

    try:
        user_id = decode_access_token(creds.credentials)
    except jwt.PyJWTError:
        raise unauthorized

    user = db.get(User, uuid.UUID(user_id))

    if user is None:
        raise unauthorized

    return user