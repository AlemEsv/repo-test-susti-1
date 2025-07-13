provider "kubernetes" {
  config_path = "~/.kube/config"
}

# Namespace para la aplicación
resource "kubernetes_namespace" "app" {
  metadata {
    name = "pedidos"
  }
}

# Deployment del User Service
resource "kubernetes_deployment" "user_service" {
  metadata {
    name      = "user-deployment"
    namespace = kubernetes_namespace.app.metadata[0].name
  }

  spec {
    replicas = 1

    selector {
      match_labels = {
        app = "user"
      }
    }

    template {
      metadata {
        labels = {
          app = "user"
        }
      }

      spec {
        container {
          image = "user-service:latest"
          name  = "user"
          port {
            container_port = 8000
          }
        }
      }
    }
  }
}

# Service del User Service
resource "kubernetes_service" "user_service" {
  metadata {
    name      = "user-service"
    namespace = kubernetes_namespace.app.metadata[0].name
  }
  
  spec {
    selector = {
      app = "user"
    }
    
    port {
      port        = 80
      target_port = 8000
    }
    
    type = "ClusterIP"
  }
}