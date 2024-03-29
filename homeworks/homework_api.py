from fastapi import APIRouter

from database.homework_servise import add_homework_db, check_homework_db, \
    get_all_homework_db, get_homework_db, delete_homework_db, edit_homework_db

from datetime import datetime
from homeworks import HomeworkRegistrationValidator, EditHomeworkValidator

homework_router = APIRouter(prefix='/homework', tags=['Homework'])


@homework_router.post('/register-homework')
async def register_homework(data: HomeworkRegistrationValidator):
    new_student_data = data.model_dump()

    checker = check_homework_db(data.info_homework)

    if checker:
        return {'message': 'Homework with this info is allready exist'}
    else:
        result = add_homework_db(**new_student_data)

        return result


@homework_router.post('/edit')
async def edit_homework(data: EditHomeworkValidator):
    change_data = data.model_dump()

    result = edit_homework_db(**change_data)

    return result


@homework_router.get('get-homework')
async def get_homework(homework_id: int):
    result = get_homework_db(homework_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'homework not found('}


@homework_router.get('/get-all-homework')
async def get_all_homework():
    all_homeworks = get_all_homework_db()

    if all_homeworks:
        return {'message': all_homeworks}
    else:
        return {'message': 'This homework is not exist'}


@homework_router.delete('/delete-homework')
async def delete_homework(homework_id: int):
    del_homework = delete_homework_db(homework_id)

    if del_homework:
        return {'message': 'homework successfully deleted'}
    else:
        return {'message': 'This homework is not exist'}
