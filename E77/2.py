import pandas as pd
import json
from datetime import datetime

def analizar_reabastecimiento(archivo_csv):
    """
    Esta función analiza los niveles de stock en las sucursales y determina si requieren reabastecimiento
    comparando las ventas promedio del período anterior con el stock actual. Los resultados se almacenan
    en un archivo JSON.

    Parámetros:
    archivo_csv (str): Ruta del archivo CSV que contiene los datos de las sucursales.

    Devuelve:
    str: Ruta del archivo JSON generado con los resultados del análisis.
    """
    # Leer el archivo CSV en un DataFrame
    try:
        df = pd.read_csv(archivo_csv)
    except FileNotFoundError:
        print(f"Error: El archivo {archivo_csv} no se encontró.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: El archivo {archivo_csv} está vacío.")
        return None
    except pd.errors.ParserError:
        print(f"Error: No se pudo analizar el archivo CSV {archivo_csv}. Asegúrese de que esté bien formateado.")
        return None

    # Eliminar filas con valores nulos
    df.dropna(inplace=True)

    # Convertir las columnas relevantes a tipos de datos apropiados
    try:
        df['stock_sucursal_principal'] = df['stock_sucursal_principal'].astype(float)
        df['stock_sucursal_secundaria'] = df['stock_sucursal_secundaria'].astype(float)
        df['ventas_periodo_anterior'] = df['ventas_periodo_anterior'].astype(float)
        df['fecha_ultimo_abastecimiento'] = pd.to_datetime(df['fecha_ultimo_abastecimiento'])
    except ValueError as e:
        print(f"Error: Formato de datos incorrecto en el archivo CSV. {e}")
        return None

    # Calcular el promedio de ventas del período anterior
    df['ventas_promedio_periodo_anterior'] = df['ventas_periodo_anterior'].rolling(window=1).mean()

    # Crear la columna 'Reabastecer'
    df['Reabastecer'] = (df['stock_sucursal_principal'] < 0.5 * df['ventas_promedio_periodo_anterior']) | \
                      (df['stock_sucursal_secundaria'] < 0.5 * df['ventas_promedio_periodo_anterior'])

    # Guardar el DataFrame resultante en un archivo JSON
    try:
        resultado_json = df.to_dict(orient='records')
        with open('resultado_reabastecimiento.json', 'w') as f:
            json.dump(resultado_json, f, indent=4)
        print("Archivo JSON generado exitosamente.")
    except Exception as e:
        print(f"Error al generar el archivo JSON: {e}")

# Ejemplo de uso
archivo_csv = 'niveles_stock.csv'  # Cambia esta ruta al archivo CSV que desees usar
analizar_reabastecimiento(archivo_csv)