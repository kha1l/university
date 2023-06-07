from pydantic import BaseModel

class GradeCreate(BaseModel):
    student_id: int
    course_id: int
    semester_id: int
    value: float

    class Config:
        orm_mode = True

class GradeUpdate(BaseModel):
    value: float

    class Config:
        orm_mode = True
