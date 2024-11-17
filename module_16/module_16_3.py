from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()
users = {'1': 'Имя: Мориган, возраст: 18'}


@app.get('/users')
async def get_users():
    return users


@app.post('/users/{username}/{age}')
async def add_user(username, age):
    new_user_id = str(
                    int(
                        max(users, key=int)
                        ) + 1
                     )
    users[new_user_id] = f'Имя: {username}, возраст: {age}'
    return f"User {new_user_id} is registered"


@app.put('/users/{user_id}/{username}/{age}')
async def update_user(user_id, username, age):
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is updated'
    
    
@app.delete('/users/{user_id}')
async def delete_user(user_id):
    users.pop(user_id)
    return f'User {user_id} is deleted'
