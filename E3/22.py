import json
import csv

def json_a_csv(json_file, csv_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Categoría", "Tipo", "Cantidad"])
        
        # Ingresos
        for categoria, cantidad in data['Ingresos'].items():
            writer.writerow(["Ingresos", categoria, cantidad])
        
        # Gastos
        for categoria, cantidad in data['Gastos'].items():
            writer.writerow(["Gastos", categoria, cantidad])
        
        # Contribuciones de los miembros
        for miembro in data['Miembros']:
            writer.writerow(["Contribuciones", miembro['Nombre'], miembro['Contribución']])

# Ejemplo de uso
json_a_csv('presupuesto.json', 'presupuesto.csv')