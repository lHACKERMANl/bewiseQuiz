from pydantic import BaseModel

class InputData(BaseModel):
    question_num: int
