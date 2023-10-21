from Repositories.IRepository import IRepository
from pymongo import MongoClient
from Models.QuestionModel import QuestionModel
import logging


logger = logging.getLogger('debugging')
class MongoRepository(IRepository):
    def __init__(self, uri, dbName, collectionName,user,password):
        self.client = MongoClient(f'mongodb://{user}:{password}@{uri}')
        self.db = self.client[dbName]
        self.collection = self.db[collectionName]
            

    async def saveData(self, data):
        try:
            question = QuestionModel(**data)
            questionDict = question.model_dump()
            result = self.collection.insert_one(questionDict)
            logger.info(f"question {questionDict.get('id')} was saved")
            return result.inserted_id
        except Exception as e:
            logger.error(f"Error while saving data: {str(e)}")
            return None
       
    async def isQuestionExists(self, questionId):
        existing = self.collection.find_one({"questionId":questionId})
        if existing is not None:
            return True
        else:
            return False
