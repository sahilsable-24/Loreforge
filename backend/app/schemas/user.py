from datetime import datetime
from pydantic import BaseModel, ConfigDict,EmailStr,Field
import uuid

# Registering the User
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)


class UserOut(BaseModel):
    model_config= ConfigDict(from_attributes=True)
    id: uuid.UUID
    email: EmailStr
    created_at: datetime

# User Login
class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)

class RefreshRequest(BaseModel):
    refresh_token: str

class TokenPair(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

    

