import csv
import json
from collections import defaultdict
from datetime import datetime

# Función para leer el archivo CSV y convertirlo a un diccionario
def leer_csv(archivo_csv):
    ventas_por_año = defaultdict(lambda: {
        "ventas_por_vendedor": defaultdict(int),
        "calificaciones_vendedores": defaultdict(float),
        "ventas_por_modelo": defaultdict(int)
    })

    with open(archivo_csv, mode='r', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            try:
                año_venta = int(fila['anio_venta'])
                vendedor = fila['vendedor']
                marca = fila['marca']
                modelo = fila['modelo']
                precio = int(fila['precio'])
                satisfaccion = float(fila['satisfaccion'])
                promocion = fila['promocion']

                ventas_por_año[año_venta]["ventas_por_vendedor"][vendedor] += precio
                ventas_por_año[año_venta]["calificaciones_vendedores"][vendedor] += satisfaccion
                ventas_por_año[año_venta]["ventas_por_modelo"][modelo] += 1

            except ValueError as e:
                print(f"Error al procesar la fila {fila}: {e}")

    return ventas_por_año

# Función para calcular promedios y rankings
def calcular_promedios_y_rankings(ventas_por_año):
    resultados = {}

    for año, datos in ventas_por_año.items():
        promedio_ventas_por_vendedor = {}
        calificaciones_vendedores = {}
        ventas_por_modelo = {}

        for vendedor, total_precio in datos["ventas_por_vendedor"].items():
            promedio_ventas_por_vendedor[vendedor] = total_precio / len(datos["ventas_por_vendedor"])
            calificaciones_vendedores[vendedor] = sum(datos["calificaciones_vendedores"].values()) / len(datos["calificaciones_vendedores"])

        for modelo, cantidad_ventas in datos["ventas_por_modelo"].items():
            ventas_por_modelo[modelo] = cantidad_ventas

        resultados[año] = {
            "promedio_ventas_por_vendedor": promedio_ventas_por_vendedor,
            "calificaciones_vendedores": calificaciones_vendedores,
            "ventas_por_modelo": ventas_por_modelo
        }

    # Calcular ranking de vendedores
    ranking_vendedores = sorted(
        resultados[2023]["calificaciones_vendedores"].items(),
        key=lambda x: x[1],
        reverse=True
    )
    ranking_vendedores_2024 = sorted(
        resultados[2024]["calificaciones_vendedores"].items(),
        key=lambda x: x[1],
        reverse=True
    )

    resultados["ranking_vendedores_2023"] = ranking_vendedores
    resultados["ranking_vendedores_2024"] = ranking_vendedores_2024

    return resultados

# Función para convertir el diccionario a JSON
def convertir_a_json(resultados, archivo_json):
    try:
        with open(archivo_json, mode='w', encoding='utf-8') as archivo:
            json.dump(resultados, archivo, ensure_ascii=False, indent=4)
        print(f"Archivo JSON generado exitosamente: {archivo_json}")
    except IOError as e:
        print(f"Error al escribir el archivo JSON: {e}")

# Función principal para ejecutar el proceso
def procesar_ventas(archivo_csv, archivo_json):
    ventas_por_año = leer_csv(archivo_csv)
    resultados = calcular_promedios_y_rankings(ventas_por_año)
    convertir_a_json(resultados, archivo_json)

# Ejemplo de uso
archivo_csv = 'ventas_autos.csv'
archivo_json = 'ventas_autos.json'

procesar_ventas(archivo_csv, archivo_json)