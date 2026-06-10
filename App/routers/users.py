from fastapi import APIRouter, status
from schema.out import OutputGetUserById
from schema.input_ import UserUpdateInput, UserLoginInput
from db.get_db import get_db_session
from errors import WrongUsernameOrPassword, NotFoundUser, ExistUsername
from repository.Repository import UserRepository
from utils.secrets import passwordManager
from utils.jwt import user_dependency


router = APIRouter()


async def user_validate(userToken, db):
    user = await UserRepository.get_user_by_id(userToken.user_id, db)
    
    if not user:
        raise NotFoundUser
    return user


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete(userToken=user_dependency, db=get_db_session):
    user = await user_validate(userToken, db)

    await UserRepository.delete_user(user, db)


@router.put("/ChangeUsername/", status_code=status.HTTP_204_NO_CONTENT)
async def change_username(data: UserUpdateInput, userToken=user_dependency, db=get_db_session):
    user = await user_validate(userToken, db)

    if (data.username == user.username):
        pass
    elif (await UserRepository.is_username(data.username, db)):
        raise ExistUsername

    await UserRepository.update_user(data, user, db)


@router.get("/", status_code=status.HTTP_200_OK)
async def user_by_id(userToken=user_dependency, db=get_db_session):
    user = await user_validate(userToken, db)

    return OutputGetUserById(username=user.username, role=user.role)