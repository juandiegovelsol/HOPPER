import csv
import json
from pycountry import Country

def load_data_from_csv(csv_file):
    """
    Carga los datos de emisiones de carbono desde un archivo CSV.
    
    Parámetros:
    csv_file (str): Ruta al archivo CSV que contiene los datos de emisiones.
    
    Retorna:
    list: Lista de diccionarios con los datos de emisiones para cada día.
    """
    data = []
    try:
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: El archivo '{csv_file}' no se encontró.")
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
    return data

def get_continent(country):
    """
    Determina el continente del país a partir de su nombre.
    
    Parámetros:
    country (str): Nombre del país.
    
    Retorna:
    str: Nombre del continente (por ejemplo, "North America", "Europe").
    """
    try:
        country_obj = Country(country)
        return country_obj.name
    except ValueError:
        print(f"Error: No se pudo determinar el continente para el país '{country}'.")
        return None

def aggregate_carbon_emissions(data):
    """
    Agrega las emisiones de carbono mensuales por continente.
    
    Parámetros:
    data (list): Lista de diccionarios con los datos de emisiones para cada día.
    
    Retorna:
    dict: Diccionario con las emisiones totales de carbono por continente y mes.
    """
    monthly_emissions = {}
    for row in data:
        date = row['Date']
        country = row['Country']
        carbon_emission = float(row['Carbon Emission (ktCO2)'])
        continent = get_continent(country)
        
        if continent:
            try:
                month, year = date.split('-')
                key = f"{month} {year}"
                if key not in monthly_emissions:
                    monthly_emissions[key] = {continent: 0}
                monthly_emissions[key][continent] += carbon_emission
            except ValueError:
                print(f"Error: Formato de fecha inválido para el país '{country}' en la fecha '{date}'.")
    return monthly_emissions

def save_to_json(data, json_file):
    """
    Guarda los datos de emisiones de carbono en un archivo JSON.
    
    Parámetros:
    data (dict): Diccionario con las emisiones totales de carbono por continente y mes.
    json_file (str): Ruta al archivo JSON donde se guardarán los datos.
    """
    try:
        with open(json_file, mode='w') as file:
            json.dump(data, file, indent=4)
        print(f"Datos guardados exitosamente en '{json_file}'.")
    except Exception as e:
        print(f"Error al guardar el archivo JSON: {e}")

def main():
    """
    Función principal que ejecuta el proceso de carga, agregación y guardado de datos de emisiones de carbono.
    """
    csv_file = 'carbon_emissions.csv'
    json_file = 'carbon_emissions_monthly.json'
    
    data = load_data_from_csv(csv_file)
    if not data:
        return
    
    monthly_emissions = aggregate_carbon_emissions(data)
    if monthly_emissions:
        save_to_json(monthly_emissions, json_file)
    else:
        print("No se pudieron procesar los datos.")

if __name__ == "__main__":
    main()
