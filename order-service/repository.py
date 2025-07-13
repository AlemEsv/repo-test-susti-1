from interfaces import IRepository

class OrderRepository(IRepository):
    def get(self, item_id: str):
        return f"dato-{item_id}"