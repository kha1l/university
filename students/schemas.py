from pydantic import BaseModel
from datetime import date

class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    birth: str
    phone: str
    group_id: int
    course_id: int

    class Config:
        orm_mode = True

class GetStudent(BaseModel):
    student_id: int
    first_name: str
    last_name: str
    birth: date
    phone: str
    group_id: int
    course_id: int

    class Config:
        orm_mode = True
