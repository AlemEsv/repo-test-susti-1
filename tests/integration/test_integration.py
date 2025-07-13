import requests
import pytest


def test_user_service_welcome():
    """servicio de usuarios responde correctamente"""
    response = requests.get("http://localhost:8001/welcome/test123")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "Hola Luis" in data["message"]


def test_order_service_ping():
    """servicio de pedidos está funcionando"""
    response = requests.get("http://localhost:8002/ping")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"


def test_order_service_action():
    """servicio de pedidos procesa correctamente"""
    response = requests.get("http://localhost:8002/action/test456")
    assert response.status_code == 200
    data = response.json()
    assert "order" in data
    assert "procesado" in data["order"]


def test_inventory_service_ping():
    """servicio de inventario está funcionando"""
    response = requests.get("http://localhost:8003/ping")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"


def test_inventory_service_inventory():
    """servicio de inventario consulta correctamente"""
    response = requests.get("http://localhost:8003/inventory/test789")
    assert response.status_code == 200
    data = response.json()
    assert "stock" in data
    assert "disponible" in data["stock"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
