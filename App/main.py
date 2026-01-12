from fastapi import FastAPI


app = FastAPI()


@app.get("/AppHealth")
async def health():
    return {"Health": "App is Healthy"}
