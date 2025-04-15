import pandas as pd
import json
from pycountry import Country

def calculate_monthly_carbon_emissions(csv_file):
    """
    Calcula las emisiones totales de carbono mensuales por continente a partir de los datos diarios de emisiones de carbono para cada país.

    Parámetros:
    csv_file (str): Ruta al archivo CSV con los datos de emisiones de carbono.

    Retorna:
    dict: Un diccionario con los datos de emisiones mensuales por continente.
    """
    try:
        # Cargar los datos del CSV
        df = pd.read_csv(csv_file)

        # Verificar si los datos están en el formato correcto
        if 'Date' not in df.columns or 'Country' not in df.columns or 'Carbon Emission (ktCO2)' not in df.columns:
            raise ValueError("El archivo CSV debe contener las columnas 'Date', 'Country' y 'Carbon Emission (ktCO2)'.")

        # Verificar que el tipo de datos sea correcto
        if not all(df['Date'].dtype == 'datetime64[ns]'):
            raise ValueError("La columna 'Date' debe contener datos de tipo datetime.")
        if not all(df['Country'].dtype == 'object'):
            raise ValueError("La columna 'Country' debe contener datos de tipo objeto.")
        if not all(df['Carbon Emission (ktCO2)'].dtype == 'float64'):
            raise ValueError("La columna 'Carbon Emission (ktCO2)' debe contener datos de tipo float.")

        # Convertir la columna 'Date' a formato datetime
        df['Date'] = pd.to_datetime(df['Date'])

        # Convertir la columna 'Country' a un objeto Country de pycountry
        df['Country'] = df['Country'].apply(lambda x: Country(x))

        # Agrupar los datos por continente y mes
        monthly_emissions = df.groupby([df['Date'].dt.month, df['Country'].name]).sum().reset_index()

        # Renombrar las columnas para facilitar el uso
        monthly_emissions.columns = ['Month', 'Continent', 'Total Carbon Emission (ktCO2)']

        # Convertir los datos a un diccionario
        monthly_emissions_dict = monthly_emissions.set_index('Month').to_dict('index')

        return monthly_emissions_dict

    except FileNotFoundError:
        print(f"Error: El archivo '{csv_file}' no se encontró.")
        return None
    except ValueError as e:
        print(f"Error de formato: {e}")
        return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None

# Ejemplo de uso
csv_file = 'carbon_emissions_data.csv'
monthly_carbon_emissions = calculate_monthly_carbon_emissions(csv_file)

if monthly_carbon_emissions:
    # Mostrar el diccionario resultante
    print(json.dumps(monthly_carbon_emissions, indent=4))