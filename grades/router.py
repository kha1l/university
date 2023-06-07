from fastapi import APIRouter, Depends
from grades.models import Grade
from sqlalchemy import insert, update
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from grades.schemas import GradeCreate, GradeUpdate


router = APIRouter(
    prefix="/grades",
    tags=["Grades"]
)

@router.post('/')
async def add_grade(grade: GradeCreate,
                    session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Grade).values(**grade.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": 200, "data": grade.dict()}


@router.put("/{grade_id}")
async def update_grade(grade_id: int, new_grade: GradeUpdate,
                       session: AsyncSession = Depends(get_async_session)):
    stmt = update(Grade).where(Grade.grade_id == grade_id).values(**new_grade.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": 200, "data": new_grade}
