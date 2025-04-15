import pandas as pd
import re
from datetime import datetime, timedelta
import json

# Función para limpiar y validar fechas
def limpiar_fecha(fecha_str):
    try:
        # Usar regex para asegurarse de que la fecha tenga el formato correcto
        fecha_regex = r'\b\d{4}-\d{2}-\d{2}\b'
        fecha_validada = re.match(fecha_regex, fecha_str)
        if fecha_validada:
            return datetime.strptime(fecha_str, '%Y-%m-%d').strftime('%Y-%m-%d')
        else:
            raise ValueError(f"Formato de fecha inválido: {fecha_str}")
    except ValueError as e:
        print(f"Error al limpiar la fecha {fecha_str}: {e}")
        return None

# Función para procesar los archivos CSV y devolver un DataFrame limpio
def procesar_datos(ventas_file, productos_file):
    # Cargar los archivos CSV
    df_ventas = pd.read_csv(ventas_file)
    df_productos = pd.read_csv(productos_file)

    # Limpiar las fechas
    df_ventas['fecha'] = df_ventas['fecha'].apply(limpiar_fecha)

    # Convertir 'cantidad', 'precio' y 'total' a float y formatarlos
    df_ventas['cantidad'] = pd.to_numeric(df_ventas['cantidad'], errors='coerce').round(2)
    df_ventas['precio'] = pd.to_numeric(df_ventas['precio'], errors='coerce').round(2)
    df_ventas['total'] = pd.to_numeric(df_ventas['total'], errors='coerce').round(2)

    # Manejar valores faltantes
    df_ventas['cantidad'].fillna(df_ventas['cantidad'].mean(), inplace=True)
    df_ventas['precio'].fillna(df_ventas['precio'].mean(), inplace=True)
    df_ventas['total'].fillna(df_ventas['total'].mean(), inplace=True)

    # Eliminar duplicados (excluyendo 'total')
    df_ventas.drop_duplicates(subset=['fecha', 'productoID', 'cantidad', 'precio'], keep='first', inplace=True)

    # Verificar coincidencia de productoHash y llenar requerimientos de verificación
    df_ventas['requiereVerificacion'] = df_ventas.apply(lambda row: row['productoHash'] != df_productos[df_productos['productoID'] == row['productoID']]['productoHash'].values[0], axis=1)

    # Agrupar por productoID y sumar ventas para el último año
    df_ventas['fecha'] = pd.to_datetime(df_ventas['fecha'])
    df_ventas_last_year = df_ventas[df_ventas['fecha'] >= (datetime.now() - timedelta(days=365))]
    ventas_totales = df_ventas_last_year.groupby('productoID')['total'].sum().reset_index()

    # Combinar ventas con productos
    df_combinado = pd.merge(ventas_totales, df_productos, on='productoID')

    # Filtrar el cuartil superior de ventas
    df_filtrado = df_combinado.nlargest(int(len(df_combinado) * 0.75), 'total')

    # Formatear 'total' para mostrar dos decimales
    df_filtrado['total'] = df_filtrado['total'].round(2)

    # Convertir a JSON
    resultado_json = df_filtrado[['productoID', 'nombreProducto', 'categoria', 'total', 'fechaUltimaVenta', 'requiereVerificacion']].to_dict(orient='records')

    return resultado_json

# Ejecución del proceso
ventas_file = 'ventas.csv'
productos_file = 'productos.csv'
resultado_json = procesar_datos(ventas_file, productos_file)

# Imprimir el resultado en formato JSON
print(json.dumps(resultado_json, indent=4, ensure_ascii=False))