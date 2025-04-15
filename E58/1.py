import pandas as pd
import json

# Función para cargar un archivo JSON a un DataFrame de Pandas
def cargar_archivo_json_a_dataframe(ruta_archivo):
    """
    Carga un archivo JSON a un DataFrame de Pandas.

    Args:
        ruta_archivo (str): Ruta al archivo JSON.

    Returns:
        pd.DataFrame: DataFrame con los datos del archivo JSON.
    """
    try:
        # Abrir y cargar el archivo JSON
        with open(ruta_archivo, 'r') as archivo:
            datos = json.load(archivo)

        # Crear un DataFrame a partir de los datos JSON
        df = pd.DataFrame(datos)
        print(df)

        # Verificar que el DataFrame tenga las columnas necesarias
        columnas_requeridas = ['cliente1', 'servicios_solicitados', 'canal_de_atencion']
        if not all(columna in df.columns for columna in columnas_requeridas):
            raise ValueError(f"El DataFrame debe contener las columnas: {columnas_requeridas}")

        # Calcular la tendencia de consumo
        df['tendencia_consumo'] = df['servicios_solicitados'].apply(lambda x: len(x))

        return df

    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo}' no se encontró.")
        return None
    except json.JSONDecodeError:
        print(f"Error: El archivo '{ruta_archivo}' no contiene un JSON válido.")
        return None
    except Exception as e:
        print(f"Error inesperado al cargar el archivo JSON: {e}")
        return None

# Ejemplo de uso
ruta_archivo = 'datos_chat.json'
df = cargar_archivo_json_a_dataframe(ruta_archivo)

if df is not None:
    print(df)