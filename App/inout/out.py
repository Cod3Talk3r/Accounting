from pydantic import BaseModel
from db.models import UserRole


class OutputGetUserById(BaseModel):
    username: str
    role: UserRole


class CreatedOut(BaseModel):
    id: int
    username: str
    role: UserRole

