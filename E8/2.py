import pandas as pd
import json
from pycountry import countries

def load_data(file_path):
    """
    Carga los datos del archivo CSV.

    Parámetros:
    file_path (str): La ruta al archivo CSV.

    Devuelve:
    pd.DataFrame: Un DataFrame con los datos cargados, o None si ocurre un error.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no fue encontrado.")
    except pd.errors.EmptyDataError:
        print(f"Error: El archivo {file_path} está vacío.")
    except pd.errors.ParserError:
        print(f"Error: No se pudo parsear el archivo {file_path}. Verifique el formato CSV.")
    return None

def calculate_monthly_emissions(df):
    """
    Calcula las emisiones totales de carbono mensuales por continente.

    Parámetros:
    df (pd.DataFrame): El DataFrame que contiene los datos de emisiones diarias.

    Devuelve:
    dict: Un diccionario con las emisiones mensuales por continente, o None si ocurre un error.
    """
    try:
        # Convertir la columna 'Date' a datetime
        df['Date'] = pd.to_datetime(df['Date'])
        
        # Agrupar por mes y continente, sumando las emisiones
        monthly_emissions = df.groupby([df['Date'].dt.to_period('M'), countries.get(alpha_2=df['Country']).continent])['Carbon Emission (ktCO2)'].sum().unstack(fill_value=0)
        print(df)
        # Renombrar las columnas de los continentes
        monthly_emissions.columns = [continent.name for continent in monthly_emissions.columns]
        
        # Convertir el índice a formato de cadena de texto para el JSON
        monthly_emissions.index = monthly_emissions.index.to_series().astype(str)
        
        return monthly_emissions.to_dict()
    except KeyError as e:
        print(f"Error: Falta la clave {e} en los datos del país.")
    except Exception as e:
        print(f"Error inesperado al calcular las emisiones mensuales: {e}")
    return None

def save_to_json(data, file_path):
    """
    Guarda los datos en un archivo JSON.

    Parámetros:
    data (dict): Los datos a guardar en formato JSON.
    file_path (str): La ruta donde se guardará el archivo JSON.

    Devuelve:
    None
    """
    try:
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Datos guardados exitosamente en {file_path}")
    except Exception as e:
        print(f"Error al guardar los datos en JSON: {e}")

def main():
    """
    Función principal que orquesta la carga de datos, cálculo de emisiones y guardado en JSON.

    Devuelve:
    None
    """
    # Ruta al archivo CSV de entrada
    csv_file_path = 'carbon_emissions.csv'
    
    # Cargar los datos desde el CSV
    df = load_data(csv_file_path)
    if df is None:
        return
    
    # Calcular las emisiones mensuales por continente
    monthly_emissions = calculate_monthly_emissions(df)
    if monthly_emissions is None:
        return
    
    # Ruta al archivo JSON de salida
    json_file_path = 'monthly_emissions_by_continent.json'
    
    # Guardar los resultados en un archivo JSON
    save_to_json(monthly_emissions, json_file_path)

if __name__ == "__main__":
    main()