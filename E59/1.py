import pandas as pd
import json

def analizar_reabastecimiento(csv_file):
    # Leyendo el archivo CSV
    df = pd.read_csv(csv_file)

    # Eliminando valores nulos
    df = df.dropna()

    # Convertiendo los valores a tipos correctos
    df['stock_sucursal_principal'] = pd.to_numeric(df['stock_sucursal_principal'], errors='coerce')
    df['stock_sucursal_secundaria'] = pd.to_numeric(df['stock_sucursal_secundaria'], errors='coerce')
    df['ventas_periodo_anterior'] = pd.to_numeric(df['ventas_periodo_anterior'], errors='coerce')
    df['fecha_ultimo_abastecimiento'] = pd.to_datetime(df['fecha_ultimo_abastecimiento'], errors='coerce')

    # Verificando y reestableciendo valores nulos (si fuera el caso)
    if df[['stock_sucursal_principal','stock_sucursal_secundaria','ventas_periodo_anterior']].isnull().any().any():
        print("Alerta: se encontraron valores nulos en las columnas: stock_sucursal_principal, stock_sucursal_secundaria o ventas_periodo_anterior")
        df[['stock_sucursal_principal','stock_sucursal_secundaria','ventas_periodo_anterior']] = df[['stock_sucursal_principal','stock_sucursal_secundaria','ventas_periodo_anterior']].fillna(0)

    # Tratando valores inválidos (0 o negativos)
    df[['stock_sucursal_principal','stock_sucursal_secundaria','ventas_periodo_anterior']] = df[['stock_sucursal_principal','stock_sucursal_secundaria','ventas_periodo_anterior']].clip(lower=1)

    # Verificando valores inválidos
    if df[(df['stock_sucursal_principal'] <= 0) | (df['stock_sucursal_secundaria'] <= 0) | (df['ventas_periodo_anterior'] <= 0)].any().any():
        print("Alerta: se encontraron valores inválidos")

    # Agregando columna 'Reabastecer'
    df['Reabastecer'] = (df['stock_sucursal_principal'] < 0.5 * df['ventas_periodo_anterior']) & (df['stock_sucursal_principal'] <= df['ventas_periodo_anterior'])

    # Cambiando booleano a int
    df['Reabastecer'] = df['Reabastecer'].astype(int)

    # Convertimos el DataFrame a una lista de diccionarios
    df_lista = df.to_dict(orient='records')

    # Convertimos la lista de diccionarios a JSON
    with open('reabastecimiento.json', 'w') as f:
        json.dump(df_lista, f, indent=4)

    return 'reabastecimiento.json'

# Ejemplo de uso
csv_file = 'materiales_construccion.csv'
analizar_reabastecimiento(csv_file)