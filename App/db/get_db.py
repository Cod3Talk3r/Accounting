from fastapi import Depends
from db.database import SessionLocal


async def get_db():
    async with SessionLocal() as session:
        yield session


get_db_session = Depends(get_db)
