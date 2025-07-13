import sys
import os
from unittest.mock import Mock
from service import OrderService
from interfaces import IRepository

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_process():
    repo = Mock(spec=IRepository)
    repo.get.return_value = "pedido-mock"
    service = OrderService(repo)
    result = service.process("123")
    assert result["order"] == "Pedido procesado: pedido-mock"
