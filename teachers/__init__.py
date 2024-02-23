from pydantic import BaseModel

class TeacherRegistrationValidator(BaseModel):
    name: str
    surname: str
    password: str
    school: int
    email: str

class EditStudentValidator(BaseModel):
    teacher_id: int
    edit_info: str
    new_info: str