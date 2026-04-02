from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello utsav again 🚀"}


@app.get("/about")
def about():
    return {"message": "this is the about page"}


# @app.get("/users/{name}")
# def get_user(name: str):
#     return {"user": name}


# class User(BaseModel):
#     name: str
#     age: int


# @app.post("/user")
# def create_user(user: User):
#     return {"message": "user created successfully", "data": user}



# creating a small crud application
class User(BaseModel):
    id: int
    name: str
    age: int

users = []

# Create user
@app.post("/users")
def create_user(user: User):
    users.append(user)
    return {"message": "user added successfully", "data": user}

# READ all
@app.get("/users")
def get_users():
    return users

@app.get("/users/{user_id}")
def get_userbyId(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code= 404, detail= "User not found")
    
# Update a user
@app.put("/users/{user_id}")
def update_user(user_id:int, updated_user: User):
    for index, user in enumerate(users):
        if user.id == user_id:
            users[index] = updated_user
            return {"message": "user updated successfully", "data": updated_user}
    raise HTTPException(status_code= 500, detail= "Failed, internal server error")
    
# Delete a user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return {"message": "user deleted successfully"}
    raise HTTPException(status_code= 500, detail = "Failed, internal server error")
            
