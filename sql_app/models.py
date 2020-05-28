from pydantic import BaseModel, Field
from typing import Optional


class User(BaseModel):
    name: str
    surname: str = None
    nationality: str = 'colombian'
    age: Optional[int]


class UserIn(User):
    password: str


class UserOut(User):
    pass


class UserUpdate(BaseModel):
    name: Optional[str]
    surname: Optional[str]
    nationality: Optional[str]
    age: Optional[int]
    password: Optional[str]


class Item(BaseModel):
    name: str
    description: Optional[str]
    price: float
    tax: Optional[float]


class ItemUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    tax: Optional[float]
