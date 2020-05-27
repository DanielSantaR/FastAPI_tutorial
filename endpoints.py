from DB import items_storage, users_storage
from fastapi import FastAPI, HTTPException, Path
import models


app = FastAPI()


@app.get(
    '/user/{user_id}',
    response_model=models.UserOut,
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
    - **user_surname:** required
    - **user_nationality:** required
    - **user_age:** optional
    """
    if user_id not in users_storage:
        raise HTTPException(
            status_code=404, detail=f"No user found with id {user_id}"
        )
    found_user = users_storage[user_id]
    return models.UserOut(**found_user)


@app.post(
    '/user/add_user/{user_id}',
    tags=['users'],
)
async def new_user(
    *,
    user_id: int = Path(..., ge=0),
    user: models.UserIn,
):
    if user_id in users_storage:
        raise HTTPException(
            status_code=409, detail=f"A user with id {user_id} already exists"
        )
    users_storage.update({user_id: user.__dict__})

    message = "User successfully saved"
    return {'message': message}


@app.put(
    '/user/update_user/{user_id}',
    tags=['users'],
)
async def update_user(
    *,
    user_id: int = Path(..., ge=0),
    user: models.UserIn,
):
    if user_id not in users_storage:
        raise HTTPException(
            status_code=404, detail=f"No user found with id {user_id}"
        )
    users_storage[user_id] = user.__dict__

    message = "User successfully updated"
    return {'message': message}


@app.delete(
    '/user/delete_user/{user_id}',
    tags=['users'],
)
async def delete_user(
    *,
    user_id: int = Path(..., ge=0)
):
    if user_id not in users_storage:
        raise HTTPException(
            status_code=404, detail=f"No user found with id {user_id}"
        )
    users_storage.pop(user_id)

    message = "User successfully deleted"
    return {'message': message}


@app.get(
    '/item/{item_id}',
    response_model=models.Item,
    tags=['items'],
)
async def get_item_by_id(
    *,
    item_id: int
):
    """
    Get all the information of an item

    - **item_name:** required
    - **item_description:** optional
    - **item_price:** required
    - **item_tax:** optional
    """
    if item_id not in items_storage:
        raise HTTPException(
            status_code=404, detail=f"No item not found with id {item_id}"
        )
    found_item = items_storage[item_id]
    return models.Item(**found_item)


@app.post(
    '/items/add_item/{item_id}',
    tags=['items'],
)
async def new_item(
    *,
    item_id: int = Path(..., ge=0),
    item: models.Item,
):
    if item_id in items_storage:
        raise HTTPException(
            status_code=409, detail=f"An item with id {item_id} already exists"
        )
    items_storage.update({item_id: item.__dict__})

    message = "Item successfully saved"
    return {'message': message}


@app.put(
    '/item/update_item/{item_id}',
    tags=['items'],
)
async def update_item(
    *,
    item_id: int = Path(..., ge=0),
    item: models.Item,
):
    if item_id not in items_storage:
        raise HTTPException(
            status_code=404, detail=f"No item found with id {item_id}"
        )
    items_storage[item_id] = item.__dict__

    message = "Item successfully updated"
    return {'message': message}


@app.delete(
    '/item/delete_item/{item_id}',
    tags=['items'],
)
async def delete_item(
    *,
    item_id: int = Path(..., ge=0)
):
    if item_id not in items_storage:
        raise HTTPException(
            status_code=404, detail=f"No user found with id {item_id}"
        )
    items_storage.pop(item_id)

    message = "Item successfully deleted"
    return {'message': message}
