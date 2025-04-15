import pandas as pd
import json

def procesar_json_fraudes(archivo_json):
    """
    Procesa un archivo JSON que contiene información de casos de fraude y genera un DataFrame
    con la cantidad monetaria total por tipo de fraude.

    Args:
    archivo_json (str): Ruta al archivo JSON que contiene los casos de fraude.

    Returns:
    pd.DataFrame: DataFrame con la cantidad total de dinero involucrado por tipo de fraude.
    """
    try:
        # Cargar el archivo JSON
        with open(archivo_json, 'r') as file:
            data = json.load(file)

        # Verificar que la clave esperada exista en el JSON
        if 'fraud_cases' not in data:
            raise ValueError("La clave 'fraud_cases' no se encuentra en el archivo JSON.")

        # Convertir la lista de diccionarios en un DataFrame
        df = pd.DataFrame(data['fraud_cases'])

        # Asegurarse de que las columnas necesarias estén presentes
        required_columns = ['fraud_type', 'transaction_amount']
        for column in required_columns:
            if column not in df.columns:
                raise KeyError(f"La columna requerida '{column}' no se encuentra en los datos.")

        # Agrupar por tipo de fraude y sumar la cantidad de la transacción
        df_agrupado = df.groupby('fraud_type')['transaction_amount'].sum().reset_index()

        return df_agrupado

    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_json}' no se encontró.")
    except json.JSONDecodeError:
        print(f"Error: El archivo '{archivo_json}' no contiene un JSON válido.")
    except ValueError as ve:
        print(f"Error de validación: {ve}")
    except KeyError as ke:
        print(f"Error de clave: {ke}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Ejemplo de uso
archivo_json = 'fraud_cases.json'  # Nombre del archivo JSON de entrada
try:
    df_fraudes = procesar_json_fraudes(archivo_json)
    print(df_fraudes)
except Exception as e:
    print(f"Error durante el procesamiento: {e}")