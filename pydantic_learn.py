from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

"""
#create schema
class User(BaseModel):
    name: str
    age: int
    email: str
    
@app.post("/create-user")
def create_user(data: User):
    return {
        "message": "User created",
        "data": data
        }
"""
#schema
class Address(BaseModel):
    village: str
    p_o: str
    p_s: str
    pin: int
 #nested schema   
class User(BaseModel):
    name: str
    age: int
    address: Address
    
@app.post("/create-user")
def create_user(user: User):
    return {
        "message": "User Create",
        "Data": user
        }

