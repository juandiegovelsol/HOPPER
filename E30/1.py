import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import json
from datetime import datetime

# Configuración para la impresión de registros antes y después de los procesos
def print_before_processing(filename, dataframe):
    print(f"\n--- Resumen del archivo {filename} antes de los procesamientos ---")
    print(f"Cantidad de registros: {len(dataframe)}")
    print(f"Primeros registros: {dataframe.head()}")
    print(f"Últimos registros: {dataframe.tail()}")
    print("\n")

# Configuración para la impresión de registros después del procesamiento
def print_after_processing(filename, dataframe):
    print(f"\n--- Resumen del archivo {filename} después de los procesamientos ---")
    print(f"Cantidad de registros después de la limpieza: {len(dataframe)}")
    print(dataframe.head(5))
    print(dataframe.tail(5))
    print("\n")

# Configuración para verificar la integridad de los productoHashes
def verificar_producto_hash(original, reemplazo):
    if original == reemplazo:
        return True
    else:
        return False

# Cálculo del cuartil superior
def calcular_cuartil_superior(dataframe):
    # Calcular ventas totales por producto
    dataframe['ventasTotales'] = dataframe.groupby('productoID')['total'].transform('sum')
    
    # Convertir la fecha a un formato datetime
    dataframe['fecha'] = pd.to_datetime(dataframe['fecha'])
    dataframe['fechaUltimaVenta'] = pd.to_datetime(dataframe['fecha'], errors='coerce')
    
    # Filtrar el último año
    fechaActual = pd.to_datetime('now')
    ultimo_ano_hoy = fechaActual - pd.DateOffset(years=1)
    dataframe = dataframe[(dataframe['fechaUltimaVenta'] >= ultimo_ano_hoy) & (dataframe['fechaUltimaVenta'] <= fechaActual)]
    
    # Ordenar por ventas totales de mayor a menor
    dataframe = dataframe.sort_values(by='ventasTotales', ascending=False)
    
    # Calcular el puntaje Z para el cuartil superior
    scaler = MinMaxScaler(feature_range=(0, 1))
    dataframe['puntajeZ'] = scaler.fit_transform(dataframe[['ventasTotales']].values)
    
    # Determinar el límite superior (cuartil superior)
    limite_superior = dataframe['puntajeZ'].quantile(0.75)
    dataframe['cuartilSuperior'] = dataframe['puntajeZ'] >= limite_superior
    
    return dataframe

# Limpieza y validación de datos
def limpiar_datos(dataframe):
    # Eliminar duplicados basándose en todas las columnas except 'total'
    dataframe = dataframe.drop_duplicates(keep='first', subset=[column for column in dataframe.columns if column != 'total'])
    
    # Convertir 'fecha' a tipo datetime y normalizar a YYYY-MM-DD
    dataframe['fecha'] = pd.to_datetime(dataframe['fecha'], errors='coerce')
    dataframe['fecha'] = dataframe['fecha'].dt.strftime('%Y-%m-%d')
    
    # Asegurar que los campos numéricos sean de tipo float y tengan dos decimales
    dataframe['cantidad'] = dataframe['cantidad'].astype(float).round(2)
    dataframe['precio'] = dataframe['precio'].astype(float).round(2)
    dataframe['total'] = dataframe['total'].astype(float).round(2)
    
    # Rellenar valores faltantes en campos numéricos con el promedio de la columna
    dataframe['cantidad'] = dataframe['cantidad'].fillna(dataframe['cantidad'].mean())
    dataframe['precio'] = dataframe['precio'].fillna(dataframe['precio'].mean())
    dataframe['total'] = dataframe['total'].fillna(dataframe['total'].mean())
    
    # Rellenar valores faltantes en campos de texto con "No disponible"
    dataframe['productoHash'] = dataframe['productoHash'].fillna('No disponible')
    
    # Validar y corregir datos basados en productoHash
    dataframe['productoHash'] = dataframe.apply(lambda row: verificar_producto_hash(row['productoHash'], row['nombreProducto']), axis=1)
    dataframe = dataframe[dataframe['productoHash']]
    dataframe['productoHash'] = dataframe['productoHash'].apply(lambda x: 'requerir verificación' if x else 'hash válido')
    
    return dataframe

# Función principal de procesamiento
def procesar_datos(ventas_file, productos_file, output_file):
    # Cargar los archivos CSV
    df_ventas = pd.read_csv(ventas_file)
    df_productos = pd.read_csv(productos_file)
    
    # Verificar y cargar los datos correctamente
    print("Iniciando el procesamiento de los datos de ventas...")
    print_before_processing('ventas.csv', df_ventas)
    print_before_processing('productos.csv', df_productos)
    
    # Combinar los datos basados en productoID
    df_combinado = df_ventas.merge(df_productos, on='productoID', how='inner')
    
    # Procesar los datos combinados
    df_limpio = limpiar_datos(df_combinado)
    df_filtrado = calcular_cuartil_superior(df_limpio)
    
    # Verificar y cargar los datos correctamente
    print_after_processing('procesado.csv', df_filtrado)
    
    # Convertir a JSON
    resultado = df_filtrado.to_dict(orient='records')
    json_output = json.dumps(resultado, indent=4)
    
    # Guardar el JSON
    with open(output_file, 'w') as f:
        f.write(json_output)
    
    print(f"\nDatos procesados guardados en {output_file}")

# Ejecutar el procesamiento
procesar_datos('ventas.csv', 'productos.csv', 'procesado.json')