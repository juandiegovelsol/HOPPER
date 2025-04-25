import pandas as pd
from pycountry import Country
import json

# Función para convertir la fecha al formato adecuado
def convert_date_to_month(date_str):
    return date_str.split('-')[1]

# Función para cargar los datos desde un archivo CSV
def load_data_from_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no se encontró.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: El archivo {file_path} está vacío.")
        return None
    except pd.errors.ParserError:
        print(f"Error: Hubo un problema al analizar el archivo {file_path}.")
        return None

# Función para agrupar las emisiones mensuales por continente
def aggregate_emissions_by_continent(df):
    try:
        # Convertir la columna de fecha a tipo datetime y extraer el mes
        df['Date'] = pd.to_datetime(df['Date'])
        df['Month'] = df['Date'].dt.strftime('%B %Y')
        
        # Agrupar por mes y continente
        monthly_emissions = df.groupby(['Month', df['Country'].apply(lambda x: Country(x).name)], as_index=False).sum()
        
        # Convertir el continente a clave del diccionario
        monthly_emissions['Continent'] = monthly_emissions['Country'].apply(lambda x: Country(x).continent)
        
        # Reestructurar los datos para tener el formato deseado
        result = monthly_emissions.groupby('Month')['Continent'].apply(lambda x: x.value_counts().to_dict()).to_dict()
        return result
    except KeyError as e:
        print(f"Error: Columna faltante {e} en los datos.")
        return None
    except Exception as e:
        print(f"Error inesperado al agrupar los datos: {e}")
        return None

# Función para guardar los datos en un archivo JSON
def save_to_json(data, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Datos guardados exitosamente en {file_path}")
    except IOError as e:
        print(f"Error al escribir en el archivo {file_path}: {e}")

# Ruta al archivo CSV
csv_file_path = 'carbon_emissions.csv'

# Cargar, agrupar y guardar los datos
df = load_data_from_csv(csv_file_path)
if df is not None:
    monthly_emissions = aggregate_emissions_by_continent(df)
    if monthly_emissions is not None:
        save_to_json(monthly_emissions, 'monthly_carbon_emissions_by_continent.json')