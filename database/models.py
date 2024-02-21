from sqlalchemy import Column, Integer, String
from database import Base

class Student(Base):
    __tablename__ = 'Student'
    name = Column(String)
    surname = Column(String)
    student_id = Column(Integer, primary_key=True, autoincrement=True)
    phone_number = Column(String, unique=True)
    password = Column(Integer)
    school = Column(Integer)
    grate = Column(Integer)
    email = Column(String)

class Teacher(Base):
    __tablename__ = 'Teacher'
    name = Column(String)
    surname = Column(String)
    teacher_id = Column(Integer, primary_key=True, autoincrement=True)
    password = Column(Integer, unique=True)
    school = Column(Integer)
    email = Column(String)

class Homework(Base):
    __tablename__ = 'Homework'
    info_homework = Column(String)
    homework_id = Column(Integer, primary_key=True, autoincrement=True)
    status_homework = Column(String)
    grade_of_homework = Column(Integer, default=0)
