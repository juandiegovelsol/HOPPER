import json
import pandas as pd

# Función para calcular el inventario actual
def calculate_current_inventory(inventory_data, purchase_data):
    # Convertir el inventario anterior a un diccionario
    inventory_dict = {item['store_id']: item['products'] for item in inventory_data}
    
    # Convertir el conjunto de datos de compras a un DataFrame
    purchase_df = pd.read_csv(purchase_data)
    
    # Calcular la cantidad de ventas por producto en cada tienda
    purchase_df['total_sold'] = purchase_df['quantity_sold'].sum(axis=1)
    
    # Crear un diccionario para almacenar la cantidad actual de productos en stock
    current_inventory = {}
    
    # Iterar sobre cada tienda
    for store_id, row in purchase_df.groupby('store_id'):
        # Obtener el inventario anterior para esta tienda
        store_inventory = inventory_dict.get(store_id, {})
        
        # Actualizar la cantidad de productos en stock
        current_inventory[store_id] = {
            'location': row['location'].iloc[0],
            'products': {
                product: store_inventory.get(product, 0) - row[product].values[0]
                for product in store_inventory
            }
        }
    
    return current_inventory

# Función para guardar el inventario actual en un archivo JSON
def save_inventory_to_json(inventory_data, file_path):
    with open(file_path, 'w') as file:
        json.dump(inventory_data, file, indent=4)

# Datos de entrada de ejemplo
inventory_file = 'inventory_previous_day.json'
purchase_file = 'purchase_data.csv'
output_file = 'inventory_current_day.json'

# Cargar el inventario anterior
with open(inventory_file, 'r') as file:
    inventory_data = json.load(file)

# Calcular el inventario actual
current_inventory = calculate_current_inventory(inventory_data, purchase_file)

# Guardar el inventario actual en un archivo JSON
save_inventory_to_json(current_inventory, output_file)

print(f"El inventario actual se ha guardado en {output_file}")