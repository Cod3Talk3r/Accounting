from fastapi import APIRouter, status
from db.get_db import get_db_session
from repository.Repository import TagRepository
from schema.input_ import TagInput
from errors import NotFoundTag, ExistTag


router = APIRouter()


@router.get("/")
async def get_all_tags(db=get_db_session):
    return await TagRepository.get_all_tags(db)


@router.get("/{name}")
async def get_tag_by_name(name: str, db=get_db_session):
    tag = await TagRepository.get_tag_by_name(name.casefold(), db)

    if tag is None:
        raise NotFoundTag
    
    return tag


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_tag(tag: TagInput, db=get_db_session):
    tag.name = tag.name.casefold()

    if await TagRepository.get_tag_by_name(tag.name, db) is not None:
        raise ExistTag

    await TagRepository.create_tag(tag, db)
