#!/bin/bash

echo "Ejecutando Tests Unitarios de los Microservicios"
echo "=================================================="
echo ""

echo "Ejecutando tests unitarios del User Service..."
docker exec proyecto1-user-1 python -m pytest tests/test_user_unit.py -v

echo ""
echo "Ejecutando tests unitarios del Order Service..."
docker exec proyecto1-order-1 python -m pytest tests/test_service_unit.py -v

echo ""
echo "Ejecutando tests unitarios del Inventory Service..."
docker exec proyecto1-inventory-1 python -m pytest tests/test_inventory_unit.py -v

echo ""
echo "Tests unitarios completados!"
