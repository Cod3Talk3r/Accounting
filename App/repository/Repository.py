from schema.input_ import UserRegisterInput, UserUpdateInput, TagInput
from db.models import User, Tag
import sqlalchemy as sa
from pydantic import BaseModel


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

        return result.scalar_one_or_none()

    @staticmethod
    async def get_user_by_id(id, db) -> User:
        query = sa.select(User).where(User.id == id)
        result = await db.execute(query)

        return result.scalar_one_or_none()

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
    async def is_username(username: str, db) -> bool:
        query = sa.select(User).where(User.username == username)
        result = await db.execute(query)
        user = result.scalar_one_or_none()

        return False if not user else True


class TagRepository():
    @staticmethod
    async def get_all_tags(db) -> list[Tag]:
        query = sa.select(Tag)
        result = await db.execute(query)

        return result.scalars().all()

    @staticmethod
    async def get_tag_by_name(name: str, db) -> Tag:
        query = sa.select(Tag).where(Tag.name==name)
        result = await db.execute(query)

        return result.scalar_one_or_none()

    @staticmethod
    async def get_tag_by_id(id: int, db) -> Tag:
        query = sa.select(Tag).where(Tag.id==id)
        result = await db.execute(query)

        return result.scalar_one_or_none()
    
    @staticmethod
    async def create_tag(name: TagInput, ownerId: int, db) -> None:
        tag = Tag(**name.model_dump(), ownerId=ownerId)

        db.add(tag)
        await db.commit()
        await db.refresh(tag)

    @staticmethod
    async def delete_tag(tag: Tag, db) -> None:
        await db.delete(tag)
        await db.commit()

    @staticmethod
    async def change_tag(tag: Tag, newTag: TagInput, db) -> None:
        tag.name = newTag.name

        await db.commit()
        await db.refresh(tag)