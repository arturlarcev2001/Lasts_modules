from fastapi import FastAPI, status, Body, HTTPException, Path
from pydantic import BaseModel
from typing import Annotated

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
async def create_user(
    username: Annotated[str,
                Path(
                  min_length=5,
                  max_length=15,
                  description="Enter user name"
                  )
              ],
    age:      Annotated[int,
                        Path(
                            ge=16,
                            le=80,
                            description="Enter user age"
                            )
                        ]
    ):
    if len(users) == 0:
        id = 1
    else:
        id = len(users) + 1
    user = User(id=id, name=username, age=age)
    users.append(user)
    return f'User {id} was created'


@app.put('/users/{id}/{username}/{age}')
async def update_user(
        id: Annotated[int,
                      Path(
                           ge=1,
                           le=100,
                           description="Enter valid ID"
                      )
                     ],

        username: Annotated[str,
                            Path(
                                  min_length=5,
                                  max_length=15,
                                  description="Enter user name"
                            )
                           ],

        age: Annotated[int,
                       Path(
                             ge=16,
                             le=80,
                             description="Enter user age"
                            )
                           ]
       ):
    try:
        user = users[int(id)-1]
        user.name = username
        user.age = age
        return f'User {id} was updated'
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/users/{id}')
async def delete_user(
	id: Annotated[int,
                      Path(
                            ge=1,
                            le=100,
                            description="Enter valid ID"
                      )
                     ]
        ):
    try:
        user = users[id-1]
        users.pop(id-1)
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')
