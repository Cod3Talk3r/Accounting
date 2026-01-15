from fastapi import APIRouter, status
from inout.input_ import UserRegisterInput, UserLoginInput
from db.get_db import get_db_session
from errors import WrongUsernameOrPassword, NotFoundUser
from repository.Repository import UserRepository


router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(data: UserRegisterInput, db=get_db_session):
        await UserRepository.register_user(data, db)


@router.post("/login", status_code=status.HTTP_200_OK)
async def login(data: UserLoginInput, db=get_db_session):
    user = await UserRepository.get_user_by_username(data, db)

    if not user:
        raise WrongUsernameOrPassword

    if user.password != data.password:
        raise WrongUsernameOrPassword

    return {"Login": "Succeed."}


@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
async def delete(data: UserLoginInput, db=get_db_session):
    user = await UserRepository.get_user_by_username(data, db)

    if not user:
        raise WrongUsernameOrPassword

    if user.password != data.password:
        raise WrongUsernameOrPassword

    await UserRepository.delete_user(user, db)

    return {"msg": f"user: {data.username} deleted."}


@router.put("/update/{ID}", status_code=status.HTTP_204_NO_CONTENT)
async def update(data: UserRegisterInput, ID, db=get_db_session):
    user = await UserRepository.get_user_by_id(ID, db)

    if not user:
        raise NotFoundUser

    await UserRepository.update_user(data, user, db)

    return user


@router.get("/user/{ID}", status_code=status.HTTP_200_OK)
async def user_by_id(ID, db=get_db_session):
    user = await UserRepository.get_user_by_id(ID, db)

    if not user:
        raise NotFoundUser

    return user
