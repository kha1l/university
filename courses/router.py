from fastapi import APIRouter, Depends
from courses.models import Course
from students.models import Student
from students.schemas import GetStudent
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from courses.schemas import CourseCreate, GetCourse
from typing import List

router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)


@router.post('/')
async def add_course(course: CourseCreate,
                     session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Course).values(**course.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": 200, "data": course.dict()}


@router.get("/{course_id}", response_model=List[GetCourse])
async def get_course(course_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Course).where(Course.course_id == course_id)
    result = await session.execute(query)
    return result.scalars().all()

@router.get('/{course_id}/students', response_model=List[GetStudent])
async def get_students_by_course(course_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Student).where(Student.course_id == course_id)
    result = await session.execute(query)
    return result.scalars().all()
