import json
import csv

def json_a_csv_presupuesto(archivo_json, archivo_csv):
    with open(archivo_json, 'r') as file:
        data = json.load(file)
    
    # Definir las columnas
    columnas = ['Categoría', 'Tipo', 'Cantidad']
    
    with open(archivo_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columnas)
        
        # Escribir ingresos
        for categoria, cantidad in data['Ingresos'].items():
            writer.writerow([categoria, 'Ingresos', cantidad])
        
        # Escribir gastos
        for categoria, cantidad in data['Gastos'].items():
            writer.writerow([categoria, 'Gastos', cantidad])
        
        # Escribir contribuciones de miembros
        for miembro in data['Miembros']:
            writer.writerow([miembro['Nombre'], 'Contribución', miembro['Contribución']])

# Ejemplo de uso
json_a_csv_presupuesto('presupuesto.json', 'presupuesto.csv')