from sql_app.db import items_storage, users_storage
from fastapi import FastAPI, HTTPException, Path
from fastapi.encoders import jsonable_encoder
from sql_app.models import Item, ItemUpdate, UserIn, UserOut, UserUpdate


app = FastAPI()


@app.get(
    '/user/{user_id}',
    response_model=UserOut,
    tags=['users'],
    summary='get user by id',
    response_description='The found user with id',
)
async def get_user_by_id(user_id: int):
    """
    Get all the information of a user

    - **name**
    - **surname**
    - **nationality**
    - **age**
    """

    print(users_storage[user_id])

    if user_id not in users_storage:
        raise HTTPException(
            status_code=404, detail=f"No user found with id {user_id}"
        )
    found_user = users_storage[user_id]
    return UserOut(**found_user)


@app.post('/user/add_user/{user_id}', tags=['users'])
async def new_user(user: UserIn, user_id: int = Path(..., ge=0)):
    if user_id in users_storage:
        raise HTTPException(
            status_code=409, detail=f"A user with id {user_id} already exists"
        )
    users_storage.update({user_id: user.dict()})

    message = "User successfully saved"
    return {'message': message}


@app.put('/user/update_user/{user_id}', tags=['users'])
async def update_user(user: UserUpdate, user_id: int = Path(..., ge=0)):
    if user_id not in users_storage:
        raise HTTPException(
            status_code=404, detail=f"No user found with id {user_id}"
        )
    if (user.name and user.name != users_storage[user_id]['name']):
        users_storage[user_id]['name'] = user.name
    if (user.surname and user.surname != users_storage[user_id]['surname']):
        users_storage[user_id]['surname'] = user.surname
    if (user.surname and user.surname != users_storage[user_id]['surname']):
        users_storage[user_id]['surname'] = user.surname
    if (user.nationality and user.nationality != users_storage[user_id]['nationality']):
        users_storage[user_id]['nationality'] = user.nationality
    if (user.age and user.age != users_storage[user_id]['age']):
        users_storage[user_id]['age'] = user.age
    if (user.password and user.password != users_storage[user_id]['password']):
        users_storage[user_id]['password'] = user.password

    message = "User successfully updated"
    return {'message': message}


@app.delete('/user/delete_user/{user_id}', tags=['users'])
async def delete_user(user_id: int = Path(..., ge=0)):
    if user_id not in users_storage:
        raise HTTPException(
            status_code=404, detail=f"No user found with id {user_id}"
        )
    users_storage.pop(user_id)

    message = "User successfully deleted"
    return {'message': message}


@app.get('/item/{item_id}', response_model=Item, tags=['items'])
async def get_item_by_id(item_id: int):
    """
    Get all the information of an item

    - **item_name**
    - **item_description**
    - **item_price**
    - **item_tax**
    """
    if item_id not in items_storage:
        raise HTTPException(
            status_code=404, detail=f"No item not found with id {item_id}"
        )
    found_item = items_storage[item_id]
    return Item(**found_item)


@app.post('/item/add_item/{item_id}', tags=['items'])
async def new_item(item: Item, item_id: int = Path(..., ge=0)):
    if item_id in items_storage:
        raise HTTPException(
            status_code=409, detail=f"An item with id {item_id} already exists"
        )
    items_storage.update({item_id: item.dict()})

    message = "Item successfully saved"
    return {'message': message}


@app.put('/item/update_item/{item_id}', tags=['items'])
async def update_all_item(item: ItemUpdate, item_id: int = Path(..., ge=0)):
    if item_id not in items_storage:
        raise HTTPException(
            status_code=404, detail=f"No item found with id {item_id}"
        )
    if (item.name and item.name != items_storage[item_id]['name']):
        items_storage[item_id]['name'] = item.name
    if (item.description and item.description != items_storage[item_id]['description']):
        items_storage[item_id]['description'] = item.description
    if (item.price and item.price != items_storage[item_id]['price']):
        items_storage[item_id]['price'] = item.price
    if (item.tax and item.tax != items_storage[item_id]['tax']):
        items_storage[item_id]['tax'] = item.tax

    message = "Item successfully updated"
    return {'message': message}


@app.delete('/item/delete_item/{item_id}', tags=['items'])
async def delete_item(item_id: int = Path(..., ge=0)):
    if item_id not in items_storage:
        raise HTTPException(
            status_code=404, detail=f"No user found with id {item_id}"
        )
    items_storage.pop(item_id)

    message = "Item successfully deleted"
    return {'message': message}
