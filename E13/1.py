import json
import csv

def leer_inventario_json(archivo_inventario):
    """Lee el archivo JSON del inventario del día anterior."""
    with open(archivo_inventario, 'r') as f_json:
        return json.load(f_json)

def leer_compras_csv(archivo_compras):
    """Lee el archivo CSV de las ventas realizadas."""
    compras = {}
    with open(archivo_compras, 'r') as f_csv:
        lector_csv = csv.DictReader(f_csv)
        for fila in lector_csv:
            store_id = fila['store_id']
            product = fila['product']
            quantity_sold = int(fila['quantity_sold'])
            
            if store_id not in compras:
                compras[store_id] = {}
            
            if product not in compras[store_id]:
                compras[store_id][product] = 0
            
            compras[store_id][product] += quantity_sold
    
    return compras

def calcular_inventario_actual(inventario_json, compras):
    """Calcula el inventario actual después de las ventas."""
    inventario_actual = []
    
    for store_entry in inventario_json:
        store_id = store_entry['store_id']
        location = store_entry['location']
        products = store_entry['products']
        
        # Inicializa el inventario actual con los valores del día anterior
        actual_inventario = products.copy()
        
        # Resta las ventas realizadas para cada producto
        for product, quantity_sold in compras.get(store_id, {}).items():
            if product in actual_inventario:
                actual_inventario[product] -= quantity_sold
        
        # Agrega el inventario actual a la lista
        inventario_actual.append({
            "store_id": store_id,
            "location": location,
            "products": actual_inventario
        })
    
    return inventario_actual

def guardar_inventario_json(inventario_actual, archivo_salida):
    """Guarda el inventario actual en un archivo JSON."""
    with open(archivo_salida, 'w') as f_json:
        json.dump(inventario_actual, f_json, indent=4)

# Ejecución del proceso
archivo_inventario = 'inventario_dia_anterior.json'
archivo_compras = 'compras_dia_hoy.csv'
archivo_salida = 'inventario_dia_hoy.json'

inventario_json = leer_inventario_json(archivo_inventario)
compras = leer_compras_csv(archivo_compras)
inventario_actual = calcular_inventario_actual(inventario_json, compras)
guardar_inventario_json(inventario_actual, archivo_salida)

print("El inventario actual ha sido generado y guardado en 'inventario_dia_hoy.json'.")