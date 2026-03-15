from jose import JWTError, jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from db.models import UserRole
from utils.settings import MIN, KEY, ALG
from datetime import datetime, timedelta, timezone
from repository.Repository import UserRepository
from utils.secrets import passwordManager
from inout.jwt import JWTResponsePayload, Payload
from errors import TokenIsNotValid


bearer = OAuth2PasswordBearer(tokenUrl="auth/token")


async def user_authendication(username, password, db):
    user = await UserRepository.get_user_by_username(username, db)

    if not user:
        return False

    if not passwordManager.verify(password, user.password):
        return False

    return user


def generate_token (user_id: int, username: str, role: str, expire: timedelta | None = None):
    exp = expire if expire else datetime.now(timezone.utc) + timedelta(minutes=MIN)

    to_encode = {
            "sub": username,
            "exp": exp,
            "id": user_id,
            "role": role
        }

    encoded_jwt = jwt.encode(to_encode, KEY, ALG)

    return JWTResponsePayload(access_token=encoded_jwt)


async def verify_token(token: str = Depends(bearer)):
    try:
        payload = jwt.decode(token, KEY, algorithms=[ALG])

        username: str = payload.get("sub") # type: ignore
        user_id: int = payload.get("id") # type: ignore
        user_role: UserRole = payload.get("role") # type: ignore

        if username is None or user_id is None:
            raise TokenIsNotValid

        return Payload(username=username, user_id=user_id, user_role=user_role)

    except JWTError:
        raise TokenIsNotValid


user_dependency: Payload = Depends(verify_token)
