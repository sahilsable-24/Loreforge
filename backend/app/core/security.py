from app.core.config import settings
import bcrypt
import hashlib, secrets, jwt
from datetime import datetime, timedelta, timezone

def hash_password(plain_password: str) -> str:
    hashed = bcrypt.hashpw(plain_password.encode("utf-8"), bcrypt.gensalt())
    return hashed.decode("utf-8")

def verify_password(plain_password:str, hashed_password:str) -> bool:
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))


#Creating Access Tokens
def create_access_token(user_id) -> str:
    exp = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_minutes)
    return jwt.encode({"sub": str(user_id), "exp":exp}, settings.jwt_secret, algorithm="HS256")

def decode_access_token(token:str) -> str:
    return jwt.decode(token, settings.jwt_secret, algorithms=["HS256"])["sub"]

#Creating refresh Tokens
def new_refresh_token() -> str:
    return secrets.token_urlsafe(48)

def hash_refresh_token(token:str) -> str:
    return hashlib.sha256(token.encode()).hexdigest()