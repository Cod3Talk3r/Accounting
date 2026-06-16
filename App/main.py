from fastapi import FastAPI
from db.init_db import init_db
from contextlib import asynccontextmanager
import routers.users as users
import routers.auth as auth
import routers.tags as tags


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()

    yield


app = FastAPI(lifespan=lifespan)


@app.get("/AppHealth")
async def health():
    return {"Health": "App is Healthy"}


app.include_router(users.router, prefix="/User")
app.include_router(tags.router, prefix="/Tag")
app.include_router(auth.router)

