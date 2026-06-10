from pydantic import BaseModel, Field
from db.models import UserRole


class UserRegisterInput(BaseModel):
    username: str = Field(min_length=6, max_length=15)
    password: str = Field(min_length=8, max_length=32)
    role: UserRole


class UserLoginInput(BaseModel):
    username: str = Field(min_length=6, max_length=15)
    password: str = Field(min_length=8, max_length=32)


class UserUpdateInput(BaseModel):
    username: str = Field(min_length=6, max_length=15)


class TagInput(BaseModel):
    name: str
