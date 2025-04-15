import pandas as pd
import json
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import random

def generar_datos_falsos(num_filas=1000):
    """
    Genera datos falsos de uso de datos móviles.

    Args:
        num_filas (int): Número de filas de datos a generar.

    Returns:
        pd.DataFrame: DataFrame con los datos falsos generados.
    """
    fecha_inicio = datetime(2023, 6, 1)
    fecha_fin = datetime(2023, 12, 31)
    datos = {
        'fecha': [fecha_inicio + timedelta(days=random.randint(0, (fecha_fin - fecha_inicio).days)) for _ in range(num_filas)],
        'cliente_id': [random.randint(10000, 99999) for _ in range(num_filas)],
        'uso_datos_mb': [round(random.uniform(50, 5000), 2) for _ in range(num_filas)],
        'hora_dia': [random.choice(['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']) for _ in range(num_filas)]
    }
    return pd.DataFrame(datos)

def validar_datos(df):
    """
    Valida los datos del DataFrame.

    Args:
        df (pd.DataFrame): DataFrame a validar.

    Returns:
        bool: True si los datos son válidos, False en caso contrario.
    """
    if df[['fecha', 'cliente_id', 'uso_datos_mb', 'hora_dia']].isnull().values.any():
        print("Error: Datos faltantes en el DataFrame.")
        return False
    if not pd.api.types.is_numeric_dtype(df['uso_datos_mb']):
        print("Error: La columna 'uso_datos_mb' contiene valores no numéricos.")
        return False
    if not pd.api.types.is_numeric_dtype(df['cliente_id']):
        print("Error: La columna 'cliente_id' contiene valores no numéricos.")
        return False
    if not pd.api.types.is_datetime64_any_dtype(df['fecha']):
        print("Error: La columna 'fecha' contiene valores no en formato de fecha.")
        return False
    return True

def convertir_fecha(df):
    """
    Convierte las fechas en el DataFrame al formato ISO.

    Args:
        df (pd.DataFrame): DataFrame con las fechas a convertir.

    Returns:
        pd.DataFrame: DataFrame con las fechas convertidas al formato ISO.
    """
    df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce').dt.isoformat()
    return df

def calcular_promedios_y_anomalias(df):
    """
    Calcula el uso total de datos, el promedio diario, y los días con uso anómalo.

    Args:
        df (pd.DataFrame): DataFrame con los datos de uso de datos.

    Returns:
        pd.DataFrame: DataFrame con los cálculos agregados.
    """
    df['dias_en_mes'] = df['fecha'].dt.to_period('M').dt.day
    df['promedio_diario_mb'] = df.groupby('cliente_id')['uso_datos_mb'].transform('mean')
    df['dias_anomalo'] = df[df['uso_datos_mb'] > 1.2 * df['promedio_diario_mb']].index
    return df

def generar_resumen_mensual(df):
    """
    Genera el resumen mensual del uso de datos.

    Args:
        df (pd.DataFrame): DataFrame con los datos agregados.

    Returns:
        dict: Diccionario con el resumen mensual.
    """
    resumen_mensual = {}
    for cliente_id, grupo in df.groupby('cliente_id'):
        uso_total_datos_mb = grupo['uso_datos_mb'].sum()
        promedio_diario_mb = grupo['promedio_diario_mb'].mean()
        dias_uso_anomalo = len(grupo[grupo['dias_anomalo']])
        porcentaje_dias_anomalo = (dias_uso_anomalo / len(grupo)) * 100
        resumen_mensual[cliente_id] = {
            'uso_total_datos_mb': uso_total_datos_mb,
            'promedio_diario_mb': round(promedio_diario_mb, 2),
            'dias_uso_anomalo': dias_uso_anomalo,
            'porcentaje_dias_anomalo': round(porcentaje_dias_anomalo, 2)
        }
    return resumen_mensual

def guardar_resumen_json(resumen_mensual, archivo_json):
    """
    Guarda el resumen mensual en un archivo JSON.

    Args:
        resumen_mensual (dict): Diccionario con el resumen mensual.
        archivo_json (str): Nombre del archivo JSON de salida.
    """
    with open(archivo_json, 'w') as f:
        json.dump(resumen_mensual, f, indent=4)

def generar_grafico_uso_datos(df):
    """
    Genera un gráfico de líneas que muestre la tendencia del uso de datos a lo largo del tiempo para cada cliente.

    Args:
        df (pd.DataFrame): DataFrame con los datos de uso de datos.
    """
    plt.figure(figsize=(14, 7))
    for cliente_id in df['cliente_id'].unique():
        cliente_data = df[df['cliente_id'] == cliente_id]
        plt.plot(cliente_data['fecha'], cliente_data['uso_datos_mb'], label=f'Cliente {cliente_id}')
    plt.title('Tendencia del uso de datos móviles a lo largo del tiempo')
    plt.xlabel('Fecha')
    plt.ylabel('Uso de datos (MB)')
    plt.legend()
    plt.grid(True)
    plt.show()

def analizar_uso_datos(archivo_csv, archivo_json, num_filas_falsos=1000):
    """
    Analiza el uso de datos móviles a partir de un archivo CSV, genera datos falsos si es necesario, y guarda un resumen en JSON.

    Args:
        archivo_csv (str): Nombre del archivo CSV de entrada.
        archivo_json (str): Nombre del archivo JSON de salida.
        num_filas_falsos (int): Número de filas de datos falsos a generar.
    """
    print(f"Leyendo archivo: {archivo_csv}")
    df = pd.read_csv(archivo_csv)

    if not validar_datos(df):
        return

    print("Generando datos falsos...")
    df_falsos = generar_datos_falsos(num_filas_falsos)
    df = pd.concat([df, df_falsos], ignore_index=True)

    print("Conversionando fechas...")
    df