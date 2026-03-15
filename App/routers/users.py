from fastapi import APIRouter, status
from inout.out import OutputGetUserById
from inout.input_ import UserUpdateInput, UserLoginInput
from db.get_db import get_db_session
from errors import WrongUsernameOrPassword, NotFoundUser, ExistUsername
from repository.Repository import UserRepository
from utils.secrets import passwordManager
from utils.jwt import user_dependency


router = APIRouter()


@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
async def delete(data: UserLoginInput, db=get_db_session):
    user = await UserRepository.get_user_by_username(data.username, db)

    if not user or not (passwordManager.verify(data.password, user.password)):
        raise WrongUsernameOrPassword

    await UserRepository.delete_user(user, db)

    return {"msg": f"user: {data.username} deleted."}


@router.put("/update/{ID}", status_code=status.HTTP_204_NO_CONTENT)
async def update(data: UserUpdateInput, ID, db=get_db_session):
    user = await UserRepository.get_user_by_id(ID, db)

    if not user:
        raise NotFoundUser

    if (data.username == user.username):
        pass
    elif (await UserRepository.is_username(data.username, db)):
        raise ExistUsername

    await UserRepository.update_user(data, user, db)



@router.get("/{ID}", status_code=status.HTTP_200_OK)
async def user_by_id(ID, db=get_db_session):
    user = await UserRepository.get_user_by_id(ID, db)

    if not user:
        raise NotFoundUser

    return OutputGetUserById(username=user.username, role=user.role)
