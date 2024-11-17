from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def main():
    return ({'message': 'Главная страница'})


@app.get('/user/admin')
async def admin():
	return ({'message': 'Вы вошли как админ'})

	
@app.get('/user/{user_id}')
async def user(user_id):
	return ({'message': f'Вы вошли как пользователь № {user_id}'})

	
@app.get('/user')
async def user_info(username='Sonic the hedgehog', user_age=9999):
	return ({'message': f'Информация о пользователе, имя:{username}, вораст:{user_age}'})
