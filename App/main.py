from fastapi import FastAPI
from db.init_db import init_db


app = FastAPI()


@app.on_event("startup")
async def start_up():
    await init_db()


@app.get("/AppHealth")
async def health():
    return {"Health": "App is Healthy"}
