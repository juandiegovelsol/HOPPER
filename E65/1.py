import csv
import json
from collections import defaultdict
from datetime import datetime

def validar_datos_venta(venta):
    """
    Valida que los datos de una venta sean completos y consistentes.
    """
    try:
        # Verificar que todos los campos requeridos estén presentes
        assert 'vendedor' in venta and 'marca' in venta and 'modelo' in venta and 'año' in venta and 'precio' in venta
        
        # Convertir campos a tipos apropiados
        vendedor = venta['vendedor']
        marca = venta['marca']
        modelo = venta['modelo']
        año = int(venta['año'])
        precio = float(venta['precio'])
        satisfaccion = int(venta['satisfaccion'])
        
        # Validar rangos de datos
        assert 1 <= año <= 2023  # Año de la venta
        
        assert 1 <= satisfaccion <= 5  # Calificación del cliente
        print("E")
        assert precio > 0  # Precio de la venta
        
        return {
            'vendedor': vendedor,
            'marca': marca,
            'modelo': modelo,
            'año': año,
            'precio': precio,
            'satisfaccion': satisfaccion
        }
    except (AssertionError, ValueError) as e:
        print(f"Error en los datos de la venta: {venta}. Detalles: {e}")
        return None

def procesar_ventas_csv(archivo_csv):
    """
    Procesa un archivo CSV de ventas de autos y genera un diccionario estructurado.
    """
    ventas_por_ano = defaultdict(lambda: {
        'promedio_ventas_por_vendedor': defaultdict(float),
        'calificaciones_vendedores': defaultdict(float),
        'ventas_por_modelo': defaultdict(int)
    })
    
    try:
        with open(archivo_csv, mode='r', encoding='utf-8') as file:
            lector_csv = csv.DictReader(file)
            
            for fila in lector_csv:
                venta = validar_datos_venta(fila)
                if venta:
                    # Extraer año de la venta
                    año_venta = int(fila['anio_venta'])
                    
                    # Actualizar datos por año
                    ventas_por_ano[año_venta]['ventas_por_modelo'][venta['modelo']] += 1
                    ventas_por_ano[año_venta]['promedio_ventas_por_vendedor'][venta['vendedor']] += venta['precio']
                    ventas_por_ano[año_venta]['calificaciones_vendedores'][venta['vendedor']] += venta['satisfaccion']
    
    except FileNotFoundError:
        print(f"Error: El archivo {archivo_csv} no se encontró.")
    except Exception as e:
        print(f"Error inesperado al procesar el archivo CSV: {e}")
    
    return ventas_por_ano

def generar_json_resumen(ventas_por_ano):
    """
    Genera un JSON con el resumen de ventas procesadas.
    """
    resumen_json = {}
    
    for año, datos in ventas_por_ano.items():
        resumen_json[f"ventas_{año}"] = {
            'promedio_ventas_por_vendedor': dict(
                (vendedor, round(total / len(ventas), 2))
                for vendedor, total in datos['promedio_ventas_por_vendedor'].items()
            ),
            'calificaciones_vendedores': dict(
                (vendedor, round(sum(calificaciones) / len(calificaciones), 2))
                for vendedor, calificaciones in datos['calificaciones_vendedores'].items()
            ),
            'ventas_por_modelo': dict(ventas_por_modelo for ventas_por_modelo in datos['ventas_por_modelo'].values())
        }
    
    return resumen_json

def main():
    # Ruta al archivo CSV de ventas
    archivo_csv = 'ventas_autos.csv'
    
    # Procesar los datos de ventas
    ventas_por_ano = procesar_ventas_csv(archivo_csv)
    
    # Generar el resumen en formato JSON
    resumen_json = generar_json_resumen(ventas_por_ano)
    
    # Guardar el JSON en un archivo
    try:
        with open('resumen_ventas.json', mode='w', encoding='utf-8') as file:
            json.dump(resumen_json, file, ensure_ascii=False, indent=4)
        print("Resumen de ventas generado y guardado en 'resumen_ventas.json'.")
    except Exception as e:
        print(f"Error al guardar el archivo JSON: {e}")

if __name__ == "__main__":
    main()