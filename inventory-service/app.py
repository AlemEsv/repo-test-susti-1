from fastapi import FastAPI, Depends
from service import InventoryService
from repository import InventoryRepository

app = FastAPI()

def get_inventory_service():
    repo = InventoryRepository()
    return InventoryService(repo)

@app.get("/ping")
def ping():
    return {"status": "ok"}

@app.get("/inventory/{item_id}")
def handle(item_id: str, service: InventoryService = Depends(get_inventory_service)):
    return service.process(item_id)