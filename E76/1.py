import pandas as pd
import json
import os

# Función para leer el archivo JSON y convertirlo en un DataFrame de Pandas
def leer_archivo_json_a_dataframe(archivo_json):
    try:
        # Verificar si el archivo existe
        if not os.path.exists(archivo_json):
            raise FileNotFoundError(f"El archivo '{archivo_json}' no se encuentra.")
        
        # Leer el archivo JSON
        with open(archivo_json, 'r') as file:
            datos = json.load(file)
        
        # Verificar si los datos son una lista de diccionarios
        if not isinstance(datos, list):
            raise ValueError("Los datos deben ser una lista de diccionarios.")
        
        # Crear un DataFrame a partir de la lista de diccionarios
        df = pd.DataFrame(datos)
        
        # Verificar si las columnas necesarias existen en el DataFrame
        columnas_requeridas = ['cliente1', 'servicios_solicitados', 'canal_de_atencion']
        for columna in columnas_requeridas:
            if columna not in df.columns:
                raise ValueError(f"La columna '{columna}' no existe en los datos.")
        
        return df
    
    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(e)
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Función para generar la variable 'tendencia_consumo'
def generar_tendencia_consumo(df):
    try:
        # Verificar si la columna 'servicios_solicitados' existe en el DataFrame
        if 'servicios_solicitados' not in df.columns:
            raise ValueError("La columna 'servicios_solicitados' no existe en los datos.")
        
        # Crear una columna 'tendencia_consumo' que indica la frecuencia de cada servicio solicitado
        df['tendencia_consumo'] = df['servicios_solicitados'].apply(lambda x: len(x))
        
        # Convertir la columna 'tendencia_consumo' a un tipo numérico
        df['tendencia_consumo'] = df['tendencia_consumo'].astype(int)
        
        return df
    
    except KeyError as e:
        print(f"Error: La columna {e} no existe en los datos.")
    except Exception as e:
        print(f"Ocurrió un error inesperado al generar la tendencia de consumo: {e}")

# Ejemplo de uso
archivo_json = 'interacciones_chat.json'  # Nombre del archivo JSON con los datos de las interacciones
df = leer_archivo_json_a_dataframe(archivo_json)

if df is not None:
    df_con_tendencia_consumo = generar_tendencia_consumo(df)
    print(df_con_tendencia_consumo)