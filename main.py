#Python
from uuid import UUID
from datetime import date
from typing import Optional

# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

# FastAPI
from fastapi import FastAPI

app = FastAPI()

class UserBase(BaseModel):
    user_id: UUID = Field(...)  #Se crea user_id para que no se repita el usuario con la libreria UUID de python
    email: EmailStr = Field(...) #con la funcion Field(...) se realiza autenticacion para que sea obligatorio

class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64
    )
class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    birth_date: Optional[date] = Field(default=None)

class Tweet(BaseModel):
    pass


@app.get(path= "/")
def home():
    return{"twitter API": "Working!"}