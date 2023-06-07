from pydantic import BaseModel

class CourseCreate(BaseModel):
    course_name: str
    department_id: int

    class Config:
        orm_mode = True

class GetCourse(BaseModel):
    course_id: int
    course_name: str
    department_id: int

    class Config:
        orm_mode = True
