import csv
import json
from collections import defaultdict
from datetime import datetime

# Función para leer el archivo CSV y convertirlo a un diccionario de ventas
def leer_ventas_csv(archivo_csv):
    ventas = defaultdict(lambda: {
        '2023': {'ventas': defaultdict(float), 'calificaciones': defaultdict(float)},
        '2024': {'ventas': defaultdict(float), 'calificaciones': defaultdict(float)}
    })

    with open(archivo_csv, mode='r', encoding='utf-8') as file:
        lector_csv = csv.DictReader(file)
        for fila in lector_csv:
            año = int(fila['anio_venta'])
            vendedor = fila['vendedor']
            marca = fila['marca']
            modelo = fila['modelo']
            precio = float(fila['precio'])
            satisfaccion = float(fila['satisfaccion'])
            comentarios = fila['comentarios']
            promocion = fila['promocion']

            # Actualizar ventas por año y vendedor
            ventas[año]['ventas'][vendedor] += precio
            ventas[año]['calificaciones'][vendedor] += satisfaccion

            # Actualizar ventas por modelo
            ventas[año]['ventas'][marca][vendedor] += precio

    return ventas

# Función para calcular promedios y rankings de calificaciones
def procesar_ventas(ventas):
    ventas_2023 = ventas['2023']
    ventas_2024 = ventas['2024']

    promedio_ventas_por_vendedor = {}
    calificaciones_vendedores = {}
    ventas_por_modelo = defaultdict(int)

    for año, datos in ventas_2023.items():
        for vendedor, total_venta in datos['ventas'].items():
            promedio_ventas_por_vendedor[vendedor] = round(total_venta / 1, 2)

        for vendedor, total_calificacion in datos['calificaciones'].items():
            calificaciones_vendedores[vendedor] = round(total_calificacion / len(datos['ventas']), 2)

        for marca, ventas_vendedor in datos['ventas'].items():
            for vendedor, precio_venta in ventas_vendedor.items():
                ventas_por_modelo[marca] += precio_venta

    return {
        "ventas_2023": {
            "promedio_ventas_por_vendedor": promedio_ventas_por_vendedor,
            "calificaciones_vendedores": calificaciones_vendedores,
            "ventas_por_modelo": ventas_por_modelo
        },
        "ventas_2024": {
            "promedio_ventas_por_vendedor": {},
            "calificaciones_vendedores": {},
            "ventas_por_modelo": defaultdict(int)
        }
    }

# Función para convertir el diccionario de ventas a formato JSON
def convertir_a_json(ventas_procesadas, archivo_json):
    with open(archivo_json, mode='w', encoding='utf-8') as file:
        json.dump(ventas_procesadas, file, ensure_ascii=False, indent=4)

# Función principal para ejecutar el procesamiento
def main():
    archivo_csv = 'ventas_autos.csv'
    archivo_json = 'ventas_procesadas.json'

    ventas = leer_ventas_csv(archivo_csv)
    ventas_procesadas = procesar_ventas(ventas)
    convertir_a_json(ventas_procesadas, archivo_json)

    print(f"Procesamiento completado. Archivo JSON guardado como '{archivo_json}'.")

if __name__ == "__main__":
    main()