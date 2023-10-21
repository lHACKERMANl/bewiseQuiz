from fastapi import APIRouter, HTTPException, routing
from Common.settings import settings
from Repositories.InputData import InputData
from Services.questionRequest import QuestionService


router = APIRouter()

questionService = QuestionService()

@router.post("/question/")
async def sendQuestionNum(question_data: InputData):
    question_num = str(question_data.question_num)
    questions = await questionService.getQuestions(question_num)
    return {"questions":f"{questions}"}

