import pandas as pd
import json

def leer_json_a_dataframe(archivo_json):
    """
    Lee un archivo JSON y lo convierte en un DataFrame de Pandas.

    Parámetros:
    archivo_json (str): Ruta al archivo JSON a leer.

    Retorna:
    pd.DataFrame: DataFrame con los datos del archivo JSON.

    Lanza:
    FileNotFoundError: Si el archivo JSON no se encuentra.
    ValueError: Si el archivo JSON no contiene datos válidos.
    """
    try:
        # Intenta abrir el archivo JSON
        with open(archivo_json, 'r') as file:
            datos = json.load(file)
    except FileNotFoundError:
        # Maneja el caso en que el archivo no se encuentra
        print(f"Error: El archivo '{archivo_json}' no se encontró.")
        return None
    except json.JSONDecodeError:
        # Maneja el caso en que el archivo no contiene JSON válido
        print(f"Error: El archivo '{archivo_json}' no contiene un JSON válido.")
        return None

    # Verifica que los datos sean un diccionario
    if not isinstance(datos, dict):
        print(f"Error: El archivo '{archivo_json}' no contiene un diccionario válido.")
        return None

    try:
        # Convierte el diccionario a un DataFrame
        df = pd.DataFrame(datos)
    except KeyError as e:
        # Maneja el caso en que faltan claves esperadas en los datos
        print(f"Error: Falta la clave esperada '{e}' en los datos del archivo JSON.")
        return None

    # Verifica si el DataFrame está vacío
    if df.empty:
        print("Error: El DataFrame está vacío después de leer el archivo JSON.")
        return None
    print(df['servicios_solicitados'])
    # Crea la variable 'tendencia_consumo' basándose en la frecuencia de cada tipo de servicio solicitado
    df['tendencia_consumo'] = df['servicios_solicitados'].apply(lambda x: x.count() if isinstance(x, set) else 0)

    return df

# Ejemplo de uso
archivo_json = 'interacciones_canal_digital.json'
df = leer_json_a_dataframe(archivo_json)

if df is not None:
    # Imprime el DataFrame con la nueva variable 'tendencia_consumo'
    print(df)