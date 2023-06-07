from fastapi import APIRouter, Depends
from teachers.models import Teacher
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from teachers.schemas import GetTeachers
from typing import List


router = APIRouter(
    prefix="/teachers",
    tags=["Teachers"]
)

@router.get("/", response_model=List[GetTeachers])
async def get_teachers(session: AsyncSession = Depends(get_async_session)):
    query = select(Teacher)
    result = await session.execute(query)
    return result.scalars().all()


