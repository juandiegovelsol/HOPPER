import json

def calcular_presupuesto(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    ingresos_totales = sum(data['Ingresos'].values())
    gastos_totales = sum(data['Gastos'].values())
    ahorros_netos = ingresos_totales - gastos_totales
    
    print(f"Ingreso Total: ${ingresos_totales}")
    print(f"Gastos Totales: ${gastos_totales}")
    print(f"Ahorros Netos: ${ahorros_netos}")

    return data

# Ejemplo de uso
data = calcular_presupuesto('presupuesto.json')