from pydantic import BaseModel

class HomeworkRegistrationValidator(BaseModel):
    info_homework: str
    status_homework: int
    grade_of_homework: int

class EditHomeworkValidator(BaseModel):
    homework_id: int
    new_info: str
    new_date: int
