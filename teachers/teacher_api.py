from fastapi import APIRouter
from datetime import datetime

from database.teacher_servise import register_teacher_db, get_teacher_db, \
    get_all_teachers_db, edit_teacher_db, delete_teacher_db, check_teacher_db
from teachers import TeacherRegistrationValidator, EditStudentValidator

teacher_router = APIRouter(prefix='/teacher', tags=['Teacher-2'])

@teacher_router.post('/register')
async def register_new_teacher(data:TeacherRegistrationValidator):

    new_teacher_data = data.model_dump()

    check_teacher = check_teacher_db(data.email)

    if check_teacher:
        return {'message': 'Teacher with this email is allready exist!'}
    else:
        result = register_teacher_db(reg_data=datetime.now(), **new_teacher_data)

        return result

@teacher_router.post('/edit-teacher')
async def edit_teacher(data:EditStudentValidator):

    change_data = data.model_dump()

    result = edit_teacher_db(**change_data)

    return result

@teacher_router.get('/get-teacher')
async def get_teacher(teacher_id: int):

    result = get_teacher_db(teacher_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Teacher not found((('}

@teacher_router.get('/get-all-teachers')
async def delete_all_teachers():

    all_teachers = get_all_teachers_db()

    if all_teachers:
        return {'message': all_teachers}
    else:
        return {'message': 'This teacher is not exist'}

@teacher_router.delete('/delete-teacher')
async def delete_all_teachers(teacher_id: int):

    del_teacher = delete_all_teachers(teacher_id)

    if del_teacher:
        return {'message': 'Teacher successfully deleted'}
    else:
        return {'message': 'This teacher is not exist('}

