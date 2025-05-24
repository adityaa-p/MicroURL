from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    url: str
    expiration_date: str
    custom_alias: str | None = None

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/urls")
async def post(item : Item):
    return item
