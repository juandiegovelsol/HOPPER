import json

def calcular_presupuesto(json_file):
    # Leer el archivo JSON
    with open(json_file, 'r') as file:
        presupuesto = json.load(file)

    # Calcular ingresos totales
    ingresos_totales = sum(presupuesto["Ingresos"].values())
    print(f"Ingreso Total: ${ingresos_totales}")

    # Calcular gastos totales
    gastos_totales = sum(presupuesto["Gastos"].values())
    print(f"Gastos Totales: ${gastos_totales}")

    # Calcular ahorros netos
    ahorros_netos = ingresos_totales - gastos_totales
    print(f"Ahorros Netos: ${ahorros_netos}")

# Ejemplo de uso
calcular_presupuesto('presupuesto.json')

import csv

def json_a_csv_presupuesto(json_file, csv_file):
    # Leer el archivo JSON
    with open(json_file, 'r') as file:
        presupuesto = json.load(file)

    # Escribir los datos en un archivo CSV
    with open(csv_file, 'w', newline='') as csvfile:
        fieldnames = ["Categoría", "Tipo", "Cantidad"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Escribir la cabecera
        writer.writeheader()

        # Escribir los ingresos
        for categoria, valor in presupuesto["Ingresos"].items():
            writer.writerow({"Categoría": categoria, "Tipo": "Ingresos", "Cantidad": valor})

        # Escribir los gastos
        for categoria, valor in presupuesto["Gastos"].items():
            writer.writerow({"Categoría": categoria, "Tipo": "Gastos", "Cantidad": valor})

# Ejemplo de uso
json_a_csv_presupuesto('presupuesto.json', 'presupuesto.csv')