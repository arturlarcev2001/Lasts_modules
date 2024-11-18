from fastapi import FastAPI, status, Body, HTTPException
from pydantic import BaseModel


app = FastAPI()
users = []


class User(BaseModel):
    id: int
    name: str
    age: int


@app.get('/users')
async def get_users():
    return users


@app.post('/users/{username}/{age}')
async def create_user(username, age):
    if len(users) == 0:
        id = 1
    else:
        id = len(users) + 1
    user = User(id=id, name=username, age=age)
    users.append(user)
    return f'User {id} was created'


@app.put('/users/{id}/{username}/{age}')
async def update_user(id, username, age):
    try:
        user = users[int(id)-1]
        user.name = username
        user.age = age
        return f'User {id} was updated'
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/users/{id}')
async def delete_user(id):
    try:
        user = users[id]
        users.pop(id)
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')
