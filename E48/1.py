import pandas as pd
import json

# Función para leer el archivo JSON como DataFrame de Pandas
def leer_json_a_df(archivo_json):
    try:
        # Intentar cargar el archivo JSON en un diccionario
        with open(archivo_json, 'r') as f:
            data = json.load(f)

        # Verificar si el diccionario contiene una lista de clientes
        if not isinstance(data, list):
            raise ValueError("El archivo JSON debe contener una lista de clientes.")

        # Convertir la lista de diccionarios en un DataFrame
        df = pd.DataFrame(data)

        # Verificar si el DataFrame tiene las columnas necesarias
        columnas_requeridas = ['cliente1', 'nombre', 'apellido', 'edad', 'servicios_solicitados', 'canal_de_atencion', 'nivel_satisfaccion']
        if not all(col in df.columns for col in columnas_requeridas):
            raise ValueError(f"El DataFrame debe contener las siguientes columnas: {columnas_requeridas}")

        return df

    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_json}' no se encontró.")
        return None
    except json.JSONDecodeError:
        print(f"Error: El archivo '{archivo_json}' no contiene un JSON válido.")
        return None
    except Exception as e:
        print(f"Error inesperado al leer el archivo JSON: {e}")
        return None

# Función para calcular la tendencia de consumo
def calcular_tendencia_consumo(df):
    # Crear una columna para contar la frecuencia de cada servicio solicitado
    df['frecuencia_servicios'] = df['servicios_solicitados'].apply(len)

    # Crear una columna para calcular la tendencia de consumo (media de la frecuencia)
    df['tendencia_consumo'] = df['frecuencia_servicios'].mean()

    return df

# Función principal
def main(archivo_json):
    # Leer el archivo JSON a un DataFrame
    df = leer_json_a_df(archivo_json)

    if df is not None:
        # Calcular la tendencia de consumo
        df = calcular_tendencia_consumo(df)

        # Imprimir el DataFrame con la nueva columna 'tendencia_consumo'
        print(df)

# Ejemplo de uso
archivo_json = 'interacciones_clientes.json'
main(archivo_json)