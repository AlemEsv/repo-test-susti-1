from interfaces import IRepository


class OrderService:
    def __init__(self, repo: IRepository):
        self.repo = repo

    def process(self, order_id: str):
        order = self.repo.get(order_id)
        return {"order": f"Pedido procesado: {order}"}
