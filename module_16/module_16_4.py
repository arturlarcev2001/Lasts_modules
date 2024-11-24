from fastapi import FastAPI, status, Body, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int
    


@app.get("/users")
def get_all_users() -> List[User]:
    return users



@app.post("/users/{username}/{age}")
def create_user(username, age):
    try:
        user = User(
                'id': id,
                'username': username,
                'age': age
                )
        if user not in users:
            users.append(user)
        else:
            raise HTTPException(status_code=404, detail="User already exists")
    except:
        print('Unknown error')
    return users
        

@app.put("/users/{user_id}")
def update_user(user_id: int, user: str = Body()) -> str:
    try:
        name = user.username
        age = user.age
        return f"User updated!"
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{user_id}")
def delete_user(user_id: int) -> str:
    try:
        users.pop(user_id)
        return f"User ID={user_id} deleted!"
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")


@app.delete("/")
def delete_all_users() -> str:
    users.clear()
    return "All users deleted!"
