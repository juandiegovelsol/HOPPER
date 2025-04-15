import csv
import json
from collections import defaultdict

# Función para leer el archivo CSV y calcular la asignación de recursos
def leer_csv_y_asignar_recursos(archivo_csv):
    # Diccionario para almacenar la asignación de recursos por región y proyecto
    asignacion_recursos = defaultdict(lambda: defaultdict(lambda: {"issue_severity": "", "necesidad_recurso": 0}))

    try:
        # Abrir y leer el archivo CSV
        with open(archivo_csv, mode='r') as file:
            lector_csv = csv.DictReader(file)

            for fila in lector_csv:
                region = fila["region"]
                proyecto = fila["proyecto"]
                severidad = fila["problema_severidad"]
                recursos = int(fila["necesidad_recursos"])

                print(region, proyecto, recursos)

                # Actualizar la severidad y los recursos para el proyecto en la región
                asignacion_recursos[region][proyecto]["issue_severity"] = severidad
                asignacion_recursos[region][proyecto]["necesidad_recurso"] += recursos

        # Calcular la necesidad total de recursos por región
        resultado = {}
        for region, proyectos in asignacion_recursos.items():
            total_recursos = sum(proyectos.values()["necesidad_recurso"])
            resultado[region] = {
                "proyectos": proyectos,
                "necesidad_de_recursos_totales": total_recursos
            }

        return resultado

    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_csv}' no se encontró.")
    except Exception as e:
        print(f"Error inesperado al leer el archivo CSV: {e}")

# Función para escribir los resultados en un archivo JSON
def escribir_json(resultado, archivo_json):
    try:
        # Abrir y escribir los resultados en el archivo JSON
        with open(archivo_json, mode='w') as file:
            json.dump(resultado, file, indent=4, ensure_ascii=False)

        print(f"Resultados guardados en '{archivo_json}'")

    except Exception as e:
        print(f"Error inesperado al escribir el archivo JSON: {e}")

# Ejemplo de uso
archivo_csv = 'datos_recursos.csv'
archivo_json = 'asignacion_recursos.json'

# Leer el archivo CSV y asignar recursos
resultado = leer_csv_y_asignar_recursos(archivo_csv)

# Escribir los resultados en un archivo JSON
escribir_json(resultado, archivo_json)