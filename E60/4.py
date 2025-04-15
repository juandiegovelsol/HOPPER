import pandas as pd
import json
from datetime import datetime

def analizar_reabastecimiento(archivo_csv):
    # Cargar los datos desde el archivo CSV en un DataFrame
    df = pd.read_csv(archivo_csv)
    
    # Eliminar filas con valores nulos
    df.dropna(inplace=True)
    
    # Convertir las columnas relevantes a los tipos de datos correctos
    df['stock_sucursal_principal'] = df['stock_sucursal_principal'].astype(float)
    df['stock_sucursal_secundaria'] = df['stock_sucursal_secundaria'].astype(float)
    df['ventas_periodo_anterior'] = df['ventas_periodo_anterior'].astype(float)
    df['fecha_ultimo_abastecimiento'] = pd.to_datetime(df['fecha_ultimo_abastecimiento'])
    
    # Calcular el promedio de ventas mensual del período anterior
    df['ventas_promedio_mes_anterior'] = df.groupby('fecha_ultimo_abastecimiento')['ventas_periodo_anterior'].transform('mean')
    
    # Crear la columna 'Reabastecer'
    df['Reabastecer'] = df['stock_sucursal_principal'] < df['ventas_promedio_mes_anterior'] * 0.5
    
    # Convertir el DataFrame a formato JSON
    resultado = df.to_dict(orient='records')
    
    # Guardar el resultado en un archivo JSON
    with open('resultado_reabastecimiento.json', 'w') as json_file:
        json.dump(resultado, json_file, indent=4)
    
    return 'resultado_reabastecimiento.json'

# Ejemplo de uso
archivo_csv = 'stock_sucursales.csv'
resultado_json = analizar_reabastecimiento(archivo_csv)
print(f'El archivo JSON de resultado ha sido guardado como: {resultado_json}')
