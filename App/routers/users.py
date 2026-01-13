from fastapi import APIRouter, status
from inout.input_ import UserRegisterInput, UserLoginInput
from db.get_db import get_db_session
from db.models import User
import sqlalchemy as sa


router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(inData: UserRegisterInput, db=get_db_session):
    user = User(username=inData.username, password=inData.password, email=inData.email, role=inData.role)

    db.add(user)
    await db.commit()
    await db.refresh(user)


@router.post("/login")
async def login(data: UserLoginInput, db=get_db_session):
    query = sa.select(User).where(User.username == data.username)
    result = await db.execute(query)
    user = result.scalar_one_or_none()

    if not user or (user.password != data.password):
        return {"msg": "Not User"}

    return {"Login": "Succeed."}


@router.delete("/delete")
async def delete(data: UserLoginInput, db=get_db_session):
    query = sa.select(User).where(User.username == data.username)
    result = await db.execute(query)
    user = result.scalar_one_or_none()
 
    if not user or (user.password != data.password):
        return {"msg": "Not User"}

    await db.delete(user)
    await db.commit()

    return {"msg": f"user: {data.username} deleted."}


@router.put("/update/{ID}")
async def update(data: UserRegisterInput, ID, db=get_db_session):
    query = sa.select(User).where(User.id == ID)
    result = await db.execute(query)
    user = result.scalar_one_or_none()

    if not user:
        return {"msg": "Not User"}

    user.username = data.username
    user.password = data.password
    user.email = data.email
    user.role = data.role

    await db.commit()
    await db.refresh(user)

    return user


@router.get("/user/{ID}")
async def user_by_id(ID, db=get_db_session):
    query = sa.select(User).where(User.id == ID)
    result = await db.execute(query)
    user = result.scalar_one_or_none()

    if not user:
        return {"msg": "user not found!"}

    return user
