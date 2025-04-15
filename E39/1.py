import csv
import json
from collections import defaultdict
import numpy as np
from scipy import stats

# Función para cargar datos históricos de precipitaciones
def cargar_datos_historicos(archivo_csv):
    datos_historicos = defaultdict(lambda: {"mm_lluvia": [], "horas_lluvia": []})
    try:
        with open(archivo_csv, mode='r', encoding='utf-8') as file:
            lector_csv = csv.DictReader(file)
            for fila in lector_csv:
                fecha = fila['fecha']
                milimetros_lluvia = float(fila['milimetros_lluvia'])
                horas_lluvia = float(fila['duracion_horas'])
                estacion = fila['estacion']
                
                if fecha.startswith('2022-'):
                    datos_historicos[estacion]["mm_lluvia"].append(milimetros_lluvia)
                    datos_historicos[estacion]["horas_lluvia"].append(horas_lluvia)
    except FileNotFoundError:
        print(f"Error: El archivo {archivo_csv} no se encontró.")
    except Exception as e:
        print(f"Error al cargar datos históricos: {e}")
    return datos_historicos

# Función para calcular promedios de precipitaciones y horas de lluvia
def calcular_promedios(datos_historicos):
    promedios = defaultdict(lambda: {"mm_lluvia": 0, "horas_lluvia": 0})
    for estacion, valores in datos_historicos.items():
        promedios[estacion]["mm_lluvia"] = np.mean(valores["mm_lluvia"])
        promedios[estacion]["horas_lluvia"] = np.mean(valores["horas_lluvia"])
    return promedios

# Función para analizar los datos de 2023 y compararlos con los históricos
def analizar_2023(datos_2023, promedios_historicos):
    resultados = {
        "mm_lluvia": defaultdict(float),
        "horas_lluvia": defaultdict(float)
    }
    
    for estacion, valores in datos_2023.items():
        resultados[estacion]["mm_lluvia"] = np.mean(valores["mm_lluvia"])
        resultados[estacion]["horas_lluvia"] = np.mean(valores["horas_lluvia"])
        
        # Comparación estadística para determinar si hay diferencia significativa
        mm_historico = promedios_historicos[estacion]["mm_lluvia"]
        horas_historico = promedios_historicos[estacion]["horas_lluvia"]
        
        t_mm, p_mm = stats.ttest_ind(valores["mm_lluvia"], [mm_historico])
        t_horas, p_horas = stats.ttest_ind(valores["horas_lluvia"], [horas_historico])
        
        resultados[estacion]["hay_diferencia_significativa_mm"] = p_mm < 0.05
        resultados[estacion]["hay_diferencia_significativa_horas"] = p_horas < 0.05
    
    return resultados

# Función principal para procesar los datos y generar el informe
def procesar_datos(archivo_historico, archivo_2023):
    # Cargar datos históricos
    datos_historicos = cargar_datos_historicos(archivo_historico)
    
    # Calcular promedios históricos
    promedios_historicos = calcular_promedios(datos_historicos)
    
    # Cargar datos de 2023
    datos_2023 = defaultdict(lambda: {"mm_lluvia": [], "horas_lluvia": []})
    try:
        with open(archivo_2023, mode='r', encoding='utf-8') as file:
            lector_csv = csv.DictReader(file)
            for fila in lector_csv:
                fecha = fila['fecha']
                milimetros_lluvia = float(fila['milimetros_lluvia'])
                horas_lluvia = float(fila['duracion_horas'])
                estacion = fila['estacion']
                
                if fecha.startswith('2023-'):
                    datos_2023[estacion]["mm_lluvia"].append(milimetros_lluvia)
                    datos_2023[estacion]["horas_lluvia"].append(horas_lluvia)
    except FileNotFoundError:
        print(f"Error: El archivo {archivo_2023} no se encontró.")
        return None
    except Exception as e:
        print(f"Error al cargar datos de 2023: {e}")
        return None
    
    # Analizar datos de 2023
    resultados_2023 = analizar_2023(datos_2023, promedios_historicos)
    
    # Crear el informe JSON
    informe = {
        "mm_lluvia_historico": promedios_historicos,
        "horas_lluvia_historico": promedios_historicos,
        "resultados_2023": resultados_2023
    }
    
    return informe

# Datos falsos para probar el código
archivo_historico = 'datos_historicos_2022.csv'
archivo_2023 = 'datos_2023.csv'

# Crear datos falsos para el archivo histórico
with open(archivo_historico, mode='w', encoding='utf-8') as file:
    fieldnames = ['fecha', 'milimetros_lluvia', 'estacion', 'duracion_horas']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    # Datos históricos (2022)
    writer.writerow({'fecha': '2022-09-01', 'milimetros_lluvia': 50, 'estacion': 'verano', 'duracion_horas': 4})
    writer.writerow({'fecha': '2022-09-02', 'milimetros_lluvia': 30, 'estacion': 'verano', 'duracion_horas': 3})
    writer.writerow({'fecha': '2022-09-03', 'milimetros_lluvia': 20, 'estacion': 'verano', 'duracion_horas': 2})
    # Datos históricos (2022)
    writer.writerow({'fecha': '2022-10-01', 'milimetros_lluvia': 100, 'estacion': 'otoño', 'duracion_horas': 5})
    writer.writerow({'fecha': '2022-10-02', 'milimetros_lluvia': 120, 'estacion': 'otoño', 'duracion_horas': 6})
    writer.writerow({'fecha': '2022-10-03', 'milimetros_lluvia': 90, 'estacion': 'otoño', 'duracion_horas': 4})
    # Datos históricos (2022)
    writer.writerow({'fecha': '2022-11-01', 'milimetros_lluvia': 70, 'estacion': 'invierno', 'duracion_horas': 3})
    writer.writerow({'fecha': '2022-11-02', 'milimetros_lluvia': 80, 'estacion': 'invierno', 'duracion_horas': 4})