from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from db.get_db import get_db_session
from db.models import User
from errors import ExistUsername, NotFoundUser
from utils.secrets import passwordManager
from schema.jwt import JWTResponsePayload
from utils.jwt import user_authendication, generate_token
from schema.input_ import UserRegisterInput, UserLoginInput
from repository.Repository import UserRepository 


route = APIRouter(
        prefix="/auth",
        tags=["auth"]
)


@route.post("/register", status_code=status.HTTP_201_CREATED)
async def create_user(data: UserRegisterInput, db = get_db_session):
    user = await UserRepository.is_username(data.username, db)

    if user:
        raise ExistUsername

    password = passwordManager.hash(data.password)
    data.password = password
    user_model = User(**data.model_dump())

    await UserRepository.register_user(user_model, db)



@route.post("/token", response_model=JWTResponsePayload)
async def create_token(data: OAuth2PasswordRequestForm = Depends(), db = get_db_session):
    user = await user_authendication(data.username, data.password, db)

    if not user:
        raise NotFoundUser

    token = generate_token(user.id, data.username, user.role.value)

    return token
