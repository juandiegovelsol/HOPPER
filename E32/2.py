import json
import pandas as pd

# Función para cargar el archivo JSON
def load_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} is not a valid JSON.")
        return None

# Función para procesar los datos de fraude y generar un DataFrame
def process_fraud_data(fraud_data):
    df = pd.DataFrame(fraud_data['fraud_cases'])
    return df

# Función para agrupar por tipo de fraude y sumar los montos de las transacciones
def group_fraud_by_type(df):
    return df.groupby('fraud_type')['transaction_amount'].sum().reset_index()

# Función principal para ejecutar el proceso
def main():
    # Ruta al archivo JSON
    file_path = 'fraud_cases.json'

    # Cargar los datos desde el archivo JSON
    fraud_data = load_json_file(file_path)
    if fraud_data is None:
        return

    # Procesar los datos de fraude
    df = process_fraud_data(fraud_data)
    if df.empty:
        print("Error: No data to process.")
        return

    # Agrupar por tipo de fraude y sumar los montos
    fraud_summary = group_fraud_by_type(df)

    # Mostrar el resumen
    print(fraud_summary)

# Ejecutar la función principal
if __name__ == "__main__":
    main()