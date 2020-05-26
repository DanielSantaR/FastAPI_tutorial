from fastapi import Body, FastAPI, Query, Path
from pydantic import BaseModel
from typing import Optional


class Car(BaseModel):
    manufacturer: str
    reference: str
    year: int
    color: Optional[str]
    price: float


class User(BaseModel):
    name: str
    surname: str


app = FastAPI()


@app.put('/user/{user_id}/car/{car_id}')
async def new_car(
    *,
    user_id: int = Path(..., ge=0),
    user: User,
    q_user: str = Body(None, max_length=30),
    car: Car,
    car_id: int = Path(..., ge=0),
    q_car: str = Query(None, min_length=5, max_length=30)
):
    result = {'user id': user_id, 'user': user}
    if(q_user):
        result.update({'user description': q_user})

    result.update({'car id:': car_id, 'car': car})
    if(q_car):
        result.update({'car description': q_car})

    return result
