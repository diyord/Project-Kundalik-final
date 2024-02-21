from fastapi import APIRouter
from database.student_servise import register_student_db, get_student_db, get_all_students_db, delete_student_db, edit_student_db, check_student_db
from datetime import datetime
from students import StudentRegistrationValidator, EditStudentValidator

student_router = APIRouter(prefix='/student', tags=['Students'])

@student_router.post('/registration-new-student')
async def register_student(data:StudentRegistrationValidator):

    new_student_data = data.model_dump()

    checker = check_student_db(data.email)

    if checker:
        return {'message': 'Student successfully registed'}

    else:
        result = register_student_db(reg_date=datetime.now(), **new_student_data)

        return result

@student_router.post('/edit')
async def edit_student(data:EditStudentValidator):

    change_data = data.model_dump()

    result = edit_student_db(**change_data)

    return result

@student_router.get('/get-student')
async def get_student(student_id: int):

    result = get_student_db(student_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Student not found('}

@student_router.get('/all-students')
async def get_all_users():

    all_students = get_all_students_db()

    if all_students:
        return {'message': all_students}
    else:
        return {'message': 'This student is not exist'}

@student_router.delete('/delete_users')
async def delete_all_users(student_id: int):

    del_student = delete_student_db(student_id)

    if del_student:
        return {'message': 'Student successfully deleted'}
    else:
        return {'message': 'This student is not exist'}

