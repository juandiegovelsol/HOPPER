import json
import csv
from collections import defaultdict

# Función para cargar datos desde un archivo JSON
def load_json_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Función para cargar datos desde un archivo CSV
def load_csv_data(file_path):
    data = defaultdict(lambda: defaultdict(int))  # Diccionario donde cada tienda tiene otro diccionario por producto
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            store_id = row['store_id']
            product = row['product']
            quantity_sold = int(row['quantity_sold'])
            data[store_id][product] += quantity_sold
    return data

# Función para calcular el inventario actual
def calculate_current_inventory(inventory_data, sales_data):
    print(inventory_data)
    current_inventory = []
    for store_id, products in inventory_data.items():
        store_data = {
            "store_id": store_id,
            "location": "Downtown",
            "products": {}
        }
        for product, quantity in products.items():
            current_quantity = quantity - sales_data.get(store_id, {}).get(product, 0)
            store_data["products"][product] = current_quantity
        current_inventory.append(store_data)
    return current_inventory

# Función para guardar datos en un archivo JSON
def save_json_data(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Ejemplo de uso
if __name__ == "__main__":
    # Cargar datos del inventario del día anterior
    inventory_data = load_json_data('inventory_data_previous_day.json')
    
    # Cargar datos de compras del día actual
    sales_data = load_csv_data('sales_data_today.csv')
    
    # Calcular el inventario actual
    current_inventory = calculate_current_inventory(inventory_data, sales_data)
    
    # Guardar el inventario actual en un archivo JSON
    save_json_data(current_inventory, 'inventory_data_today.json')

    print("El inventario actual se ha generado correctamente.")