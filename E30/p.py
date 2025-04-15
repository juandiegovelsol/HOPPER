import pandas as pd

# Datos simulados
datos = {
    'producto': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    'total': [1000, 800, 1200, 400, 1500, 600, 300, 700]
}

# Crear DataFrame
ventas_totales = pd.DataFrame(datos)

# Ordenar por ventas totales de mayor a menor
ventas_totales = ventas_totales.sort_values(by='total', ascending=False)

# Seleccionar el 75% superior de los productos (quintil superior)
quintil_superior = ventas_totales.iloc[:int(len(ventas_totales) * 0.25)]

# Mostrar resultados
print("Ventas totales ordenadas:")
print(ventas_totales)
print("\nQuintil superior (75% con más ventas):")
print(quintil_superior)
