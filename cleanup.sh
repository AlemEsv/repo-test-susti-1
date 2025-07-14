#!/bin/bash

# 1. Limpiar Kubernetes
kubectl delete -f kubernetes/ --ignore-not-found=true 2>/dev/null || echo "  No hay recursos"

# 2. Limpiar imágenes Docker del proyecto
docker rmi user-service:latest order-service:latest inventory-service:latest 2>/dev/null || echo "  No hay imágenes del proyecto"

# 3. Limpiar cache Docker
docker system prune -af --volumes 2>/dev/null || echo "  Error limpiando Docker"

# 4. Limpiar archivos temporales
find . -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find . -name "*.pyc" -delete 2>/dev/null || true
find . -name "*.log" -delete 2>/dev/null || true

# 5. Detener Minikube
echo "Detener Minikube"
minikube stop 2>/dev/null || echo "Minikube no está corriendo"

echo "Limpieza completada"
