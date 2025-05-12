import pandas as pd
import json

def leer_json_a_dataframe(archivo_json):
    """
    Lee un archivo JSON y lo convierte en un DataFrame de Pandas.

    Parámetros:
    archivo_json (str): Ruta del archivo JSON que contiene los datos.

    Retorna:
    DataFrame de Pandas: DataFrame con los datos leídos del archivo JSON.
    """
    try:
        # Abrir y cargar el archivo JSON
        with open(archivo_json, 'r') as file:
            datos = json.load(file)

        # Verificar si los datos son un diccionario
        if not isinstance(datos, dict):
            raise ValueError("El archivo JSON no contiene un diccionario.")

        # Crear un DataFrame a partir de los datos del diccionario
        df = pd.DataFrame(datos)

        # Verificar si el DataFrame está vacío
        if df.empty:
            raise ValueError("El DataFrame está vacío.")

        return df

    except FileNotFoundError:
        print(f"Error: El archivo {archivo_json} no fue encontrado.")
    except json.JSONDecodeError:
        print(f"Error: El archivo {archivo_json} no es un JSON válido.")
    except ValueError as ve:
        print(f"Error de valor: {ve}")
    except Exception as e:
        print(f"Error inesperado: {e}")

def calcular_tendencia_consumo(df):
    """
    Calcula la tendencia de consumo para cada tipo de servicio solicitado.

    Parámetros:
    df (DataFrame de Pandas): DataFrame que contiene los datos de las interacciones.

    Retorna:
    DataFrame de Pandas: DataFrame con una nueva columna 'tendencia_consumo' que indica la frecuencia de cada tipo de servicio.
    """
    df['tendencia_consumo'] = df['servicios_solicitados'].apply(lambda x: len(x))
    return df

def main():
    # Ruta al archivo JSON que contiene los datos de las interacciones
    archivo_json = 'interacciones_clientes.json'

    try:
        # Leer los datos del archivo JSON
        df = leer_json_a_dataframe(archivo_json)

        # Calcular la tendencia de consumo
        df = calcular_tendencia_consumo(df)

        # Mostrar el DataFrame resultante
        print(df)

    except Exception as e:
        print(f"Error en el proceso principal: {e}")

if __name__ == "__main__":
    main()