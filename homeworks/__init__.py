from pydantic import BaseModel

class HomeworkRegistrationValidator(BaseModel):
    info_homework: str
    status_homework: int
    grade_of_homework: int

class EditHomeworkValidator(BaseModel):
    homework_id: int
    edit_info: str
    new_info: int
