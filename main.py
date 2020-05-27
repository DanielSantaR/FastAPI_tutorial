from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse
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


class UnicornException(Exception):
    def __init__(self, id: str):
        self.id = id


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


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=430,
        content={'message': f'id {exc.id} not found'}
    )


@app.get(
    '/user/{user_id}',
    response_model=UserOut,
    tags=['users'],
    summary='get user by id',
    response_description='The found user with id',
)
async def get_user_by_id(
    *,
    user_id: int
):
    """
    Get all the information of a user

    - **user_name:** required
    - **surname:** required
    - **nationality:** required
    - **age:** optional
    """
    if user_id not in users:
        raise UnicornException(user_id)
    found_user = users[user_id]
    return UserOut(**found_user)


@app.get(
    '/item/{item_id}',
    response_model=Item,
    tags=['items'],
    description='get all the information of an item by id',
    deprecated=True,
)
async def get_item_by_id(
    *,
    item_id: int
):
    if item_id not in items:
        raise UnicornException(item_id)
    found_item = items[item_id]
    return Item(**found_item)
