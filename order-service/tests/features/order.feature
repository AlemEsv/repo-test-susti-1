Feature: Servicio de Pedidos
  Scenario: procesar un pedido
    Given el servicio esta en linea
    When hago un GET a /action/1
    Then el resultado debe incluir "procesado"