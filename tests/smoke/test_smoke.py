import requests
import pytest


class TestSmokeServices:
    """Tests de humo para verificar que todos los servicios responden"""

    def test_user_service_is_alive(self):
        """Verifica que el servicio de usuarios está respondiendo"""
        try:
            response = requests.get("http://localhost:8001/welcome/smoke-test", timeout=5)
            assert response.status_code == 200
        except requests.exceptions.RequestException:
            pytest.fail("User service no está respondiendo")

    def test_order_service_is_alive(self):
        """Verifica que el servicio de pedidos está respondiendo"""
        try:
            response = requests.get("http://localhost:8002/ping", timeout=5)
            assert response.status_code == 200
            assert response.json()["status"] == "ok"
        except requests.exceptions.RequestException:
            pytest.fail("Order service no está respondiendo")

    def test_inventory_service_is_alive(self):
        """Verifica que el servicio de inventario está respondiendo"""
        try:
            response = requests.get("http://localhost:8003/ping", timeout=5)
            assert response.status_code == 200
            assert response.json()["status"] == "ok"
        except requests.exceptions.RequestException:
            pytest.fail("Inventory service no está respondiendo")


class TestSmokeBasicFunctionality:
    """Tests de humo para funcionalidad básica"""

    def test_user_service_basic_response(self):
        """Verifica respuesta básica del servicio de usuarios"""
        response = requests.get("http://localhost:8001/welcome/test")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data

    def test_order_service_basic_response(self):
        """Verifica respuesta básica del servicio de pedidos"""
        response = requests.get("http://localhost:8002/action/test")
        assert response.status_code == 200
        data = response.json()
        assert "order" in data

    def test_inventory_service_basic_response(self):
        """Verifica respuesta básica del servicio de inventario"""
        response = requests.get("http://localhost:8003/inventory/test")
        assert response.status_code == 200
        data = response.json()
        assert "stock" in data


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
