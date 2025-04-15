import json

def calcular_presupuesto(archivo_json):
    with open(archivo_json, 'r') as file:
        data = json.load(file)
    
    ingresos_totales = sum(data['Ingresos'].values())
    gastos_totales = sum(data['Gastos'].values())
    ahorros_netos = ingresos_totales - gastos_totales
    
    print(f"Ingreso Total: ${ingresos_totales}")
    print(f"Gastos Totales: ${gastos_totales}")
    print(f"Ahorros Netos: ${ahorros_netos}")

# Ejemplo de uso
calcular_presupuesto('presupuesto.json')