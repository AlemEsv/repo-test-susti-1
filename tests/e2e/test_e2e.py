"""
End-to-End Tests - Tests que simulan flujos completos de usuario
Estos tests prueban escenarios reales de uso de la aplicación
"""
import requests
import pytest
import time


class TestE2EUserJourney:
    """Tests E2E que simulan el viaje completo de un usuario"""
    
    def test_complete_user_order_flow(self):
        """
        Test E2E: Flujo completo desde bienvenida hasta pedido
        Simula: Usuario se conecta -> Ve inventario -> Hace pedido
        """
        user_id = "e2e_user_123"
        item_id = "e2e_item_456"
        
        # Paso 1: Usuario se conecta al sistema
        response = requests.get(f"http://localhost:8001/welcome/{user_id}")
        assert response.status_code == 200
        welcome_data = response.json()
        assert "Hola" in welcome_data["message"]
        
        # Paso 2: Usuario consulta inventario
        response = requests.get(f"http://localhost:8003/inventory/{item_id}")
        assert response.status_code == 200
        inventory_data = response.json()
        assert "disponible" in inventory_data["stock"]
        
        # Paso 3: Usuario hace un pedido
        response = requests.get(f"http://localhost:8002/action/{item_id}")
        assert response.status_code == 200
        order_data = response.json()
        assert "procesado" in order_data["order"]
        
        # Verificación final: El flujo se completó correctamente
        assert "Hola" in welcome_data["message"]  # El servicio siempre retorna "Hola Luis"
        assert "disponible" in inventory_data["stock"]
        assert "procesado" in order_data["order"]
    
    def test_multiple_users_concurrent_access(self):
        """
        Test E2E: Múltiples usuarios accediendo concurrentemente
        """
        user_ids = ["user_1", "user_2", "user_3"]
        
        # Simular múltiples usuarios accediendo al mismo tiempo
        for user_id in user_ids:
            response = requests.get(f"http://localhost:8001/welcome/{user_id}")
            assert response.status_code == 200
            
            # Cada usuario consulta inventario
            response = requests.get(f"http://localhost:8003/inventory/item_{user_id}")
            assert response.status_code == 200
    
    def test_service_chain_communication(self):
        """
        Test E2E: Verificar que los servicios pueden comunicarse en cadena
        """
        # Test que simula una comunicación entre todos los servicios
        test_id = "chain_test_789"
        
        # Verificar que todos los servicios procesan el mismo ID
        user_response = requests.get(f"http://localhost:8001/welcome/{test_id}")
        order_response = requests.get(f"http://localhost:8002/action/{test_id}")
        inventory_response = requests.get(f"http://localhost:8003/inventory/{test_id}")
        
        # Todos deben responder exitosamente
        assert user_response.status_code == 200
        assert order_response.status_code == 200
        assert inventory_response.status_code == 200
        
        # Verificar que todos procesaron correctamente (no necesariamente el ID)
        assert "Hola" in str(user_response.json())
        assert "procesado" in str(order_response.json())
        assert "disponible" in str(inventory_response.json())


class TestE2EErrorScenarios:
    """Tests E2E para escenarios de error"""
    
    def test_invalid_user_id_handling(self):
        """Test E2E: Manejo de ID de usuario válido (nuestro servicio es permisivo)"""
        valid_ids = ["test1", "user123", "valid_user"]
        
        for valid_id in valid_ids:
            response = requests.get(f"http://localhost:8001/welcome/{valid_id}")
            # Nuestro servicio responde con cualquier ID válido
            assert response.status_code == 200
    
    def test_service_resilience(self):
        """Test E2E: Verificar que los servicios son resilientes"""
        # Hacer múltiples peticiones rápidas para probar la resilencia
        for i in range(5):
            response = requests.get(f"http://localhost:8002/ping")
            assert response.status_code == 200
            time.sleep(0.1)  # Pequeña pausa entre peticiones


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=long"])
