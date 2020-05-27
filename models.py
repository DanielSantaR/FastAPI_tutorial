from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    user_name: str = None
    user_surname: str = None
    user_nationality: str = 'colombian'
    user_age: Optional[int] = None


class UserIn(User):
    user_password: str = None


class UserOut(User):
    pass


class Item(BaseModel):
    item_name: str = None
    item_description: Optional[str] = None
    item_price: float = None
    item_tax: Optional[float] = None
