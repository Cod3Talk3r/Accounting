from db.database import engine, Base, SessionLocal
from fastapi import Depends


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_db():
    async with SessionLocal() as session:
        yield session


get_db_session = Depends(get_db)
