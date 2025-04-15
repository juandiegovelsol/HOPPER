import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from datetime import datetime
import json
from sklearn.preprocessing import StandardScaler

# Configuración para generar datos falsos
SEED = 42
np.random.seed(SEED)

# Función para generar datos falsos con una tendencia diaria para cada cliente
def generar_datos_falsos(num_clientes=100, dias=30):
    dates = pd.date_range(start='2023-06-01', end='2023-06-30', freq='D')
    datos = {
        'fecha': np.repeat(dates, num_clientes),
        'cliente_id': np.tile(np.arange(1, num_clientes + 1, 1), len(dates)),
        'uso_datos_mb': np.random.randint(50, 1000, size=len(dates) * num_clientes),
        'hora_dia': np.tile([f"{hour}:00" for hour in range(1, 25)], num_clientes)
    }
    print(len(datos['fecha']),len(datos['hora_dia']))
    df = pd.DataFrame(datos)
    return df

# Carga los datos desde el archivo CSV, reemplazando valores nulos por 0
def cargar_datos(archivo_csv):
    if not os.path.exists(archivo_csv):
        print(f"El archivo {archivo_csv} no existe. Generando datos falsos para probar el programa.")
        df = generar_datos_falsos()
        df.to_csv(archivo_csv, index=False)
    else:
        df = pd.read_csv(archivo_csv)
    
    # Reemplazar valores nulos por 0
    df.fillna(0, inplace=True)
    return df

# Convierte la columna 'hora_dia' al formato datetime si está presente
def convertir_fecha(df):
    if 'hora_dia' in df.columns:
        df['hora_dia'] = pd.to_datetime(df['hora_dia'], format='%H:%M').dt.time
    
    # Convierte 'fecha' al formato datetime
    df['fecha'] = pd.to_datetime(df['fecha'])
    
    # Convierte 'cliente_id' al formato entero
    df['cliente_id'] = df['cliente_id'].astype(int)
    return df

# Calcula el uso total de datos por cliente, identificando días anómalos y estadísticas relevantes
def analizar_uso_datos(df):
    df = convertir_fecha(df)
    
    # Verifica si hay datos erróneos en las columnas clave
    if df[['fecha', 'cliente_id', 'uso_datos_mb']].isnull().any().any():
        print("Error: Hay datos faltantes en las columnas clave.")
        return None
    if not df['uso_datos_mb'].dtype.kind in 'nu':
        print("Error: Se detectaron valores no numéricos en la columna 'uso_datos_mb'.")
        return None
    if df['cliente_id'].dtype.kind not in 'ui':
        print("Error: Se detectaron valores no numéricos en la columna 'cliente_id'.")
        return None
    
    df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d', errors='coerce')
    
    # Filtra filas válidas
    df_valido = df.dropna(subset=['fecha', 'cliente_id', 'uso_datos_mb', 'hora_dia'])

    # Agrupa por cliente y fecha, y suma el uso de datos
    resumen = df_valido.groupby(['cliente_id', 'fecha']).sum().reset_index()

    # Calcula el uso diario y el promedio diario
    resumen['uso_diario_mb'] = resumen['uso_datos_mb'] / len(resumen['fecha'].unique())
    resumen['promedio_diario_mb'] = resumen['uso_diario_mb'].mean()

    # Define días anómalos (donde el uso supera un 20% el promedio diario)
    resumen['es_anomalo'] = abs(resumen['uso_datos_mb'] - resumen['uso_diario_mb']) / resumen['promedio_diario_mb'] > 0.2

    # Calcula el número de días anómalos y el porcentaje
    resumen['dias_anomalo'] = resumen['es_anomalo'].astype(int)
    resumen['porcentaje_anomalo'] = (resumen['dias_anomalo'] / len(resumen['fecha'].unique()) * 100).round(2)

    return resumen

# Genera datos falsos para test
def generar_df_falso():
    df = generar_datos_falsos(10, 30)
    df.to_csv('datos_movil.csv', index=False)

# Genera un gráfico de líneas que muestra la tendencia del uso de datos a lo largo del tiempo para cada cliente
def graficar_uso_datos(resumen_mensual):
    plt.figure(figsize=(12, 8))
    for cliente, datos in resumen_mensual.items():
        plt.plot(datos['fecha'], datos['uso_datos_mb'], label=f'Cliente {cliente}')
    plt.xlabel('Fecha')
    plt.ylabel('Uso de Datos (MB)')
    plt.title('Tendencia del Uso de Datos Móviles por Cliente')
    plt.legend(title='Cliente')
    plt.grid(True)
    plt.show()

# Guardar el análisis en un archivo .json
def guardar_json(resultado, archivo_json):
    with open(archivo_json, 'w') as f:
        json.dump(resultado, f, indent=4)

# Función principal que ejecuta todo el flujo: análisis, generación de gráficos y guardado del resultado en formato JSON
def analizar_y_generar_reporte(archivo_csv, archivo_json):
    # Cargar y preprocesar datos
    df = cargar_datos(archivo_csv)
    
    # Analizar uso de datos
    resumen_mensual = analizar_uso_datos(df)
    
    # Si el análisis fue exitoso, proceder a generar el JSON y el gráfico
    if resumen_mensual is not None:
        resumen_mensual = {cliente: datos for cliente, datos in resumen_mensual.iterrows()}
        guardar_json(resumen_mensual, archivo_json)
        graficar_uso_datos(resumen_mensual)
    else:
        print("El análisis no se pudo completar debido a datos erróneos.")

# Ejecutar el programa
archivo_csv = 'datos_movil.csv'
archivo_json = 'resumen_analisis.json'
generar_df_falso()
analizar_y_generar_reporte(archivo_csv, archivo_json)
