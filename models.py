from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    user_name: str
    user_surname: str
    user_nationality: str
    user_age: Optional[int]


class UserIn(User):
    user_password: str


class UserOut(User):
    pass


class Item(BaseModel):
    item_name: str
    item_description: Optional[str]
    item_price: float
    item_tax: Optional[float]
