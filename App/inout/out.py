from pydantic import BaseModel
from db.models import UserRole


class OutputGetUser(BaseModel):
    username: str
    role: UserRole
