import sys
import os
from unittest.mock import Mock
from service import InventoryService
from interfaces import IRepository

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_process():
    repo = Mock(spec=IRepository)
    repo.get.return_value = "stock-mock"
    service = InventoryService(repo)
    result = service.process("001")
    assert result["stock"] == "Stock disponible: stock-mock"
