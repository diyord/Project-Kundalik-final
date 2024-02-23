from database.models import Student, Teacher
from database import get_db

def register_teacher_db(name,surname, password, school, email):
    db = next(get_db())

    register_teacher = Teacher(name=name, surname=surname, password=password, school=school, email=email)

    if register_teacher:

        db.add(register_teacher)
        db.commit()

        return 'Successfull!'
    else:
        return 'Error'


def get_teacher_db(teacher_id):
    db = next(get_db())

    get_teacher = db.query(Teacher).filter_by(teacher_id=teacher_id).first()

    if get_teacher:
        return get_teacher
    else:
        return 'Error(, try again'

def get_all_teachers_db():
    db = next(get_db())

    get_all_teachers = db.query(Teacher).all()

    return get_all_teachers

def check_teacher_email_db(email):
    db = next(get_db())

    check = db.query(Teacher).filter_by(email=email).first()

    if check:
        return check
    else:
        return None

def edit_teacher_db(teacher_id, edit_info, new_info):
    db = next(get_db())

    edit_teacher = db.query(Teacher).filter_by(teacher_id=teacher_id).first()

    if edit_teacher:
        if edit_info == 'name':
            edit_teacher.name = new_info
            db.commit()
            return 'Successefull!'
        elif edit_info == 'surname':
            edit_teacher.surname = new_info
            db.commit()
            return 'Successefull!'
        elif edit_info == 'password':
            edit_teacher.password = new_info
            db.commit()
            return 'Successefull!'
        elif edit_info == 'school':
            edit_teacher.school = new_info
            db.commit()
            return 'Successefull!'
        elif edit_info == 'email':
            edit_teacher.email = new_info
            db.commit()
            return 'Successefull!'
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
