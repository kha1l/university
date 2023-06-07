from pydantic import BaseModel
from datetime import date

class GetTeachers(BaseModel):
    first_name: str
    last_name: str
    birth: date
    phone: str
    department_id: int

    class Config:
        orm_mode = True
