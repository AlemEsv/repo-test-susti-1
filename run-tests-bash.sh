#!/bin/bash

# Script simple para ejecutar tests - funciona en Windows con Git Bash

echo "Test Runner Bash - Microservicios"
echo "===================================="
echo ""

TEST_TYPE=$1

if [ -z "$TEST_TYPE" ]; then
    echo "Uso: bash run-tests.sh [tipo]"
    echo ""
    echo "Tipos disponibles:"
    echo "  smoke       - Tests rápidos de verificación"
    echo "  integration - Tests de integración"  
    echo "  e2e         - Tests end-to-end"
    echo "  unit        - Tests unitarios"
    echo ""
    exit 1
fi

# Detectar comando de Python disponible
PYTHON_CMD="python"
if command -v python.exe >/dev/null 2>&1; then
    PYTHON_CMD="python.exe"
elif command -v python3 >/dev/null 2>&1; then
    PYTHON_CMD="python3"
elif command -v python >/dev/null 2>&1; then
    PYTHON_CMD="python"
else
    echo "Python no encontrado"
    exit 1
fi

case $TEST_TYPE in
    "smoke")
        echo "Ejecutando Smoke Tests..."
        $PYTHON_CMD -m pytest tests/smoke/ -v --tb=short
        ;;
    "integration")
        echo "Ejecutando Integration Tests..."
        $PYTHON_CMD -m pytest tests/integration/ -v
        ;;
    "e2e")
        echo "Ejecutando E2E Tests..."
        $PYTHON_CMD -m pytest tests/e2e/ -v --tb=long
        ;;
    "unit")
        echo "Ejecutando Unit Tests..."
        echo ""
        echo "User Service..."
        docker exec proyecto1-user-1 python -m pytest tests/test_user_unit.py -v
        echo ""
        echo "Order Service..."
        docker exec proyecto1-order-1 python -m pytest tests/test_service_unit.py -v
        echo ""
        echo "Inventory Service..."
        docker exec proyecto1-inventory-1 python -m pytest tests/test_inventory_unit.py -v
        ;;
    *)
        echo "Tipo de test no válido: $TEST_TYPE"
        echo "Usa: smoke, integration, e2e, o unit"
        exit 1
        ;;
esac

echo ""
echo "Tests completados!"
