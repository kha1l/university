from fastapi import FastAPI
from students.router import router as router_students
from teachers.router import router as router_teachers
from courses.router import router as router_courses
from grades.router import router as router_grades

app = FastAPI(
    title='Test Project'
)

# Роутер студентов
app.include_router(router_students)

# Роутер учетилей
app.include_router(router_teachers)

# Роутер курсов
app.include_router(router_courses)

# Роутер оценок
app.include_router(router_grades)
