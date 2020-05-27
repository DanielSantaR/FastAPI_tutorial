from fastapi import FastAPI
from pydantic import BaseModel, Field
from starlette import status
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
    0: { 
        "name": "juan",
        "age": 20,
        "sex": "male",
        "student_grade": 10,
        },
    1: {
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
    person_id: int
):
    return people[person_id]

@app.post('/new/{person_id}', status_code=status.HTTP_201_CREATED)
async def new_student(
    *,
    person_id: int,
    student: Student
):
    people.update({person_id: {**student.dict()}})
    return {'message': f'{student.name} successfully saved'}
