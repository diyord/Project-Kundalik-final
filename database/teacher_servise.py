from database.models import Student, Teacher
from database import get_db

def register_teacher_db(name,surname, password, teacher_id, school, email):
    db = next(get_db())

    register_teacher = Teacher(name=name, surname=surname, password=password, teacher_id=teacher_id, school=school, email=email)

    db.add(register_teacher)
    db.commit()
    return 'Successfull!'
def get_teacher_db(teacher_id):
    db = next(get_db())

    get_teacher = db.query(Teacher).filter_by(teacher_id=teacher_id)

    if get_teacher:
        return get_teacher
    else:
        return 'Error(, try again'

def get_all_teachers_db():
    db = next(get_db())

    get_all_teachers = db.query(Teacher).all()

    if get_all_teachers:
        return get_all_teachers
    else:
        return 'Error(, try again'

def check_teacher_db(email):
    db = next(get_db())

    check = db.query(Teacher).filter_by(email=email).first()

    if check:
        return check
    else:
        return 'This email is not exist!'

def edit_teacher_db(teacher_id, edit_info, new_info):
    db = next(get_db())

    edit_teacher = db.query(Student).filter_by(teacher_id=teacher_id, new_info=new_info, edit_info=edit_info)

    if edit_teacher:
        if edit_info == 'name':
            edit_teacher.name = new_info
        elif edit_info == 'surname':
            edit_teacher.surname = new_info
        elif edit_info == 'password':
            edit_teacher.password = new_info
        elif edit_info == 'school':
            edit_teacher.school = new_info
        elif edit_info == 'email':
            edit_teacher.email = new_info
        else:
            return 'Information successfully changed!'
    else:
        return 'Error((, try again plz'

def delete_teacher_db(teacher_id):
    db = next(get_db())

    teacher = db.query(Teacher).filter_by(teacher_id=teacher_id).first()

    if not teacher:
       return 'Teacher not found((('
    else:
       db.delete(teacher)
       db.commit()
       return 'Teacher deleted!'
