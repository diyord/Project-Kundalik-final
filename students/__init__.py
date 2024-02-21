from pydantic import BaseModel


class StudentRegistrationValidator(BaseModel):
    name: str
    surname: str
    phone_number: int
    password: str
    school: int
    grate: int
    email: str

class EditStudentValidator(BaseModel):
    student_id: int
    edit_date: str
    new_date: str