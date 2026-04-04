from sqlalchemy import Column, Integer, String, Boolean, Enum, ForeignKey
from sqlalchemy.orm import relationship
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

    tags = relationship(
        "Tag",
        back_populates="owner",
        cascade="all, delete",
        passive_deletes=True
    )

    acounts = relationship(
    	"Acount",
	    back_populates="user",
    	cascade="all, delete",
    	passive_deletes=True
    )


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    ownerId = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    owner = relationship("User", back_populates="tags")

    acounts = relationship(
        "Acount",
        back_populates="tag",
	    cascade="save-update",
	    passive_deletes=True
    )


class Acount(Base):
    __tablename__ = "acounting"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer, nullable=False, index=True)
    description = Column(String, nullable=True)
    acountingType = Column(Boolean, nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    tag_id = Column(Integer, ForeignKey("tags.id", ondelete="SET NULL"))

    user = relationship("User", back_populates="acounts")
    tag = relationship("Tag", back_populates="acounts")
