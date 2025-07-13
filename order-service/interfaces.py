from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    def get(self, item_id: str):
        pass
