from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, ForeignKey

Base = declarative_base()

class Grade(Base):
    __tablename__ = 'grade'

    grade_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.student_id'))
    course_id = Column(Integer, ForeignKey('course.course_id'))
    value = Column(Float)
    semester_id = Column(Integer, ForeignKey('semester.semester_id'))
