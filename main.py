from fastapi import FastAPI
from uuid import uuid4
from api import router as encode_router
from models import User, Gender, Role

app = FastAPI()

db: list[User] = [
    User(
        id=uuid4(), 
        first_name='Ramin', 
        last_name='Fallahzadeh',
        gender=Gender.male,
        roles=[Role.admin] 
        ),
    User(
        id=uuid4(), 
        first_name='Chris', 
        last_name='Arboleda',
        gender=Gender.male,
        roles=[Role.student]
        )
]

app.include_router(encode_router, prefix="/encode", tags=["encode"])
