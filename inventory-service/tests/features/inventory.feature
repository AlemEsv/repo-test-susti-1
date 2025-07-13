Feature: Servicio de Inventario
  Scenario: consultar inventario
    Given el servicio esta en linea
    When hago un GET a /action/1
    Then el resultado debe incluir "disponible"