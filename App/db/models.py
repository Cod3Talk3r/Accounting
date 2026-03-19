from sqlalchemy import Column, Integer, String, Boolean, Enum, ForeignKey
from db.database import Base
import enum


class UserRole(enum.Enum):
    user = "user"
    admin = "admin"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.user, nullable=False)


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    ownerId = Column(Integer, ForeignKey("users.id"))


class Acount(Base):
    __tablename__ = "acounting"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer, nullable=False, index=True)
    description = Column(String, nullable=True)
    acountingType = Column(Boolean, nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    tag_id = Column(Integer, ForeignKey("tags.id"))
