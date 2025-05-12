import json
import pandas as pd

# Función para leer un archivo JSON
def leer_archivo_json(archivo_json):
    with open(archivo_json, 'r') as file:
        return json.load(file)

# Función para leer un archivo CSV
def leer_archivo_csv(archivo_csv):
    return pd.read_csv(archivo_csv)

# Función para calcular el inventario actual
def calcular_inventario_actual(inventario_anterior, compras):
    resultados = []
    
    for tienda in inventario_anterior:
        store_id = tienda['store_id']
        location = tienda['location']
        productos = tienda['products']
        
        # Convertir el DataFrame de compras a un diccionario
        compras_diccionario = compras.set_index(['store_id', 'product'])['quantity_sold'].to_dict()
        print(compras_diccionario)
        # Calcular el inventario actual
        inventario_actual = {producto: productos[producto] - compras_diccionario.get(producto, 0) for producto in productos}
        
        # Añadir los resultados a la lista
        resultados.append({
            'store_id': store_id,
            'location': location,
            'products': inventario_actual
        })
    
    return resultados

# Función para guardar un archivo JSON
def guardar_archivo_json(archivo_json, datos):
    with open(archivo_json, 'w') as file:
        json.dump(datos, file, indent=4)

# Función principal
def main():
    # Archivos de entrada y salida
    inventario_anterior_json = 'inventario_anterior.json'
    compras_csv = 'compras.csv'
    inventario_actual_json = 'inventario_actual.json'
    
    # Leer los datos de inventario anterior y compras
    inventario_anterior = leer_archivo_json(inventario_anterior_json)
    compras = leer_archivo_csv(compras_csv)
    
    # Calcular el inventario actual
    inventario_actual = calcular_inventario_actual(inventario_anterior, compras)
    
    # Guardar el inventario actual en un archivo JSON
    guardar_archivo_json(inventario_actual_json, inventario_actual)
    
    print("El inventario actual se ha generado y guardado en 'inventario_actual.json'.")

# Llamar a la función principal
if __name__ == "__main__":
    main()