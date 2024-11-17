from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()


@app.get('/')
async def main():
    return ({'message': 'Главная страница'})


@app.get('/user/admin')
async def admin():
    return ({'message': 'Вы вошли как админ'})

    
@app.get('/user/{user_id}')
async def user(
    user_id: Annotated[int,
                Path(
                    ge=1,
                    le=100,
                    description="Enter user ID"
                )
                      ]
    ):
    return ({'message': f'Вы вошли как пользователь № {user_id}'})

    
@app.get('/user/{username}/{age}')
async def user_info(
    username: Annotated[str,
                Path(
                    min_legth=5,
                    max_length=20,
                    description="Enter username", 
                    example="tharn"
                    )
                       ],
            
    age: Annotated[int, 
                Path(
                    ge=18,
                    lt=120,
                    description="Enter age"
                    )
                       ]
    ):
    return ({'message': f'Информация о пользователе, имя:{username}, вораст:{age}'})
