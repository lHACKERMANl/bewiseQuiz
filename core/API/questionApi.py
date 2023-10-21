from fastapi import APIRouter, HTTPException, routing
from Models.InputData import InputData
from Services.questionRequest import QuestionService


router = APIRouter()

questionService = QuestionService()

@router.post("/question/")
async def sendQuestionNum(question_data: InputData):
    question_num = str(question_data.question_num)
    questions = await questionService.getQuestions(question_num)
    if questions:
        await questionService.saveQuestions(questions)
    return {"questions":f"{questions}"}

