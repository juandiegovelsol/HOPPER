import json
import csv
from collections import defaultdict

# Función para convertir la lista de listas en un diccionario con el nombre como clave
def transformar_datos(datos):
    inventario = defaultdict(dict)
    for pieza in datos:
        nombre = pieza[1]  # Nombre de la pieza está en la segunda posición
        inventario[nombre].update({
            "ID": pieza[0],              # ID en la primera posición
            "DESCRIPCION": pieza[2],    # Descripción en la tercera posición
            "CANTIDAD": pieza[3],       # Cantidad en la cuarta posición
            "PROVEEDOR": pieza[4],      # Proveedor en la quinta posición
            "FECHA INGRESO": pieza[5],  # Fecha de ingreso en la sexta posición
            "NUMERO LOTE": pieza[6]      # Número de lote en la séptima posición
        })
    return inventario

# Función para cargar datos desde un archivo CSV
def cargar_datos_csv(archivo_csv):
    with open(archivo_csv, mode='r', newline='', encoding='utf-8') as file:
        lector_csv = csv.reader(file)
        datos = list(lector_csv)  # Lee todo el archivo CSV en una lista de listas
    return datos[1:]  # Omite la fila de encabezados

# Función para guardar datos en un archivo JSON
def guardar_datos_json(datos, archivo_json):
    with open(archivo_json, mode='w', encoding='utf-8') as file:
        json.dump(datos, file, indent=4, ensure_ascii=False)

# Función principal para procesar los datos
def procesar_datos(archivo_csv, archivo_json):
    datos = cargar_datos_csv(archivo_csv)
    print(datos)
    inventario = transformar_datos(datos)
    
    guardar_datos_json(inventario, archivo_json)
    print(f"Datos procesados y guardados en {archivo_json}")

# Ejemplo de uso
archivo_csv = 'piezas_automotrices.csv'
archivo_json = 'inventario_piezas.json'
procesar_datos(archivo_csv, archivo_json)