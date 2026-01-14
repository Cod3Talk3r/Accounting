from fastapi import APIRouter, status
from inout.input_ import UserRegisterInput, UserLoginInput
from db.get_db import get_db_session
from db.models import User
import sqlalchemy as sa
from errors import UserNotFound
from repository.Repository import UserRepository


router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(data: UserRegisterInput, db=get_db_session):
        await UserRepository.register_user(data, db)


@router.post("/login")
async def login(data: UserLoginInput, db=get_db_session):
    user = await UserRepository.get_user_by_username(data, db)

    if not user:
        raise UserNotFound

    if user.password != data.password:
        return {"msg": "Wrong Password!"}

    return {"Login": "Succeed."}


@router.delete("/delete")
async def delete(data: UserLoginInput, db=get_db_session):
    user = await UserRepository.get_user_by_username(data, db)

    if not user:
        raise UserNotFound

    if user.password != data.password:
        return {"msg": "Wrong Password!"}

    await UserRepository.delete_user(user, db)

    return {"msg": f"user: {data.username} deleted."}


@router.put("/update/{ID}")
async def update(data: UserRegisterInput, ID, db=get_db_session):
    user = await UserRepository.get_user_by_id(ID, db)

    if not user:
        raise UserNotFound

    await UserRepository.update_user(data, user, db)

    return user


@router.get("/user/{ID}")
async def user_by_id(ID, db=get_db_session):
    query = sa.select(User).where(User.id == ID)
    result = await db.execute(query)
    user = result.scalar_one_or_none()

    if not user:
        raise UserNotFound

    return user
