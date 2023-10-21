import httpx
import logging
from Repositories.MongoRepository import MongoRepository
from Common.settings import settings


logger = logging.getLogger('debugging')
repo = MongoRepository(settings.uri,settings.db,settings.collection,settings.user,settings.password)

class QuestionService:
    async def getQuestions(self, questionNum):
        async with httpx.AsyncClient() as client:
            response = await client.get(f'https://jservice.io/api/random?count={questionNum}')

            if response.status_code == 200:
                questions = response.json() 
                logger.debug("Success: " + str(questions))
                return questions
            else:                
                logger.warning(f"You did not get any questions: status - {str(response.status_code)} \n url - https://jservice.io/api/random?count={questionNum}")
                return None

    async def saveQuestions(self, questions):
        for question in questions:
            if not await repo.isQuestionExists(question["id"]):
                saveId = await repo.saveData(question)
                logger.debug(f'saveId: {saveId}')
            else:
                logger.debug(f'question {question["id"]} is existing')
                newQuestion = await self.getQuestions(1)
                await self.saveQuestions(newQuestion)



