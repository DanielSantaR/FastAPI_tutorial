from fastapi import Body, FastAPI, Query, Path
from pydantic import BaseModel, Field
from typing import List, Set, Optional


class Car(BaseModel):
    manufacturer: str = Field(..., min_length=5, max_length=20)
    reference: str = Field(..., min_length=5, max_length=30)
    year: int = Field(..., ge=1900, le=2021)
    color: Optional[str] = Field(None, min_length=5, max_length=20)
    price: float = Field(..., ge=0)
    tags: Set[Optional[str]] = []
    #tags: List[Optional[str]] = []


class User(BaseModel):
    name: str
    surname: str


app = FastAPI()


@app.put('/user/{user_id}/car/{car_id}')
async def update_car(
    *,
    user_id: int = Path(..., ge=0),
    user: User = Body(..., embed=True),
    q_user: str = Body(None, max_length=30),
    car: Car = Body(..., embed=True),
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
