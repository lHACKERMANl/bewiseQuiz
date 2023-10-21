import httpx
import logging



class QuestionService:
    async def getQuestions(self, questionNum):
        async with httpx.AsyncClient() as client:
            response = await client.get(f'https://jservice.io/api/random?count={questionNum}')

            if response.status_code == 200:
                questions = response.json()
                logging.debug("questionRequest.py | Success: " + str(questions))
                return questions
            else:                
                logging.warning(f"You did not get any questions: status - {str(response.status_code)} \n url - https://jservice.io/api/random?count={questionNum}")
                return None
