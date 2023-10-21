from abc import ABC, abstractmethod

class IRepository(ABC):
    @abstractmethod
    async def saveData(self, data):
        pass
