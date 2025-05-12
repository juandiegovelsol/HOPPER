import pandas as pd
import json
from datetime import datetime

def analizar_abastecimiento(archivo_csv):
    # Leer el CSV
    df = pd.read_csv(archivo_csv)
    
    # Convertir las columnas necesarias a tipos correctos
    df['stock_sucursal_principal'] = pd.to_numeric(df['stock_sucursal_principal'], errors='coerce')
    df['stock_sucursal_secundaria'] = pd.to_numeric(df['stock_sucursal_secundaria'], errors='coerce')
    df['ventas_periodo_anterior'] = pd.to_numeric(df['ventas_periodo_anterior'], errors='coerce')
    
    # Eliminar filas con valores nulos
    df = df.dropna()
    
    # Convertir las fechas a tipo datetime
    df['fecha_ultimo_abastecimiento'] = pd.to_datetime(df['fecha_ultimo_abastecimiento'])
    
    # Calcular el mes del año anterior
    mes_actual = df['fecha_ultimo_abastecimiento'].dt.month
    mes_anterior = mes_actual - 1
    
    # Establecer el rango de fechas para el mes anterior
    fecha_inicio_anterior = df['fecha_ultimo_abastecimiento'].dt.replace(day=1, month=mes_anterior, year=df['fecha_ultimo_abastecimiento'].dt.year)
    fecha_fin_anterior = fecha_inicio_anterior + pd.DateOffset(days=30)
    
    # Calcular las ventas mensuales del mes anterior
    ventas_mes_anterior = df[(df['fecha_ultimo_abastecimiento'] >= fecha_inicio_anterior) &
                             (df['fecha_ultimo_abastecimiento'] <= fecha_fin_anterior)]['ventas_periodo_anterior'].sum()
    
    # Crear la columna "Reabastecer"
    df['Reabastecer'] = (df['stock_sucursal_principal'] < (ventas_mes_anterior * 0.5)) | (df['stock_sucursal_secundaria'] < (ventas_mes_anterior * 0.5))
    
    # Convertir el DataFrame a formato JSON
    resultado = df.to_dict(orient='records')
    
    # Guardar el resultado en un archivo JSON
    with open('abastecimiento.json', 'w') as f:
        json.dump(resultado, f, indent=4)
    
    print("El archivo 'abastecimiento.json' ha sido generado con éxito.")

# Ejemplo de uso
analizar_abastecimiento('productos.csv')