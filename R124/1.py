import pulp

# Crear un problema de maximización
problema = pulp.LpProblem("Maximizar_Ingresos", pulp.LpMaximize)

# Variables de decisión: cantidad de cada producto a producir (en cajas)
x1 = pulp.LpVariable('Producto_1', lowBound=0, cat='Continuous')
x2 = pulp.LpVariable('Producto_2', lowBound=0, cat='Continuous')
x3 = pulp.LpVariable('Producto_3', lowBound=0, cat='Continuous')
x4 = pulp.LpVariable('Producto_4', lowBound=0, cat='Continuous')

# Función objetivo: maximizar ingresos
problema += 26 * x1 + 40 * x2 + 38 * x3 + 52 * x4, "Ingresos Totales"

# Restricciones de ingredientes para cada producto
problema += x1 * 0.5 <= 550, "Cacahuetes para Producto_1"
problema += x2 * 0.5 <= 550, "Cacahuetes para Producto_2"
problema += x2 * 0.05 >= 0, "Almendras mínimas para Producto_2"
problema += x2 * 0.075 >= 0, "Pistachos mínimos para Producto_2"

problema += x3 * 0.5 <= 150, "Pistachos para Producto_3"

problema += x4 * 0.15 >= 0, "Almendras mínimas para Producto_4"
problema += x4 * 0.15 >= 0, "Pistachos mínimos para Producto_4"
problema += x4 * 0.15 >= 0, "Avellanas mínimas para Producto_4"

# Restricciones de existencias totales
problema += 0.5 * x1 + 0.5 * x2 <= 550, "Total Cacahuetes"
problema += 0.1 * x2 + 0.3 * x4 <= 90, "Total Almendras"
problema += 0.15 * x2 + 0.5 * x3 + 0.3 * x4 <= 150, "Total Pistachos"
problema += 0.3 * x4 <= 70, "Total Avellanas"

# Solucionar el problema
problema.solve()

# Imprimir resultados
print(f"Estado: {pulp.LpStatus[problema.status]}")
print(f"Produce {x1.varValue} cajas de Producto_1")
print(f"Produce {x2.varValue} cajas de Producto_2")
print(f"Produce {x3.varValue} cajas de Producto_3")
print(f"Produce {x4.varValue} cajas de Producto_4")
print(f"Ingresos Totales: {pulp.value(problema.objective)} euros")