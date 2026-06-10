from fastapi import FastAPI
from db.init_db import init_db
import routers.users as users
import routers.auth as auth
import routers.tags as tags


app = FastAPI()


@app.on_event("startup")
async def start_up():
    await init_db()


@app.get("/AppHealth")
async def health():
    return {"Health": "App is Healthy"}


app.include_router(users.router, prefix="/User")
app.include_router(tags.router, prefix="/Tag")
app.include_router(auth.router)

