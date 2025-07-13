output "namespace_name" {
  description = "Nombre del namespace creado"
  value       = kubernetes_namespace.app.metadata[0].name
}
