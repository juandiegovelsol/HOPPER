import json
import csv

def read_inventory(json_file):
    with open(json_file, 'r') as file:
        return json.load(file)

def read_sales(csv_file):
    sales_dict = {}
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            store_id = row['store_id']
            product = row['product']
            quantity_sold = int(row['quantity_sold'])
            if store_id not in sales_dict:
                sales_dict[store_id] = {}
            if product not in sales_dict[store_id]:
                sales_dict[store_id][product] = 0
            sales_dict[store_id][product] += quantity_sold
    return sales_dict

def update_inventory(inventory, sales_dict):
    updated_inventory = []
    for store in inventory:
        store_id = store['store_id']
        location = store['location']
        products = store['products']
        updated_products = {}
        
        for product, quantity in products.items():
            if store_id in sales_dict and product in sales_dict[store_id]:
                updated_products[product] = quantity - sales_dict[store_id][product]
            else:
                updated_products[product] = quantity
        
        updated_inventory.append({
            "store_id": store_id,
            "location": location,
            "products": updated_products
        })
    
    return updated_inventory

def write_inventory(inventory, json_file):
    with open(json_file, 'w') as file:
        json.dump(inventory, file, indent=4)

# Ejemplo de uso
inventory_file = 'inventory_day_before.json'
sales_file = 'sales.csv'
output_file = 'inventory_day_today.json'

# Leer datos de inventario del día anterior
inventory = read_inventory(inventory_file)

# Leer datos de ventas del día
sales_dict = read_sales(sales_file)

# Actualizar inventario para el día actual
updated_inventory = update_inventory(inventory, sales_dict)

# Escribir datos de inventario del día actual en un archivo JSON
write_inventory(updated_inventory, output_file)

print(f"El inventario actualizado se ha guardado en {output_file}")