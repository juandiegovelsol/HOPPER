import pandas as pd
import json
from datetime import datetime

def analizar_stock(csv_input, json_output):
    try:
        # Cargar el CSV
        df = pd.read_csv(csv_input)
        
        # Eliminar valores nulos
        df.dropna(inplace=True)
        
        # Convertir columnas a tipos adecuados
        df['stock_sucursal_principal'] = pd.to_numeric(df['stock_sucursal_principal'], errors='coerce')
        df['stock_sucursal_secundaria'] = pd.to_numeric(df['stock_sucursal_secundaria'], errors='coerce')
        df['ventas_periodo_anterior'] = pd.to_numeric(df['ventas_periodo_anterior'], errors='coerce')
        
        # Convertir fecha a formato datetime
        df['fecha_ultimo_abastecimiento'] = pd.to_datetime(df['fecha_ultimo_abastecimiento'], errors='coerce')
        
        # Crear la columna Reabastecer
        df['Reabastecer'] = (
            df['ventas_periodo_anterior'] > df['stock_sucursal_principal'] * 1.5
        )
        print(df)
        
        # Guardar el DataFrame en JSON
        with open(json_output, 'w') as file:
            json.dump(df.to_dict(orient='records'), file, indent=4)
        
        print(f"El archivo JSON '{json_output}' ha sido creado con éxito.")
    
    except FileNotFoundError:
        print(f"Error: El archivo '{csv_input}' no se encontró.")
    except pd.errors.EmptyDataError:
        print("Error: El archivo CSV está vacío.")
    except pd.errors.ParserError:
        print("Error: Hubo un problema al leer el archivo CSV.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Ejemplo de uso
csv_input = 'stock.csv'  # Cambia este nombre al archivo CSV que deseas analizar
json_output = 'analisis_stock.json'  # Cambia este nombre al archivo JSON de salida

# Ejecutar la función
analizar_stock(csv_input, json_output)
