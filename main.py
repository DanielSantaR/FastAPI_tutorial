from fastapi import Body, FastAPI, Path, Query
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Set, Optional


class Owner(BaseModel):
    owner_name: str = Field(..., min_length=2, max_length=20)
    owner_surname: str = Field(..., min_length=2, max_length=20)
    owner_age: int = Field(None, gt=0)


class DogImage(BaseModel):
    image_url: HttpUrl
    image_name: str = Field(None, min_length=2)


class Dog(BaseModel):
    dog_name: str = Field(..., min_length=2, max_length=20)
    dog_breed: str = Field(..., min_length=2, max_length=20)
    dog_age: int = Field(None, gt=0)
    dog_weight: float = Field(None, gt=0)
    dog_tags: Set[Optional[str]]
    dog_owner: Owner
    dog_image: List[Optional[DogImage]]


app = FastAPI()


@app.put('/dogs/{dog_id}')
async def update_dog(
    *,
    dog_id: int = Path(..., ge=0),
    dog: Dog = Body(..., embed=True),
    q: str = Query(None)
):
    result = {'dog_id': dog_id, 'Dog': dog}
    if(q):
        result.update({'description': q})
    return result
