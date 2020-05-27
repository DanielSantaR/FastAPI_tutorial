from fastapi import FastAPI, Path
from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    username: str
    email: EmailStr


class UserAccountBD(User):
    hashed_password: str
    age: int = None


class UserIn(User):
    password: str
    age: int = None


class UserOut(User):
    pass


app = FastAPI()


def fake_password(original_password: str):
    return 'fake' + original_password + 'fake'


def save_user_db(user_in: UserIn):
    hashed_password = fake_password(user_in.password)
    user_db = UserAccountBD(**user_in.dict(), hashed_password=hashed_password)
    print('User saved successfully')
    return user_db


@app.post('/new/', response_model=UserOut)
async def new_user(
    *,
    user: UserIn
):
    saved_user = save_user_db(user)
    return saved_user

