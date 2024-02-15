from fastapi import FastAPI
from fastapi.params import Body
app = FastAPI()

@app.get("/")
async def root():
    return   {"message": "Hello World"}


@app.post("/post")
async def create_post(payload: dict = Body(...)):
    print('payload',payload)
    return   {"message": "Hello World"}

