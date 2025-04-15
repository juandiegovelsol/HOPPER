import pandas as pd
import json

# Función para cargar el JSON desde un archivo
def load_json_from_file(file_path):
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

# Función para procesar los casos de fraude y generar el informe
def process_fraud_cases(json_data):
    if not json_data or 'fraud_cases' not in json_data:
        print("Error: El JSON no contiene la clave 'fraud_cases'.")
        return None

    # Convertir la lista de diccionarios en un DataFrame
    df = pd.DataFrame(json_data['fraud_cases'])

    # Agrupar por 'fraud_type' y sumar 'transaction_amount'
    fraud_report = df.groupby('fraud_type')['transaction_amount'].sum().reset_index()

    return fraud_report

# Ruta al archivo JSON
file_path = 'fraud_cases.json'

# Cargar y procesar los datos
json_data = load_json_from_file(file_path)
fraud_report = process_fraud_cases(json_data)

# Mostrar el informe resultante
if fraud_report is not None:
    print(fraud_report)
