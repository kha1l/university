from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from sqlalchemy import select, insert, update, delete
from students.models import Student
from students.schemas import StudentCreate, GetStudent
from datetime import date
from typing import List


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

@router.post('/')
async def add_student(student: StudentCreate,
                      session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Student).values(
        first_name=student.first_name,
        last_name=student.last_name,
        birth=date.fromisoformat(student.birth),
        phone=student.phone,
        group_id=student.group_id,
        course_id=student.course_id
    )
    await session.execute(stmt)
    await session.commit()
    return {"status": 200, "data": student.dict()}

@router.get("/{student_id}", response_model=List[GetStudent])
async def get_student(student_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Student).where(Student.student_id == student_id)
    result = await session.execute(query)
    return result.scalars().all()

@router.put("/{student_id}")
async def update_student(student_id: int, student_data: StudentCreate,
                         session: AsyncSession = Depends(get_async_session)):
    stmt = update(Student).where(Student.student_id == student_id).values({
            Student.first_name: student_data.first_name,
            Student.last_name: student_data.last_name,
            Student.birth: date.fromisoformat(student_data.birth),
            Student.phone: student_data.phone,
            Student.group_id: student_data.group_id,
            Student.course_id: student_data.course_id
        })
    await session.execute(stmt)
    await session.commit()
    return {"status": 200, "data": student_data}

@router.delete("{student_id")
async def delete_student(student_id: int, session: AsyncSession = Depends(get_async_session)):
    query = delete(Student).where(Student.student_id == student_id)
    await session.execute(query)
    await session.commit()
    return {"status": 200, "data": {'delete': f'id - {student_id}'}}
