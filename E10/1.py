import pandas as pd
import json
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

# Función para generar datos falsos
def generar_datos_falsos(num_registros=1000):
    np.random.seed(42)  # Para que los datos falsos sean reproducibles
    datos = {
        'fecha': [datetime(2023, 6, np.random.randint(1, 31)).strftime('%Y-%m-%d') for _ in range(num_registros)],
        'cliente_id': np.random.randint(10000, 20000, num_registros),
        'uso_datos_mb': np.random.randint(100, 1500, num_registros),
        'hora_dia': [f"{np.random.randint(0, 24):02}:00" for _ in range(num_registros)]
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
    df = df[(df['cliente_id'].notnull()) & (df['uso_datos_mb'].notnull())]
    
    # Convertir fecha a formato ISO si es necesario
    df['fecha'] = df['fecha'].dt.strftime('%Y-%m-%d')
    
    return df

# Función para analizar el uso de datos
def analizar_uso_datos(df):
    resumen_mensual = {}
    
    # Agrupar por cliente y fecha
    df_agrupado = df.groupby(['cliente_id', 'fecha']).sum().reset_index()
    
    for cliente_id, grupo in df_agrupado.groupby('cliente_id'):
        uso_total = grupo['uso_datos_mb'].sum()
        dias = len(grupo)
        promedio_diario = uso_total / dias
        dias_anomalos = grupo[grupo['uso_datos_mb'] > 1.2 * promedio_diario]['fecha'].nunique()
        porcentaje_anomalos = (dias_anomalos / dias) * 100 if dias > 0 else 0
        
        resumen_mensual[cliente_id] = {
            'uso_total_datos_mb': uso_total,
            'promedio_diario_mb': promedio_diario,
            'dias_uso_anomalo': dias_anomalos,
            'porcentaje_dias_anomalo': porcentaje_anomalos
        }
    
    return resumen_mensual

# Función para generar el gráfico de líneas
def generar_grafico_uso_datos(df):
    plt.figure(figsize=(14, 7))
    for cliente_id, grupo in df.groupby('cliente_id'):
        plt.plot(grupo['fecha'], grupo['uso_datos_mb'], marker='o', label=f'Cliente {cliente_id}')
    plt.title('Tendencia del Uso de Datos Móviles por Cliente')
    plt.xlabel('Fecha')
    plt.ylabel('Uso de Datos (MB)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Función principal para ejecutar el análisis
def ejecutar_analisis(archivo_csv=None, generar_datos=False):
    if generar_datos:
        df = generar_datos_falsos()
    elif archivo_csv:
        try:
            df = pd.read_csv(archivo_csv)
        except FileNotFoundError:
            print(f"Error: El archivo {archivo_csv} no existe.")
            return
        except pd.errors.EmptyDataError:
            print(f"Error: El archivo {archivo_csv} está vacío.")
            return
        except pd.errors.ParserError:
            print(f"Error: Hubo un problema al analizar el archivo {archivo_csv}.")
            return
    else:
        print("Error: Debe especificar un archivo CSV o generar datos falsos.")
        return
    
    df = procesar_datos(df)
    resumen = analizar_uso_datos(df)
    
    # Guardar el resumen en un archivo JSON
    with open('resumen_uso_datos.json', 'w') as f_json:
        json.dump({'resumen_mensual': resumen}, f_json, indent=4)
    
    print("Resumen guardado en 'resumen_uso_datos.json'")
    
    # Generar gráfico
    generar_grafico_uso_datos(df)

# Ejemplo de uso
ejecutar_analisis(archivo_csv='datos_uso_datos.csv')  # Descomentar esta línea si tienes un archivo CSV
#ejecutar_analisis(generar_datos=True)  # Generar y analizar datos falsos