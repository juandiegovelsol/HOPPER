import json
import csv

# Función para leer el archivo JSON de inventario del día anterior
def read_inventory_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Función para leer el archivo CSV de ventas
def read_sales_csv(file_path):
    sales = {}
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            store_id = row['store_id']
            product = row['product']
            quantity_sold = int(row['quantity_sold'])
            if store_id not in sales:
                sales[store_id] = {}
            if product not in sales[store_id]:
                sales[store_id][product] = 0
            sales[store_id][product] += quantity_sold
    return sales

# Función para calcular el inventario actual
def calculate_current_inventory(inventory, sales):
    current_inventory = []
    for store in inventory:
        store_id = store['store_id']
        location = store['location']
        products = store['products']
        
        # Actualizar el inventario basado en las ventas
        for product, quantity_sold in sales.get(store_id, {}).items():
            if product in products:
                products[product] -= quantity_sold
        
        # Añadir el inventario actualizado a la lista
        current_inventory.append({
            "store_id": store_id,
            "location": location,
            "products": products
        })
    return current_inventory

# Función para escribir el archivo JSON de inventario actual
def write_inventory_json(file_path, inventory):
    with open(file_path, 'w') as file:
        json.dump(inventory, file, indent=4)

# Ruta al archivo JSON de inventario del día anterior
inventory_file_path = 'inventory_day_before.json'

# Ruta al archivo CSV de ventas
sales_file_path = 'sales.csv'

# Leer datos de inventario del día anterior
inventory = read_inventory_json(inventory_file_path)

# Leer datos de ventas
sales = read_sales_csv(sales_file_path)

# Calcular inventario actual
current_inventory = calculate_current_inventory(inventory, sales)

# Escribir inventario actual en archivo JSON
write_inventory_json('inventory_day_today.json', current_inventory)

print("El inventario actual ha sido generado y guardado en 'inventory_day_today.json'.")