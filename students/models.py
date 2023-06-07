from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'

    student_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    birth = Column(Date)
    phone = Column(String(30))
    group_id = Column(Integer, ForeignKey('group_.group_id'))
    course_id = Column(Integer, ForeignKey('course.course_id'))
