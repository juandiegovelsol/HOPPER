from pulp import LpMaximize, LpProblem, LpVariable, lpSum, value

# Crear un problema de maximización
problema = LpProblem("Maximizar_Ingresos", LpMaximize)

# Variables de decisión: número de cajas a producir para cada producto
x1 = LpVariable('Producto_1', lowBound=0, cat='Integer')  # No pueden ser negativas y deben ser enteras
x2 = LpVariable('Producto_2', lowBound=0, cat='Integer')
x3 = LpVariable('Producto_3', lowBound=0, cat='Integer')
x4 = LpVariable('Producto_4', lowBound=0, cat='Integer')

# Función objetivo: maximizar ingresos
problema += 26 * x1 + 40 * x2 + 38 * x3 + 52 * x4, "Total_Ingresos"

# Restricciones de ingredientes
problema += x1 * 0.5 + x2 * 0.5 <= 550, "Limitacion_Cacahuetes"
problema += x2 * 0.5 + x4 * 0.3 <= 90, "Limitacion_Almendras"
problema += x3 * 0.5 + x2 * 0.15 + x4 * 0.3 <= 150, "Limitacion_Pistachos"
problema += x4 * 0.3 <= 70, "Limitacion_Avellanas"

# Restricciones de composición del producto 2
problema += x2 * 0.5 >= x2 * 0.1, "Minimo_Almendras_Producto_2"
problema += x2 * 0.5 >= x2 * 0.15, "Minimo_Pistachos_Producto_2"
problema += x2 * 0.5 <= x2 * 0.5, "Maximo_Cacahuetes_Producto_2"

# Restricciones de composición del producto 4
problema += x4 * 0.5 >= x4 * 0.3, "Minimo_Almendras_Producto_4"
problema += x4 * 0.5 >= x4 * 0.3, "Minimo_Pistachos_Producto_4"
problema += x4 * 0.5 >= x4 * 0.3, "Minimo_Avellanas_Producto_4"

# Resolver el problema
problema.solve()

# Resultados
print(f"Estado de la solución: {problema.status}")
print(f"Ingresos totales: {value(problema.objective)}")
print(f"Producto_1: {x1.varValue} cajas")
print(f"Producto_2: {x2.varValue} cajas")
print(f"Producto_3: {x3.varValue} cajas")
print(f"Producto_4: {x4.varValue} cajas")