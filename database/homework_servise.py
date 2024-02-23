from database.models import Homework
from database import get_db


def add_homework_db(info_homework, status_homework, grade_of_homework):
    db = next(get_db())

    new_homework = Homework(info_homework=info_homework, status_homework=status_homework,
                            grade_of_homework=grade_of_homework)

    if new_homework:

        db.add(new_homework)
        db.commit()

        return 'Successfull!'
    else:
        return 'ERROR, try again!'


def get_homework_db(homework_id):
    db = next(get_db())

    get_homework = db.query(Homework).filter_by(homework_id=homework_id)

    if get_homework:
        return get_homework
    else:
        return 'Error, plz try again'


def edit_homework_db(homework_id, edit_info, new_info):
    db = next(get_db())

    edit_homework = db.query(Homework).filter_by(homework_id=homework_id).first()

    if edit_homework:
        if edit_info == 'info_homework':
            edit_homework.info_homework = new_info
            db.commit()
            return 'Successefull'
        elif edit_info == 'status_homework':
            edit_homework.status_homework = new_info
            db.commit()
            return 'Successefull'
        elif edit_info == 'grade_of_homework':
            edit_homework.grade_of_homework = new_info
            db.commit()
            return 'Successefull'
    else:
        return 'Error, plz try again'


def get_all_homework_db():
    db = next(get_db())

    all_homework = db.query(Homework).all()

    return all_homework


def check_homework_db(info_homework):
    db = next(get_db())

    checker = db.query(Homework).filter_by(info_homework=info_homework).first()

    if checker:
        return checker
    else:
        return None


def delete_homework_db(homework_id):
    db = next(get_db())

    delete_homework = db.query(Homework).filter_by(homework_id=homework_id).first()

    if delete_homework:
        return 'Homework successfully deleted'
    else:
        db.delete(delete_homework)
        db.commit()
        return 'Error, try again'
