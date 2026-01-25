from pydantic import BaseModel
from db.models import UserRole


class UserRegisterInput(BaseModel):
    username: str
    password: str
    role: UserRole


class UserLoginInput(BaseModel):
    username: str
    password: str


class UserUpdateInput(BaseModel):
    username: str
    role: UserRole
