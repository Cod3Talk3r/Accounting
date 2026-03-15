from inout.input_ import UserRegisterInput, UserUpdateInput
from db.models import User
import sqlalchemy as sa


class UserRepository():
    @staticmethod
    async def register_user(data: UserRegisterInput, db) -> None:
        user = User(username=data.username, password=data.password, role=data.role)

        db.add(user)
        await db.commit()
        await db.refresh(user)

    @staticmethod
    async def get_user_by_username(data: str, db) -> User:
        query = sa.select(User).where(User.username == data)
        result = await db.execute(query)
        user = result.scalar_one_or_none()

        return user

    @staticmethod
    async def get_user_by_id(id, db) -> User:
        query = sa.select(User).where(User.id == id)
        result = await db.execute(query)
        user = result.scalar_one_or_none()

        return user

    @staticmethod
    async def delete_user(user: User, db) -> None:
        await db.delete(user)
        await db.commit()

    @staticmethod
    async def update_user(data: UserUpdateInput, user: User, db) -> None:
        user.username = data.username  # type: ignore

        await db.commit()
        await db.refresh(user)

    @staticmethod
    async def is_username(username, db) -> bool:
        query = sa.select(User).where(User.username == username)
        result = await db.execute(query)
        user = result.scalar_one_or_none()

        return False if not user else True
