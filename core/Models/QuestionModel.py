from pydantic import BaseModel
from datetime import datetime

class QuestionModel(BaseModel):
    id: int
    question: str
    answer: str
    created_at: datetime
