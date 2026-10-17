from datetime import datetime
from pydantic import BaseModel, ConfigDict,EmailStr,Field
import uuid


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)


class UserOut(BaseModel):
    model_config= ConfigDict(from_attributes=True)
    id: uuid.UUID
    email: EmailStr
    created_at: datetime