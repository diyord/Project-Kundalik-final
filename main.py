from fastapi import FastAPI

from students.student_api import student_router
from teachers.teacher_api import teacher_router
from homeworks.homework_api import homework_router

from database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

app.include_router(student_router)
app.include_router(teacher_router)
app.include_router(homework_router)