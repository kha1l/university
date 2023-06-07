from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class Course(Base):
    __tablename__ = 'course'

    course_id = Column(Integer, primary_key=True)
    course_name = Column(String(100), nullable=False)
    department_id = Column(Integer, ForeignKey('department.department_id'))
