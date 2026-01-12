from fastapi import APIRouter
from inout.input_ import UserRegisterInput
from db.get_db import get_db_session
from db.models import User


router = APIRouter()


@router.post("/register")
async def register(inData: UserRegisterInput, db = get_db_session):
    user = User(username=inData.username, password=inData.password, email=inData.email, role=inData.role)

    db.add(user)
    await db.commit()
    await db.refresh(user)

    return user
