from database.models import Student
from database import get_db

def register_student_db(name, surname, phone_number, password, school, grate, email):
    db = next(get_db())

    new_student = Student(name=name, surname=surname, phone_number=phone_number, password=password, \
                          school=school, grate=grate, email=email)
    db.add(new_student)
    db.commit()
def get_student_db(student_id):
    db = next(get_db())

    get_student = db.query(Student).filter_by(student_id=student_id)
    if get_student:
        return get_student
    else:
        return 'Error, student not found plz try again'
def get_all_students_db():
    db = next(get_db())

    all_students = db.query(Student).all()

    return all_students

def check_student_db(email):
    db = next(get_db())

    check = db.query(Student).filter_by(email=email).first()

    if check:
        return check
    else:
        return 'This email is not exist!'

def edit_student_db(student_id, edit_info, new_info):
    db = next(get_db())

    edit_student = db.query(Student).filter_by(student_id=student_id, edit_info=edit_info, new_info=new_info)

    if edit_student:
        if edit_info == 'name':
            edit_student.name = new_info
        elif edit_info == 'surname':
            edit_student.surname = new_info
        elif edit_info == 'password':
            edit_student.password = new_info
        elif edit_info == 'school':
            edit_student.school = new_info
        elif edit_info == 'grate':
            edit_student.grate = new_info
        elif edit_info == 'email':
            edit_student.email = new_info
        else:
            return 'Info successfully added!'
    else:
        return 'Error! this function is not exist!! Plz try another function'

def delete_student_db(student_id):
    db = next(get_db())

    delete_student = db.query(Student).filter_by(student_id=student_id).first()

    if not delete_student:
        return 'Student not found(('
    else:
        db.delete(delete_student)
        db.commit()
        return 'Student deleted'
