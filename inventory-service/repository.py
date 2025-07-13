from interfaces import IRepository


class InventoryRepository(IRepository):
    def get(self, item_id: str):
        return f"dato-{item_id}"
