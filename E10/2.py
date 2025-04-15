import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Función para generar datos falsos
def generar_datos_falsos(num_registros=1000):
    np.random.seed(42)  # Para generar números aleatorios reproducibles
    datos = {
        'fecha': [datetime(2023, np.random.randint(6, 8), np.random.randint(1, 28)).strftime('%Y-%m-%d') for _ in range(num_registros)],
        'cliente_id': np.random.randint(10000, 20000, size=num_registros),
        'uso_datos_mb': np.random.randint(50, 1500, size=num_registros),
        'hora_dia': [f"{np.random.randint(0, 23):02}:{np.random.randint(0, 60):02}" for _ in range(num_registros)]
    }
    return pd.DataFrame(datos)

# Función para validar y procesar los datos
def procesar_datos(df):
    # Convertir columnas a los tipos de datos correctos
    df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')
    df['cliente_id'] = pd.to_numeric(df['cliente_id'], errors='coerce')
    df['uso_datos_mb'] = pd.to_numeric(df['uso_datos_mb'], errors='coerce')
    
    # Filtrar datos faltantes o erróneos
    df.dropna(inplace=True)
    df = df[(df['cliente_id'].notna()) & (df['uso_datos_mb'].notna())]
    
    return df

# Función para analizar el uso de datos
def analizar_uso_datos(df):
    df.set_index('fecha', inplace=True)
    df.sort_index(inplace=True)
    
    resumen_mensual = {}
    
    for cliente_id, grupo in df.groupby('cliente_id'):
        uso_diario = grupo['uso_datos_mb'].resample('D').sum()
        promedio_diario = uso_diario.mean()
        dias_anomalos = (uso_diario > promedio_diario * 1.2).sum()
        porcentaje_anomalos = (dias_anomalos / len(uso_diario)) * 100 if len(uso_diario) > 0 else 0
        
        resumen_mensual[cliente_id] = {
            'uso_total_datos_mb': uso_diario.sum(),
            'promedio_diario_mb': promedio_diario,
            'dias_uso_anomalo': dias_anomalos,
            'porcentaje_dias_anomalo': porcentaje_anomalos
        }
        
        # Gráfico de líneas para el uso diario de datos
        plt.figure(figsize=(10, 5))
        plt.plot(uso_diario.index, uso_diario.values, marker='o', label=f'Cliente {cliente_id}')
        plt.title(f'Uso de Datos Diarios - Cliente {cliente_id}')
        plt.xlabel('Fecha')
        plt.ylabel('Uso de Datos (MB)')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f'uso_datos_cliente_{cliente_id}.png')
        plt.close()
    
    return resumen_mensual

# Función principal para ejecutar el análisis
def ejecutar_analisis(archivo_csv=None, generar_datos=False):
    if generar_datos:
        df = generar_datos_falsos()
    else:
        if not archivo_csv:
            raise ValueError("Debe especificar el archivo CSV o generar datos falsos.")
        df = pd.read_csv(archivo_csv)
    
    df_procesado = procesar_datos(df)
    resumen = analizar_uso_datos(df_procesado)
    
    # Guardar el resumen en un archivo JSON
    with open('resumen_uso_datos.json', 'w') as f_json:
        json.dump({'resumen_mensual': resumen}, f_json, indent=4)

    print("Análisis completado. Resultados guardados en 'resumen_uso_datos.json'.")

# Ejecutar el análisis con datos falsos
ejecutar_analisis(archivo_csv='datos_uso_datos.csv')