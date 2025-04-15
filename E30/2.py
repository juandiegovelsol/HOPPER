import pandas as pd
import json
from datetime import datetime, timedelta
import os

def cargar_datos_csv(ruta_ventas, ruta_productos):
    """
    Carga los datos de ventas y productos desde archivos CSV.

    Args:
        ruta_ventas (str): Ruta al archivo CSV de ventas.
        ruta_productos (str): Ruta al archivo CSV de productos.

    Returns:
        tuple: Un tuple con los DataFrames de ventas y productos.
    """
    try:
        df_ventas = pd.read_csv(ruta_ventas)
        df_productos = pd.read_csv(ruta_productos)
        return df_ventas, df_productos
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_ventas} o {ruta_productos}.")
        return None, None
    except pd.errors.EmptyDataError:
        print(f"Error: Los archivos {ruta_ventas} o {ruta_productos} están vacíos.")
        return None, None
    except pd.errors.ParserError:
        print(f"Error: Hubo un problema al analizar el archivo {ruta_ventas} o {ruta_productos}.")
        return None, None

def limpiar_datos(df_ventas, df_productos):
    """
    Limpia y procesa los datos de ventas y productos.

    Args:
        df_ventas (DataFrame): DataFrame de ventas.
        df_productos (DataFrame): DataFrame de productos.

    Returns:
        tuple: Un tuple con los DataFrames limpios y los productos validados.
    """
    # Eliminar duplicados basados en todas las columnas excepto 'total'
    df_ventas.drop_duplicates(subset=['fecha', 'productoID', 'cantidad', 'precio', 'productoHash'], inplace=True)

    # Corregir formatos de fecha
    df_ventas['fecha'] = pd.to_datetime(df_ventas['fecha'], errors='coerce')
    df_ventas['fecha'] = df_ventas['fecha'].dt.strftime('%Y-%m-%d')

    # Convertir campos numéricos a float y asegurarse de que tengan dos decimales
    df_ventas['cantidad'] = pd.to_numeric(df_ventas['cantidad'], errors='coerce').fillna(0).round(2)
    df_ventas['precio'] = pd.to_numeric(df_ventas['precio'], errors='coerce').fillna(0).round(2)
    df_ventas['total'] = pd.to_numeric(df_ventas['total'], errors='coerce').fillna(0).round(2)

    # Rellenar valores faltantes en campos numéricos con el promedio de la columna
    df_ventas['cantidad'].fillna(df_ventas['cantidad'].mean(), inplace=True)
    df_ventas['precio'].fillna(df_ventas['precio'].mean(), inplace=True)
    df_ventas['total'].fillna(df_ventas['total'].mean(), inplace=True)

    # Rellenar valores faltantes en campos de texto con "No disponible"
    df_ventas['nombreProducto'].fillna("No disponible", inplace=True)
    df_ventas['categoria'].fillna("No disponible", inplace=True)

    # Validar y corregir datos basados en productoHash
    df_ventas['productoHash'] = df_ventas['productoHash'].str.strip()
    df_productos['productoHash'] = df_productos['productoHash'].str.strip()

    productos_validos = df_productos.set_index('productoID').dropna()
    df_ventas['requiereVerificacion'] = df_ventas['productoHash'].isin(productos_validos.index).astype(bool)

    # Calcular ventas totales por producto en el último año
    df_ventas['fechaUltimaVenta'] = df_ventas['fecha'].dt.date
    df_ventas = df_ventas[df_ventas['fechaUltimaVenta'] >= datetime.now().date() - timedelta(days=365)]
    ventas_totales = df_ventas.groupby('productoID')['total'].sum().reset_index()

    # Filtrar productos que hayan generado ingresos en el cuartil superior
    ventas_totales = ventas_totales.sort_values(by='total', ascending=False)
    quintil_superior = ventas_totales.iloc[:int(len(ventas_totales) * 0.75)]
    productos_filtrados = df_productos[df_productos['productoID'].isin(quintil_superior['productoID'])]

    # Calcular ventas totales y fechas de última venta para cada producto filtrado
    productos_filtrados['ventasTotales'] = ventas_totales['total']
    productos_filtrados['fechaUltimaVenta'] = ventas_totales['fechaUltimaVenta']

    return productos_filtrados, df_ventas

def guardar_datos_json(productos_filtrados, ruta_salida):
    """
    Guarda los datos procesados en un archivo JSON.

    Args:
        productos_filtrados (DataFrame): DataFrame de productos filtrados.
        ruta_salida (str): Ruta donde se guardará el archivo JSON.
    """
    try:
        productos_filtrados.to_json(ruta_salida, orient='records', indent=4)
        print(f"Datos guardados exitosamente en {ruta_salida}")
    except Exception as e:
        print(f"Error al guardar los datos en JSON: {e}")

def generar_datos_falsos(ruta_ventas, ruta_productos):
    """
    Genera datos falsos para los archivos CSV si no existen.

    Args:
        ruta_ventas (str): Ruta al archivo CSV de ventas.
        ruta_productos (str): Ruta al archivo CSV de productos.
    """
    if not os.path.exists(ruta_ventas):
        datos_ventas = {
            'fecha': ['2021-01-01', '2021-01-02', '2021-02-01', '2021-03-01', '2021-04-01'],
            'productoID': [101, 102, 103, 104, 105],
            'cantidad': [2, 1, 3, 2, 1],
            'precio': [15.00, 25.00, 30.00, 35.00, 40.00],
            'total': [30.00, 25.00, 90.00, 70.00, 40.00],
            'productoHash': ['abc123', 'def456', 'ghi789', 'jkl012', 'mno345']
        }
        df_ventas = pd.DataFrame(datos_ventas)
        df_ventas.to_csv(ruta_ventas, index=False)

    if not os.path.exists(ruta_productos):
        datos_productos = {
            'productoID': [101, 102, 103, 104, 105],
            'nombreProducto': ['Zapato deportivo', 'Camiseta deportiva', 'Gorra', 'Guantes', 'Calcetines'],
            'categoria': ['Calzado', 'Ropa', 'Accesorios', 'Accesorios', 'Accesorios'],
            'productoHash': ['abc123', 'def456', 'ghi789', 'jkl012', 'mno345']
        }
        df_productos = pd.DataFrame(datos_productos)
        df_