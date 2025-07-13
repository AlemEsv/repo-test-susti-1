from fastapi import FastAPI, Depends
from service import OrderService
from repository import OrderRepository

app = FastAPI()


def get_order_service():
    repo = OrderRepository()
    return OrderService(repo)


@app.get("/ping")
def ping():
    return {"status": "ok"}


@app.get("/action/{item_id}")
def handle(item_id: str, service: OrderService = Depends(get_order_service)):
    return service.process(item_id)
