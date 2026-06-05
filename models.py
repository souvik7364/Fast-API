from typing import Optional, List
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    description: str
    price: float
    quantity: int
    class Config():
        orm_mode=True

class User(BaseModel):
    username:str
    email:str
    password:str

class ShowUser(BaseModel):
    username:str
    email:str
    product: List[Product] = []
    class Config():
        orm_mode=True

class ShowProduct(BaseModel):
    name: str
    description: str
    price: float
    quantity: int
    owner: Optional[ShowUser] = None
    class Config():
        orm_mode=True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
