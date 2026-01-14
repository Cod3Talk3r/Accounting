from fastapi import Depends
from db.database import SessionLocal, AsyncSession


async def get_db():
    async with SessionLocal() as session:
        yield session


get_db_session: AsyncSession = Depends(get_db)
