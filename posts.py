from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

posts = []

class Post(BaseModel):
    id: int
    title: str
    content: str

@app.get("/posts")
def get_posts():
    return posts
    
@app.post("/posts")
def create_posts(post: Post):
    posts.append(post)
    return {"message": "post created successfully!!"}
    