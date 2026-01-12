from fastapi import APIRouter
from inout.input_ import UserRegisterInput
from db.init_db import get_db_session


router = APIRouter()


@router.post("/register")
async def register(inData: UserRegisterInput, db = get_db_session):
    return {"msg": f"username is: {inData.username} and password is: {inData.password}"}
