from pydantic import BaseModel


class OutputGetUser(BaseModel):
    username: str
    email: str
    role: str
