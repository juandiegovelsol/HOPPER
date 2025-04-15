import csv
import json
from collections import defaultdict
from datetime import datetime

# Función para procesar el archivo CSV y generar el JSON con la estructura solicitada
def procesar_ventas_csv(archivo_csv):
    # Diccionarios para almacenar los resultados
    ventas_2023 = defaultdict(lambda: {
        "promedio_ventas_por_vendedor": defaultdict(int),
        "calificaciones_vendedores": defaultdict(float),
        "ventas_por_modelo": defaultdict(int)
    })
    ventas_2024 = defaultdict(lambda: {
        "promedio_ventas_por_vendedor": defaultdict(int),
        "calificaciones_vendedores": defaultdict(float),
        "ventas_por_modelo": defaultdict(int)
    })

    # Leer el archivo CSV
    with open(archivo_csv, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Validar que las columnas necesarias existan
            required_columns = ["vendedor", "marca", "modelo", "año", "precio", "satisfaccion", "comentarios", "promocion"]
            for column in required_columns:
                if column not in row:
                    print(f"Advertencia: La columna '{column}' está faltando en la fila: {row}")
                    continue

            # Convertir el año a entero y el precio a float
            try:
                año = int(row["año"])
                precio = float(row["precio"])
            except ValueError:
                print(f"Advertencia: Error al convertir el año o precio en la fila: {row}")
                continue

            # Verificar si el año es 2023 o 2024
            if año == 2023:
                ventas_2023[año]["promedio_ventas_por_vendedor"][row["vendedor"]] += precio
                ventas_2023[año]["calificaciones_vendedores"][row["vendedor"]] += float(row["satisfaccion"])
                ventas_2023[año]["ventas_por_modelo"][row["modelo"]] += 1
            elif año == 2024:
                ventas_2024[año]["promedio_ventas_por_vendedor"][row["vendedor"]] += precio
                ventas_2024[año]["calificaciones_vendedores"][row["vendedor"]] += float(row["satisfaccion"])
                ventas_2024[año]["ventas_por_modelo"][row["modelo"]] += 1
            else:
                print(f"Advertencia: Año desconocido '{año}' en la fila: {row}")

    # Calcular promedios y rankings
    for año in [2023, 2024]:
        for vendedor, ventas in ventas_2023[año]["promedio_ventas_por_vendedor"].items():
            ventas_2023[año]["promedio_ventas_por_vendedor"][vendedor] /= ventas

        for vendedor, calificaciones in ventas_2023[año]["calificaciones_vendedores"].items():
            ventas_2023[año]["calificaciones_vendedores"][vendedor] /= 10  # Normalizar calificaciones

        ranking_vendedores = sorted(ventas_2023[año]["calificaciones_vendedores"].items(), key=lambda x: x[1], reverse=True)
        ventas_2023[año]["ranking_vendedores"] = ranking_vendedores

    # Ordenar los modelos por número de ventas
    for año in [2023, 2024]:
        ventas_por_modelo_ordenadas = sorted(ventas_2023[año]["ventas_por_modelo"].items(), key=lambda x: x[1], reverse=True)
        ventas_2023[año]["ventas_por_modelo"] = {modelo: ventas for modelo, ventas in ventas_por_modelo_ordenadas}

    # Crear el diccionario final
    resultado = {
        "ventas_2023": ventas_2023,
        "ventas_2024": ventas_2024
    }

    # Escribir el JSON resultante en un archivo
    with open('resultado_ventas.json', mode='w', encoding='utf-8') as json_file:
        json.dump(resultado, json_file, indent=4, ensure_ascii=False)

    print("El archivo JSON ha sido generado correctamente.")

# Ejemplo de uso
archivo_csv = 'ventas.csv'
procesar_ventas_csv(archivo_csv)