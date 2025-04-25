import pandas as pd
import json
from pycountry import Country

def procesar_datos_emisiones(csv_file, json_file):
    try:
        # Cargar los datos desde un archivo CSV
        df = pd.read_csv(csv_file)
        
        # Validar que las columnas necesarias estén presentes
        required_columns = ['Date', 'Country', 'Carbon Emission (ktCO2)']
        if not all(column in df.columns for column in required_columns):
            raise ValueError(f"Faltan una o más columnas necesarias en el archivo CSV: {required_columns}")
        
        # Convertir la columna 'Date' a formato datetime
        df['Date'] = pd.to_datetime(df['Date'])
        
        # Agrupar por mes y continente
        grouped_data = df.groupby([df['Date'].dt.to_period('M'), df['Country']])['Carbon Emission (ktCO2)'].sum().unstack()
        
        # Renombrar las columnas para que representen los continentes
        grouped_data.columns = [country.name for country in df['Country'].nunique().unique()]
        
        # Renombrar el índice para que represente los meses
        grouped_data.index = grouped_data.index.to_period('M').strftime('%B %Y')
        
        # Crear un diccionario para almacenar los resultados por continente
        results = {}
        for month, continent_emissions in grouped_data.items():
            results[month] = {continent: emissions for continent, emissions in continent_emissions.items()}
        
        # Guardar los resultados en un archivo JSON
        with open(json_file, 'w') as f:
            json.dump(results, f, indent=4)
        
        print(f"Los datos han sido procesados y guardados en {json_file}")
    
    except FileNotFoundError:
        print(f"Error: El archivo {csv_file} no se encontró.")
    except ValueError as ve:
        print(f"Error de validación: {ve}")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")

# Ejemplo de uso
procesar_datos_emisiones('carbon_emissions.csv', 'monthly_carbon_emissions_by_continent.json')