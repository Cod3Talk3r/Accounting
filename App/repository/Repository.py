from inout.input_ import UserRegisterInput, UserLoginInput
from db.models import User
import sqlalchemy as sa


class UserRepository():
    @staticmethod
    async def register_user(data: UserRegisterInput, db):
        user = User(username=data.username, password=data.password, email=data.email, role=data.role)

        db.add(user)
        await db.commit()
        await db.refresh(user)


    @staticmethod
    async def get_user_by_username(data: UserLoginInput, db):
        query = sa.select(User).where(User.username == data.username)
        result = await db.execute(query)
        user = result.scalar_one_or_none()

        return user


    @staticmethod
    async def get_user_by_id(id, db):
        query = sa.select(User).where(User.id == id)
        result = await db.execute(query)
        user = result.scalar_one_or_none()

        return user


    @staticmethod
    async def delete_user(user: User, db):
        await db.delete(user)
        await db.commit()


    @staticmethod
    async def update_user(data: UserRegisterInput, user: User, db):
        user.username = data.username  #type: ignore
        user.password = data.password  #type: ignore
        user.email = data.email  #type: ignore
        user.role = data.role  #type:ignore

        await db.commit()
        await db.refresh(user)
        

