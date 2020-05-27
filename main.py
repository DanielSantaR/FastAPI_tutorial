from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Union


class Person(BaseModel):
    name: str
    age: int
    sex: str
    profession: str


class Student(Person):
    profession = "student"
    student_grade: int = Field(..., ge=0, le=11)


class Teacher(Person):
    profession = "teacher"
    teacher_courses: List[int] = Field(..., ge=0, le=11)


people = {
    "person_1": { 
        "name": "juan",
        "age": 20,
        "sex": "male",
        "student_grade": 10,
        },
    "person_2": {
        "name": "lucas",
        "age": 40,
        "sex": "male",
        "teacher_courses": [7,8,9,10],        
    },
}


app = FastAPI()

@app.get('/{person_id}', response_model=Union[Student, Teacher])
async def get_anyone(
    *,
    person_id: str
):
    return people[person_id]