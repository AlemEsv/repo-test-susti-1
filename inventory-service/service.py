from interfaces import IRepository

class InventoryService:
    def __init__(self, repo: IRepository):
        self.repo = repo

    def process(self, item_id: str):
        stock = self.repo.get(item_id)
        return {"stock": f"Stock disponible: {stock}"}