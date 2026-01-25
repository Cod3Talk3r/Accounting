from pydantic import BaseModel
from db.models import UserRole


class JWTResponsePayload(BaseModel):
    access_token: str
    token_type: str = "bearer"


class Payload(BaseModel):
    username: str
    user_id: int
    user_role: UserRole
