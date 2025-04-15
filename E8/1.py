import pandas as pd
import json
from pycountry import countries

def load_data(file_path):
    """
    Carga los datos de emisiones de carbono desde un archivo CSV.
    
    Parámetros:
    file_path (str): La ruta al archivo CSV que contiene los datos.
    
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
        print(f"Error: No se pudo parsear el archivo {file_path}. Verifica su formato.")
    return None

def get_continent(country_name):
    """
    Obtiene el nombre del continente para un país dado.
    
    Parámetros:
    country_name (str): El nombre del país.
    
    Devuelve:
    str: El nombre del continente, o 'Unknown' si el país no se encuentra.
    """
    try:
        country = countries.get(name=country_name)
        return country.continent.name
    except KeyError:
        return "Unknown"

def aggregate_emissions_by_continent(df):
    """
    Agrupa las emisiones de carbono por continente y mes, y calcula el total mensual.
    
    Parámetros:
    df (pd.DataFrame): El DataFrame que contiene los datos de emisiones diarias.
    
    Devuelve:
    dict: Un diccionario con las emisiones totales mensuales por continente.
    """
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.strftime('%B %Y')
    df['Continent'] = df['Country'].apply(get_continent)
    
    monthly_emissions = df.groupby(['Month', 'Continent'])['Carbon Emission (ktCO2)'].sum().unstack(fill_value=0)
    return monthly_emissions.to_dict(orient='index')

def save_to_json(data, output_file):
    """
    Guarda los datos agregados en un archivo JSON.
    
    Parámetros:
    data (dict): Los datos a guardar, en formato de diccionario.
    output_file (str): La ruta del archivo JSON de salida.
    """
    try:
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Datos guardados exitosamente en {output_file}")
    except IOError as e:
        print(f"Error al guardar el archivo JSON: {e}")

def main():
    """
    Función principal que orquesta la carga de datos, agrupación y guardado de resultados.
    """
    file_path = 'carbon_emissions.csv'
    output_file = 'monthly_emissions_by_continent.json'
    
    df = load_data(file_path)
    if df is not None:
        aggregated_data = aggregate_emissions_by_continent(df)
        save_to_json(aggregated_data, output_file)

if __name__ == "__main__":
    main()