import csv
import json
from collections import defaultdict
from typing import Dict, List, Tuple

# Función para validar los datos de cada fila del CSV
def validar_fila(fila: List[str]) -> bool:
    try:
        # Verificar que todos los campos requeridos estén presentes y no estén vacíos
        assert len(fila) == 9
        vendedor, marca, modelo, año, precio, satisfaccion, comentarios, promocion, anio_venta = fila
        
        # Validar que el año sea un número entero
        año = int(año)
        anio_venta = int(anio_venta)
        
        # Validar que el precio sea un número entero o flotante
        precio = float(precio)
        
        # Validar que la satisfacción sea un número entero entre 1 y 5
        satisfaccion = int(satisfaccion)
        assert 1 <= satisfaccion <= 5
        
        return True
    except (AssertionError, ValueError):
        # Si hay algún error en la validación, devolver False
        return False

# Función para procesar el archivo CSV y generar el JSON solicitado
def procesar_ventas_csv_a_json(archivo_csv: str, archivo_json: str) -> None:
    ventas_por_ano = defaultdict(lambda: {
        "promedio_ventas_por_vendedor": defaultdict(float),
        "calificaciones_vendedores": defaultdict(list),
        "ventas_por_modelo": defaultdict(int)
    })
    
    total_filas = 0
    filas_validas = 0
    
    try:
        with open(archivo_csv, mode='r', encoding='utf-8') as file:
            lector_csv = csv.reader(file)
            next(lector_csv)  # Omitir la fila de encabezados
            
            for fila in lector_csv:
                total_filas += 1
                if validar_fila(fila):
                    filas_validas += 1
                    vendedor, marca, modelo, año, precio, satisfaccion, comentarios, promocion, anio_venta = fila
                    año = int(año)
                    anio_venta = int(anio_venta)
                    precio = float(precio)
                    satisfaccion = int(satisfaccion)
                    
                    # Acumular datos para el cálculo del promedio de ventas por vendedor
                    ventas_por_ano[anio_venta]["promedio_ventas_por_vendedor"][vendedor] += precio
                    
                    # Acumular calificaciones para calcular el promedio más adelante
                    ventas_por_ano[anio_venta]["calificaciones_vendedores"][vendedor].append(satisfaccion)
                    
                    # Contar ventas por modelo
                    ventas_por_ano[anio_venta]["ventas_por_modelo"][modelo] += 1
        
        # Calcular los promedios y preparar los datos finales
        resultado = {}
        for anio, datos in ventas_por_ano.items():
            promedio_ventas_por_vendedor = {
                vendedor: total / count
                for vendedor, total in datos["promedio_ventas_por_vendedor"].items()
                for count in [len(datos["calificaciones_vendedores"][vendedor])]
            }
            
            calificaciones_vendedores = {
                vendedor: round(sum(calificaciones) / len(calificaciones), 1)
                for vendedor, calificaciones in datos["calificaciones_vendedores"].items()
            }
            
            # Ordenar a los vendedores por calificación
            calificaciones_vendedores_ordenadas = dict(sorted(calificaciones_vendedores.items(), key=lambda item: item[1], reverse=True))
            
            resultado[str(anio)] = {
                "promedio_ventas_por_vendedor": promedio_ventas_por_vendedor,
                "calificaciones_vendedores": calificaciones_vendedores_ordenadas,
                "ventas_por_modelo": dict(datos["ventas_por_modelo"])
            }
        
        # Escribir el resultado en un archivo JSON
        with open(archivo_json, mode='w', encoding='utf-8') as file:
            json.dump(resultado, file, indent=4, ensure_ascii=False)
        
        print(f"Procesamiento completado. {filas_validas} de {total_filas} filas válidas.")
    
    except FileNotFoundError:
        print(f"Error: El archivo {archivo_csv} no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Ejemplo de uso
archivo_csv = 'ventas_autos_usados.csv'
archivo_json = 'ventas_autos_usados.json'
procesar_ventas_csv_a_json(archivo_csv, archivo_json)