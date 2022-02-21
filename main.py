# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI

app = FastAPI()

class User(BaseModel):
    pass

class Tweet(BaseModel):
    pass


@app.get(path= "/")
def home():
    return{"twitter API": "Working!"}