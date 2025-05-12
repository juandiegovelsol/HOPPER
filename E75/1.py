import pandas as pd
import numpy as np
import json
import os
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def generar_datos_falsos(cantidad_filas=1000):
    """
    Genera un archivo CSV con datos falsos de uso de datos móviles.

    Args:
        cantidad_filas (int): Número de filas a generar.

    Returns:
        pd.DataFrame: DataFrame con los datos generados.

    Raises:
        ValueError: Si la cantidad de filas es negativa.
    """
    if cantidad_filas < 0:
        raise ValueError("La cantidad de filas no puede ser negativa.")

    # Configurar semilla para reproducibilidad (opcional)
    np.random.seed(42)

    # Crear fechas aleatorias dentro de un rango de 1 año
    fecha_inicio = datetime(2023, 1, 1)
    fecha_fin = datetime(2024, 1, 1)
    fechas = pd.date_range(start=fecha_inicio, end=fecha_fin, freq='D')

    # Generar datos falsos
    clientes = np.random.choice(['12345', '12346', '12347'], cantidad_filas)
    uso_datos_mb = np.random.randint(100, 1000, cantidad_filas)  # Uso de datos entre 100 y 1000 MB
    horas_dia = np.random.choice(['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00'], cantidad_filas)

    # Crear el DataFrame
    df = pd.DataFrame({'fecha': fechas, 'cliente_id': clientes, 'uso_datos_mb': uso_datos_mb, 'hora_dia': horas_dia})

    # Guardar como CSV
    archivo_csv = 'datos_falsos.csv'
    df.to_csv(archivo_csv, index=False)
    print(f"Datos falsos generados y guardados en '{archivo_csv}'.")

    return df

def analizar_uso_datos(archivo_csv):
    """
    Analiza el uso de datos móviles desde un archivo CSV.

    Args:
        archivo_csv (str): Ruta del archivo CSV con los datos.

    Returns:
        pd.DataFrame: DataFrame con los datos analisados.

    Raises:
        FileNotFoundError: Si el archivo no existe.
        ValueError: Si el archivo no tiene las columnas requeridas o contiene datos inválidos.
    """
    if not os.path.exists(archivo_csv):
        raise FileNotFoundError(f"El archivo '{archivo_csv}' no existe.")

    # Leer el archivo CSV
    try:
        df = pd.read_csv(archivo_csv)
    except Exception as e:
        raise ValueError(f"Error al leer el archivo CSV: {e}")

    # Validar columnas requeridas
    columnas_requeridas = ['fecha', 'cliente_id', 'uso_datos_mb', 'hora_dia']
    for columna in columnas_requeridas:
        if columna not in df.columns:
            raise ValueError(f"El archivo CSV no contiene la columna requerida '{columna}'.")

    # Convertir la columna 'fecha' al formato ISO
    try:
        df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d', errors='coerce')
    except Exception as e:
        raise ValueError(f"Error al convertir la columna 'fecha' al formato ISO: {e}")

    # Eliminar filas con fechas inválidas
    df = df.dropna(subset=['fecha'])

    # Convertir la columna 'cliente_id' a numérica
    try:
        df['cliente_id'] = pd.to_numeric(df['cliente_id'], errors='coerce')
    except Exception as e:
        raise ValueError(f"Error al convertir la columna 'cliente_id' a numérica: {e}")

    # Eliminar filas con cliente_id inválido
    df = df.dropna(subset=['cliente_id'])

    # Convertir la columna 'uso_datos_mb' a numérica
    try:
        df['uso_datos_mb'] = pd.to_numeric(df['uso_datos_mb'], errors='coerce')
    except Exception as e:
        raise ValueError(f"Error al convertir la columna 'uso_datos_mb' a numérica: {e}")

    # Eliminar filas con uso_datos_mb inválido
    df = df.dropna(subset=['uso_datos_mb'])

    # Agrupar por cliente y día
    uso_datos_mensual = df.groupby(['cliente_id', pd.Grouper(key='fecha', freq='M')])['uso_datos_mb'].sum().reset_index()

    # Calcular el promedio diario
    uso_datos_mensual['promedio_diario_mb'] = uso_datos_mensual.groupby('cliente_id')['uso_datos_mb'].transform('mean')

    # Identificar días con uso anómalo (supera el 20% del promedio diario)
    uso_datos_mensual['dias_uso_anomalo'] = uso_datos_mensual['uso_datos_mb'] > (1.2 * uso_datos_mensual['promedio_diario_mb'])

    # Calcular el porcentaje de días anómalos
    uso_datos_mensual['porcentaje_dias_anomalo'] = (uso_datos_mensual['dias_uso_anomalo'].astype(float) / uso_datos_mensual['fecha'].nunique()).round(2) * 100

    return uso_datos_mensual

def guardar_resultados_json(df, archivo_json):
    """
    Guarda los resultados del análisis en un archivo JSON.

    Args:
        df (pd.DataFrame): DataFrame con los resultados del análisis.
        archivo_json (str): Ruta del archivo JSON donde se guardarán los resultados.

    Raises:
        FileNotFoundError: Si el archivo de salida no se puede crear.
    """
    try:
        resultados = df.groupby('cliente_id').to_dict('index')['resumen_mensual']

        with open(archivo_json, 'w') as f:
            json.dump(resultados, f, indent=4)

        print(f"Resultados guardados en '{archivo_json}'.")
    except Exception as e:
        raise FileNotFoundError(f"Error al guardar los resultados en el archivo JSON: {e}")

def generar_grafico(df):
    """
    Genera un gráfico de líneas que muestra la tendencia del uso de datos a lo largo del tiempo para cada cliente.

    Args:
        df (pd.DataFrame): DataFrame con los datos del análisis.
    """
    plt.figure(figsize=(12, 6))

    # Agrupar por cliente y fecha
    df_agrupado = df.groupby(['cliente_id', pd.Grouper(key='fecha', freq='D')])['uso_datos_mb'].sum().unstack(fill_value=0).reset_index()

    # Graficar el uso de datos diario por cliente
    for cliente in df_agrupado['cliente_id'].unique():
        plt.plot(df_agrupado[df_agrupado['cliente_id'] == cliente]['fecha'], df_agrupado[df_agrupado['cliente_id'] == cliente]['uso