from db import items_storage, users_storage
from fastapi import FastAPI, HTTPException, Path
from fastapi.encoders import jsonable_encoder

# TODO: 
# es meejor importar las clases, en este caso modelos
# de pydantic de est forma

# from models import UserIn, ...

# de esta forma evitas estar escribiendo models en todo el codigo
# TODO

import models


app = FastAPI()

# TODO:
# En el PEP8 se habla de no superar los 80 caracteres en
# una misma linea de codigo pero tampoco es bueno exagerar queriendo
# que todo quede muy corto

# la definicion de la funcion podria ser mejor

# async def get_user_by_id(*, user_id: int):

# no supera los 80 caracteres y es mas facil de leer

# TODO

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

    - **user_name**
    - **user_surname**
    - **user_nationality**
    - **user_age**
    """
    if user_id not in users_storage:
        raise HTTPException(
            status_code=404, detail=f"No user found with id {user_id}"
        )
    found_user = users_storage[user_id]
# TODO:
# buen uso del destructor a la hora de crear un modelo nuevo
# TODO
    return models.UserOut(**found_user)

# TODO:
# En el PEP8 se habla de no superar los 80 caracteres en
# una misma linea de codigo pero tampoco es bueno exagerar queriendo
# que todo quede muy corto
# TODO

@app.post('/user/add_user/{user_id}', tags=['users'])
async def new_user(
    *,
    user_id: int = Path(..., ge=0),
    user: models.UserIn,
):
    if user_id in users_storage:
        raise HTTPException(
            status_code=409, detail=f"A user with id {user_id} already exists"
        )

# TODO:
# en vez de usar __dict__ es mas recomendable usar la funcion 
# propia de pydantic dict()
# users_storage.update({user_id: user.dict()})
# TODO

    users_storage.update({user_id: user.__dict__})

    message = "User successfully saved"
    return {'message': message}

# TODO:
# En el PEP8 se habla de no superar los 80 caracteres en
# una misma linea de codigo pero tampoco es bueno exagerar queriendo
# que todo quede muy corto

# este metodo de actualizar el usuario seria bueno hacerlo 
# de forma en que no toque ingresar otra vez todos los campos,
# mas bien que uno ingrese el que quiere actualizar
# TODO

@app.put('/user/update_user/{user_id}', tags=['users'])
async def update_user(
    *,
    user_id: int = Path(..., ge=0),
    user: models.UserIn,
):
    if user_id not in users_storage:
        raise HTTPException(
            status_code=404, detail=f"No user found with id {user_id}"
        )

# TODO:
# en vez de usar __dict__ es mas recomendable usar la funcion 
# propia de pydantic dict()
# TODO

    users_storage[user_id] = user.__dict__

    message = "User successfully updated"
    return {'message': message}


@app.patch('/user/patch/{user_id}', response_model=models.UserOut, tags=['users'])
async def update_partial_user(user_id: int, user: models.UserIn):
    if user_id not in users_storage:
        raise HTTPException(
            status_code=404, detail=f"No user found with id {user_id}"
        )
    stored_user_data = users_storage[user_id]
    stored_item_model = models.UserIn(**stored_user_data)
    update_data = user.dict(exclude_unset=True)
    updated_user = stored_item_model.copy(update=update_data)
    users_storage[user_id] = jsonable_encoder(updated_user)
    message = "User successfully updated"
    return {'message': message}

# TODO:
# En el PEP8 se habla de no superar los 80 caracteres en
# una misma linea de codigo pero tampoco es bueno exagerar queriendo
# que todo quede muy corto
# TODO

@app.delete('/user/delete_user/{user_id}', tags=['users'])
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

# TODO:
# En el PEP8 se habla de no superar los 80 caracteres en
# una misma linea de codigo pero tampoco es bueno exagerar queriendo
# que todo quede muy corto
# TODO

@app.get('/item/{item_id}', response_model=models.Item, tags=['items'])
async def get_item_by_id(
    *,
    item_id: int
):
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
    return models.Item(**found_item)


@app.post('/item/add_item/{item_id}', tags=['items'])
async def new_item(
    *,
    item_id: int = Path(..., ge=0),
    item: models.Item,
):
    if item_id in items_storage:
        raise HTTPException(
            status_code=409, detail=f"An item with id {item_id} already exists"
        )

# TODO:
# en vez de usar __dict__ es mas recomendable usar la funcion 
# propia de pydantic dict()
# TODO

    items_storage.update({item_id: item.__dict__})

    message = "Item successfully saved"
    return {'message': message}

# TODO:
# En el PEP8 se habla de no superar los 80 caracteres en
# una misma linea de codigo pero tampoco es bueno exagerar queriendo
# que todo quede muy corto

# este metodo de actualizar el item seria bueno hacerlo 
# de forma en que no toque ingresar otra vez todos los campos,
# mas bien que uno ingrese el que quiere actualizar
# TODO

@app.put('/item/update_item/{item_id}', tags=['items'])
async def update_all_item(
    *,
    item_id: int = Path(..., ge=0),
    item: models.Item,
):
    if item_id not in items_storage:
        raise HTTPException(
            status_code=404, detail=f"No item found with id {item_id}"
        )

# TODO:
# en vez de usar __dict__ es mas recomendable usar la funcion 
# propia de pydantic dict()
# TODO

    items_storage[item_id] = item.__dict__

    message = "Item successfully updated"
    return {'message': message}


@app.patch('/item/patch/{item_id}', response_model=models.Item, tags=['items'])
async def update_partial_item(item_id: int, item: models.Item):
    if item_id not in items_storage:
        raise HTTPException(
            status_code=404, detail=f"No item found with id {item_id}"
        )
    stored_item_data = items_storage[item_id]
    stored_item_model = models.Item(**stored_item_data)
    update_data = item.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_data)
    items_storage[item_id] = jsonable_encoder(updated_item)
    message = "Item successfully updated"
    return {'message': message}

# TODO:
# En el PEP8 se habla de no superar los 80 caracteres en
# una misma linea de codigo pero tampoco es bueno exagerar queriendo
# que todo quede muy corto
# TODO

@app.delete('/item/delete_item/{item_id}', tags=['items'])
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
