import pandas as pd
import os
import json
from collections import defaultdict
from datetime import datetime, timedelta

def limpiar_y_combinar_datos(ventas_file, productos_file):
    # Verificar si los archivos existen
    if not os.path.exists(ventas_file):
        raise FileNotFoundError(f"El archivo '{ventas_file}' no existe.")
    if not os.path.exists(productos_file):
        raise FileNotFoundError(f"El archivo '{productos_file}' no existe.")
    
    # Cargar los datos
    df_ventas = pd.read_csv(ventas_file)
    df_productos = pd.read_csv(productos_file)
    
    # Convertir la columna de fechas a formato YYYY-MM-DD
    df_ventas['fecha'] = pd.to_datetime(df_ventas['fecha'], errors='coerce').dt.strftime('%Y-%m-%d')
    
    # Limpiar duplicados y corregir formatos
    df_ventas.drop_duplicates(subset=['productoID', 'fecha'], keep='first', inplace=True)
    
    # Convertir campos numéricos y manejar valores faltantes
    df_ventas['cantidad'] = pd.to_numeric(df_ventas['cantidad'], errors='coerce').round(2)
    df_ventas['precio'] = pd.to_numeric(df_ventas['precio'], errors='coerce').round(2)
    df_ventas['total'] = pd.to_numeric(df_ventas['total'], errors='coerce').round(2)
    
    df_ventas['cantidad'] = df_ventas['cantidad'].fillna(df_ventas['cantidad'].mean())
    df_ventas['precio'] = df_ventas['precio'].fillna(df_ventas['precio'].mean())
    df_ventas['total'] = df_ventas['total'].fillna(df_ventas['total'].mean())
    
    # Reemplazar valores faltantes en texto con "No disponible"
    df_ventas['productoHash'] = df_ventas['productoHash'].fillna("No disponible")
    df_ventas['fechaUltimaVenta'] = df_ventas['fecha'].max(axis=1)
    
    # Validar y corregir productoHash
    productos_dict = df_productos[['productoID', 'productoHash']].to_dict('records')
    for _, row in df_ventas.iterrows():
        if row['productoHash'] not in productos_dict:
            df_ventas.at[row.index, 'requiereVerificacion'] = True
        else:
            productos = next((p for p in productos_dict if p['productoID'] == row['productoID']), None)
            if productos and productos['productoHash'] != row['productoHash']:
                df_ventas.at[row.index, 'requiereVerificacion'] = True
    
    # Combinar datos por productoID
    df_combinado = pd.merge(df_ventas, df_productos, on='productoID', how='left')
    
    # Filtrar productos que generaron ingresos en el cuartil superior
    df_combinado['ventasTotales'] = df_combinado['cantidad'] * df_combinado['precio']
    df_combinado['ventasTotalesAnuales'] = df_combinado.groupby('productoID')['ventasTotales'].transform(lambda x: x.sum() * (datetime.now() - timedelta(days=365)).year - x.sum() * (datetime.now() - timedelta(days=365) - timedelta(days=365))).round(2)
    
    df_ordenado = df_combinado.sort_values(by='ventasTotalesAnuales', ascending=False)
    df_cuartilSuperior = df_ordenado.head(int(len(df_ordenado) * 0.25))
    
    # Preparar el resultado en formato JSON
    resultado_json = df_cuartilSuperior[['productoID', 'nombreProducto', 'categoria', 'ventasTotales', 'fechaUltimaVenta', 'requiereVerificacion']].to_dict(orient='records')
    
    return resultado_json

# Ejemplo de uso
try:
    resultado = limpiar_y_combinar_datos('ventas.csv', 'productos.csv')
    print(json.dumps(resultado, indent=4, ensure_ascii=False))
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(f"Se produjo un error inesperado: {e}")
