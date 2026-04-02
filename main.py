from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello utsav again 🚀"}


@app.get("/about")
def about():
    return {"message": "this is the about page"}


@app.get("/users/{name}")
def get_user(name: str):
    return {"user": name}


class User(BaseModel):
    name: str
    age: int


@app.post("/user")
def create_user(user: User):
    return {"message": "user created successfully", "data": user}
