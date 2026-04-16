import random

from fastapi import FastAPI

app = FastAPI()

#http://127.0.0.1:8000/
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/teste1")
async def funcaoteste():
    return {"teste":"deu certo"}