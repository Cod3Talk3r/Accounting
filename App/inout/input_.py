from pydantic import BaseModel


class UserRegisterInput(BaseModel):
    username: str
    password: str
    email: str
    role: str


class UserLoginInput(BaseModel):
    username: str
    password: str
