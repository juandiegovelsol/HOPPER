import pandas as pd
import pycountry
import json
from datetime import datetime

def load_csv_data(file_path):
    """
    Carga los datos de emisiones de carbono desde un archivo CSV.
    
    Args:
        file_path (str): Ruta al archivo CSV.
    
    Returns:
        pd.DataFrame: DataFrame con los datos cargados.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no se encontró.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: El archivo CSV está vacío.")
        return None
    except pd.errors.ParserError:
        print("Error: Error al analizar el archivo CSV.")
        return None

def determine_continent(country_name):
    """
    Determina el continente de un país a partir de su nombre.
    
    Args:
        country_name (str): Nombre del país.
    
    Returns:
        str: Nombre del continente.
    """
    try:
        country = pycountry.Country(country_name)
        return country.continent
    except pycountry.LookupError:
        print(f"Error: No se pudo encontrar el país '{country_name}'.")
        return None

def aggregate_monthly_data(df):
    """
    Agrupa los datos de emisiones de carbono mensuales por continente.
    
    Args:
        df (pd.DataFrame): DataFrame con los datos de emisiones diarias.
    
    Returns:
        dict: Diccionario con los datos agregados por continente y mes.
    """
    aggregated_data = {}
    for _, row in df.iterrows():
        try:
            date = datetime.strptime(row['Date'], '%Y-%m-%d')
            month = date.strftime('%B %Y')
            country = row['Country']
            continent = determine_continent(country)
            
            if continent is None:
                continue
            
            if month not in aggregated_data:
                aggregated_data[month] = {}
            
            if continent not in aggregated_data[month]:
                aggregated_data[month][continent] = 0
            
            aggregated_data[month][continent] += row['Carbon Emission (ktCO2)']
        except ValueError as e:
            print(f"Error al procesar la fecha '{row['Date']}': {e}")
        except KeyError as e:
            print(f"Falta la clave '{e}' en la fila {row}")
    
    return aggregated_data

def save_to_json(data, file_path):
    """
    Guarda los datos agregados en un archivo JSON.
    
    Args:
        data (dict): Diccionario con los datos a guardar.
        file_path (str): Ruta al archivo JSON.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Datos guardados exitosamente en {file_path}")
    except IOError as e:
        print(f"Error al escribir en el archivo {file_path}: {e}")

def main():
    # Ruta al archivo CSV
    csv_file_path = 'carbon_emissions.csv'
    
    # Cargar los datos
    df = load_csv_data(csv_file_path)
    if df is None:
        return
    
    # Agrupar los datos mensuales por continente
    aggregated_data = aggregate_monthly_data(df)
    
    # Guardar los datos en un archivo JSON
    json_file_path = 'monthly_carbon_emissions_by_continent.json'
    save_to_json(aggregated_data, json_file_path)

if __name__ == "__main__":
    main()