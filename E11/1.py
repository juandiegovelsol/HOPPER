import json
import csv
from datetime import datetime

# Función para validar y transformar los datos
def transformar_datos(datos):
    # Verificar que los datos sean una lista
    if not isinstance(datos, list):
        raise ValueError("Los datos deben ser una lista.")
    
    # Verificar que cada elemento sea una lista de exactamente 6 elementos
    for item in datos:
        if not isinstance(item, list) or len(item) != 6:
            raise ValueError("Cada elemento de la lista debe ser una lista de exactamente 6 elementos.")
    
    # Crear el diccionario final
    resultado = {}
    for item in datos:
        id_pieza, nombre, descripcion, cantidad, proveedor, fecha_ingreso = item
        
        # Validar tipos de datos
        if not isinstance(id_pieza, str) or not id_pieza:
            raise ValueError(f"El ID '{id_pieza}' es inválido o está vacío.")
        if not isinstance(nombre, str) or not nombre:
            raise ValueError(f"El nombre '{nombre}' es inválido o está vacío.")
        if not isinstance(descripcion, str) or not descripcion:
            raise ValueError(f"La descripción '{descripcion}' es inválida o está vacía.")
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError(f"La cantidad '{cantidad}' es inválida.")
        if not isinstance(proveedor, str) or not proveedor:
            raise ValueError(f"El proveedor '{proveedor}' es inválido o está vacío.")
        
        # Validar fecha de ingreso
        try:
            datetime.strptime(fecha_ingreso, "%d/%m/%Y")
        except ValueError:
            raise ValueError(f"La fecha de ingreso '{fecha_ingreso}' tiene un formato inválido. Debe ser DD/MM/YYYY.")
        
        # Crear el objeto para cada pieza
        pieza = {
            "ID": id_pieza,
            "DESCRIPCION": descripcion,
            "CANTIDAD": cantidad,
            "PROVEEDOR": proveedor,
            "FECHA INGRESO": fecha_ingreso,
            "NUMERO LOTE": "l123"  # Asumiendo que el número de lote es siempre 'l123' según el ejemplo
        }
        
        # Usar el nombre como clave, convirtiéndolo a mayúsculas y reemplazando espacios por guiones bajos
        clave_validada = nombre.upper().replace(" ", "_")
        resultado[clave_validada] = pieza
    
    return resultado

# Función para cargar datos desde un archivo CSV
def cargar_datos_desde_csv(archivo_csv):
    try:
        with open(archivo_csv, mode='r', encoding='utf-8') as archivo:
            lector_csv = csv.reader(archivo)
            # Saltarse la fila de encabezados
            next(lector_csv, None)
            datos = [fila for fila in lector_csv]
        return datos
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_csv}' no fue encontrado.")
        return []
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
        return []

# Función para guardar los datos en un archivo JSON
def guardar_datos_en_json(datos, archivo_json):
    try:
        with open(archivo_json, mode='w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        print(f"Datos guardados exitosamente en '{archivo_json}'.")
    except Exception as e:
        print(f"Error al guardar los datos en JSON: {e}")

# Función principal para procesar los datos
def procesar_datos_y_guardar(archivo_csv, archivo_json):
    datos = cargar_datos_desde_csv(archivo_csv)
    if datos:
        try:
            datos_transformados = transformar_datos(datos)
            guardar_datos_en_json(datos_transformados, archivo_json)
        except ValueError as ve:
            print(f"Error de validación de datos: {ve}")

# Ejemplo de uso: especifica las rutas de tus archivos CSV y JSON
archivo_csv = 'datos_piezas.csv'  # Ruta al archivo CSV de entrada
archivo_json = 'piezas_transformadas.json'  # Ruta al archivo JSON de salida

procesar_datos_y_guardar(archivo_csv, archivo_json)