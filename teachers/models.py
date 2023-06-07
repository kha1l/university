from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey

Base = declarative_base()


class Teacher(Base):
    __tablename__ = 'teacher'

    teacher_id = Column(Integer, primary_key=True)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    birth = Column(Date)
    phone = Column(String(30))
    department_id = Column(Integer, ForeignKey('department.department_id'))
