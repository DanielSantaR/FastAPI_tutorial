from fastapi import FastAPI, HTTPException
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


users = {
    0: {
        'user_name': 'juan',
        'user_surname': 'lopez',
        'user_nationality': 'colombian',
        'password': '1235'
    },
    1: {
        'user_name': 'lucas',
        'user_surname': 'ocampo',
        'user_nationality': 'rusian',
        'age': 20,
        'password': 'abcdf'
    },
}

items = {
    0: {
        'item_name': 'reloj',
        'item_description': 'reloj de oro',
        'item_price': 2000,
    },
    1: {
        'item_name': 'celular',
        'item_price': 2000,
        'item_tax': 0.5,
    }
}


app = FastAPI()


@app.get('/user/{user_id}', response_model=UserOut)
async def get_user_by_id(
    *,
    user_id: int
):
    if user_id not in users:
        raise HTTPException(status_code=404, detail='User not found')
    found_user = users[user_id]
    return UserOut(**found_user)


@app.get('/item/{item_id}', response_model=Item)
async def get_item_by_id(
    *,
    item_id: int
):
    if item_id not in items:
        raise HTTPException(status_code=404, detail='Item not found')
    found_item = items[item_id]
    return Item(**found_item)
