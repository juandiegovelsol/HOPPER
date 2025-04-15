import json
import csv
from collections import defaultdict

# Función para cargar datos desde un archivo JSON
def load_json_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Función para cargar datos desde un archivo CSV
def load_csv_data(file_path):
    data = defaultdict(lambda: defaultdict(int))
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            store_id = row['store_id']
            product = row['product']
            quantity_sold = int(row['quantity_sold'])
            data[store_id][product] += quantity_sold
    return data

# Función para calcular el inventario actualizado
def calculate_updated_inventory(previous_inventory, sales_data):
    updated_inventory = []
    for store in previous_inventory:
        store_id = store['store_id']
        location = store['location']
        products = store['products']
        current_inventory = {product: products[product] - sales_data.get(store_id, {}).get(product, 0) for product in products}
        updated_inventory.append({
            "store_id": store_id,
            "location": location,
            "products": current_inventory
        })
    return updated_inventory

# Función para guardar datos en un archivo JSON
def save_json_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Caminos de los archivos de entrada y salida
inventory_file_path = 'previous_inventory.json'
sales_file_path = 'sales.csv'
output_file_path = 'updated_inventory.json'

# Cargar datos
previous_inventory = load_json_data(inventory_file_path)
sales_data = load_csv_data(sales_file_path)
print(sales_data)
# Calcular inventario actualizado
updated_inventory = calculate_updated_inventory(previous_inventory, sales_data)

# Guardar resultados
save_json_data(output_file_path, updated_inventory)

print(f"El archivo de inventario actualizado se ha guardado en {output_file_path}")