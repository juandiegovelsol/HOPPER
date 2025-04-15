import json
import pandas as pd

# Función para cargar el archivo JSON
def load_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no se encontró.")
        return None
    except json.JSONDecodeError:
        print(f"Error: El archivo {file_path} no contiene un JSON válido.")
        return None

# Función para convertir el JSON en un DataFrame de Pandas
def json_to_dataframe(data):
    try:
        if not data:
            print("Error: No se encontró datos en el archivo JSON.")
            return None
        
        df = pd.DataFrame(data['fraud_cases'])
        return df
    except KeyError as e:
        print(f"Error: La clave '{e}' no se encuentra en el JSON.")
        return None
    except Exception as e:
        print(f"Error al convertir el JSON en un DataFrame: {e}")
        return None

# Función para agrupar los casos de fraude por tipo y sumar la cantidad de dinero involucrada
def aggregate_fraud_data(df):
    try:
        if df is None:
            print("Error: No se pudo convertir el JSON en un DataFrame.")
            return None
        
        aggregated_data = df.groupby('fraud_type')['transaction_amount'].sum().reset_index()
        return aggregated_data
    except KeyError as e:
        print(f"Error: La columna '{e}' no se encuentra en el DataFrame.")
        return None
    except Exception as e:
        print(f"Error al agrupar los casos de fraude: {e}")
        return None

# Función principal para ejecutar el procesamiento
def main():
    # Ruta al archivo JSON
    json_file_path = 'fraud_cases.json'
    
    # Cargar el archivo JSON
    data = load_json_file(json_file_path)
    
    # Convertir el JSON en un DataFrame de Pandas
    df = json_to_dataframe(data)
    
    # Agrupar los casos de fraude por tipo y sumar la cantidad de dinero involucrada
    aggregated_data = aggregate_fraud_data(df)
    
    # Mostrar el resultado
    if aggregated_data is not None:
        print(aggregated_data)

# Ejecutar la función principal
if __name__ == "__main__":
    main()