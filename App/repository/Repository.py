from inout.input_ import UserRegisterInput
# from db.get_db import get_db_session
from db.models import User


class UserRepository():
    @staticmethod
    async def register(data: UserRegisterInput, db):
        user = User(username=data.username, password=data.password, email=data.email, role=data.role)

        db.add(user)
        await db.commit()
        await db.refresh(user)
