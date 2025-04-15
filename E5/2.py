import csv
import json
from collections import defaultdict
from statistics import mean

# Función para procesar el archivo CSV y generar el JSON solicitado
def procesar_ventas_csv_a_json(archivo_csv, archivo_json):
    ventas_por_anio = defaultdict(lambda: {
        "ventas_totales": 0,
        "ventas_por_vendedor": defaultdict(int),
        "calificaciones": [],
        "ventas_por_modelo": defaultdict(int)
    })

    try:
        # Abrir y leer el archivo CSV
        with open(archivo_csv, mode='r', encoding='utf-8') as file:
            lector_csv = csv.DictReader(file)
            
            for fila in lector_csv:
                try:
                    anio = fila['anio_venta']
                    vendedor = fila['vendedor']
                    marca = fila['marca']
                    modelo = fila['modelo']
                    precio = float(fila['precio'])
                    satisfaccion = int(fila['satisfaccion'])
                    
                    # Acumular datos para el año correspondiente
                    ventas_por_anio[anio]["ventas_totales"] += precio
                    ventas_por_anio[anio]["ventas_por_vendedor"][vendedor] += precio
                    ventas_por_anio[anio]["calificaciones"].append(satisfaccion)
                    ventas_por_anio[anio]["ventas_por_modelo"][f"{marca} {modelo}"] += 1

                except ValueError as e:
                    print(f"Error al procesar la fila {fila}: {e}")

        # Procesar los datos acumulados para generar el JSON final
        resultado = {}
        for anio, datos in ventas_por_anio.items():
            promedio_ventas_por_vendedor = {
                vendedor: round(ventas, 2)
                for vendedor, ventas in datos["ventas_por_vendedor"].items()
            }
            
            calificaciones_vendedores = {
                vendedor: round(mean(calificaciones), 1)
                for vendedor, calificaciones in zip(datos["ventas_por_vendedor"].keys(), [datos["calificaciones"]] * len(datos["ventas_por_vendedor"]))
            }
            
            resultado[anio] = {
                "promedio_ventas_por_vendedor": promedio_ventas_por_vendedor,
                "calificaciones_vendedores": calificaciones_vendedores,
                "ventas_por_modelo": dict(datos["ventas_por_modelo"])
            }

        # Guardar el resultado en un archivo JSON
        with open(archivo_json, mode='w', encoding='utf-8') as file:
            json.dump(resultado, file, indent=4, ensure_ascii=False)
        
        print(f"Procesamiento completado. Datos guardados en {archivo_json}")

    except FileNotFoundError:
        print(f"Error: El archivo {archivo_csv} no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Ejemplo de uso
archivo_csv = 'ventas_autos.csv'
archivo_json = 'ventas_autos_procesadas.json'
procesar_ventas_csv_a_json(archivo_csv, archivo_json)