#!/bin/bash

# Script simple para ver logs
# Uso: ./logs.sh [user|order|inventory|all|pods]

SERVICE=$1

if [ -z "$SERVICE" ]; then
    echo "Ver logs del proyecto"
    echo "Uso: ./logs.sh [servicio]"
    echo ""
    echo "Servicios:"
    echo "  user       - Logs de user-service"
    echo "  order      - Logs de order-service"
    echo "  inventory  - Logs de inventory-service"
    echo "  all        - Logs de todos los servicios"
    echo "  pods       - Estado de todos los pods"
    exit 0
fi

# Verificar conexión a Kubernetes
if ! kubectl cluster-info >/dev/null 2>&1; then
    echo "No hay conexión a Kubernetes"
    echo "Ejecuta: minikube start"
    exit 1
fi

case $SERVICE in
    user)
        echo "Logs de user-service:"
        kubectl logs deployment/user-deployment --tail=50
        ;;
    order)
        echo "Logs de order-service:"
        kubectl logs deployment/order-deployment --tail=50
        ;;
    inventory)
        echo "Logs de inventory-service:"
        kubectl logs deployment/inventory-deployment --tail=50
        ;;
    all)
        echo "Logs de todos los servicios:"
        echo "=== USER SERVICE ==="
        kubectl logs deployment/user-deployment --tail=20 2>/dev/null || echo "No disponible"
        echo ""
        echo "=== ORDER SERVICE ==="
        kubectl logs deployment/order-deployment --tail=20 2>/dev/null || echo "No disponible"
        echo ""
        echo "=== INVENTORY SERVICE ==="
        kubectl logs deployment/inventory-deployment --tail=20 2>/dev/null || echo "No disponible"
        ;;
    pods)
        echo "Estado de pods:"
        kubectl get pods -o wide
        echo ""
        echo "Servicios:"
        kubectl get services
        echo ""
        echo "Ingress:"
        kubectl get ingress
        ;;
    *)
        echo "Servicios válidos: user, order, inventory, all, pods"
        exit 1
        ;;
esac
