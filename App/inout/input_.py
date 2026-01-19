from pydantic import BaseModel, Field


class UserRegisterInput(BaseModel):
    username: str = Field(min_length=6, max_length=15)
    password: str = Field(min_length=8, max_length=32)
    email: str = Field(min_length=7)
    role: str


class UserLoginInput(BaseModel):
    username: str
    password: str


class UserUpdateInput(BaseModel):
    username: str
    email: str
    role: str
