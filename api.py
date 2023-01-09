from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from uuid import UUID
from models import User, UserUpdateRequest 
import main
import requests




router = APIRouter()

@router.get('/read_test')
async def read_test():
    # http = urllib3.PoolManager()
    # response = http.request('GET', 'http://127.0.0.1:8000/encode/users/get_users')
    # response = requests.get('https://www.thunderclient.com/welcome')
    response = await get_all_users()
    print(response)
    print(type(response))
    print('\nhi\n')
    return {'Hello':'World'}


@router.get('/users/get_users')
async def get_all_users():
    return main.db

@router.post('/users/register_user')
async def register_user(user: User):
    main.db.append(user)
    return {'id':user.id}

@router.get('/users/{user_id}')
async def get_user(user_id: UUID):
    for user in main.db:
        if user.id == user_id:
            return user
    raise HTTPException(
        status_code=404,
        detail=f'user with id: {user_id} not found!'
    )

@router.delete('/users/{user_id}')
async def delete_user(user_id: UUID):
    for user in main.db:
        if user.id == user_id:
            main.db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f'user with id: {user_id} not found!'
    )

@router.put('/users/{user_id}')
async def update_user(user_id: UUID, user_update_req: UserUpdateRequest):
    for user in main.db:
        if user.id == user_id:
            if user_update_req.first_name != None:
                user.first_name = user_update_req.first_name
            if user_update_req.last_name != None:
                user.last_name = user_update_req.last_name
            if user_update_req.middle_name != None:
                user.middle_name = user_update_req.middle_name
            if user_update_req.roles:
                user.roles = user_update_req.roles
            return
    raise HTTPException(
        status_code=404,
        detail=f'user with id: {user_id} not found!'
    )