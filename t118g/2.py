import csv
from datetime import datetime, time
import sys

# Función para validar el formato de la hora
def validar_hora(hora_str):
    try:
        # Intenta analizar la cadena de tiempo; si falla, lanza una excepción
        datetime.strptime(hora_str, "%S:%M:%H:%d:%m:%Y")
        return True
    except ValueError:
        return False

# Función para calcular el número de horas trabajadas
def calcular_horas_trabajadas(hora_entrada_str, hora_salida_str):
    try:
        hora_entrada = datetime.strptime(hora_entrada_str, "%S:%M:%H:%d:%m:%Y")
        hora_salida = datetime.strptime(hora_salida_str, "%S:%M:%H:%d:%m:%Y")
        
        # Asegurarse de que la hora de salida sea mayor que la de entrada
        if hora_salida <= hora_entrada:
            return 0.0
        
        # Calcula la diferencia, pero fijándolo en caso de que salida sea menor de 24 hrs
        diferencia = hora_salida - hora_entrada
        return diferencia.total_seconds() / 3600.0
    except ValueError:
        return 0.0

# Función principal para procesar el archivo CSV
def procesar_csv(archivo_csv, tasa_por_hora):
    totales_por_dia = {}

    with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
        lector_csv = csv.reader(csvfile)
        next(lector_csv)  # Salta la cabecera

        for fila in lector_csv:
            hora_entrada_str, hora_salida_str = fila
            
            if not validar_hora(hora_entrada_str) or not validar_hora(hora_salida_str):
                print(f"Registro inválido encontrado y ignorado: {fila}")
                continue

            horas_trabajadas = calcular_horas_trabajadas(hora_entrada_str, hora_salida_str)
            if horas_trabajadas > 0:
                fecha = hora_entrada_str.split(':')[4]  # Extraer la fecha 'dd' del formato ss:mm:HH:dd:mm:YYYY
                total_diario = horas_trabajadas * tasa_por_hora
                
                if fecha not in totales_por_dia:
                    totales_por_dia[fecha] = 0
                totales_por_dia[fecha] += total_diario

    # Imprimir resumen
    for fecha, total in totales_por_dia.items():
        print(f"Día {fecha}: ${total:,.2f}")

# Ejemplo de uso
tasa_por_hora_en_clp = 10000  # Por ejemplo, CLP 10,000 por hora
archivo_csv_ejemplo = 'registros_trabajo.csv'
procesar_csv(archivo_csv_ejemplo, tasa_por_hora_en_clp)