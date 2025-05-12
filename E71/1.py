#681e0e3c23182802e0d81ab3

import json

def calcular_presupuesto(datos):
    ingresos_totales = sum(datos["Ingresos"].values())
    gastos_totales = sum(datos["Gastos"].values())
    ahorros_netos = ingresos_totales - gastos_totales
    
    return {
        "Ingreso Total": ingresos_totales,
        "Gastos Totales": gastos_totales,
        "Ahorros Netos": ahorros_netos
    }

def main():
    # Datos en formato JSON
    datos_json = '''
    {
      "Ingresos": {
        "Salario": 3000,
        "Freelance": 500
      },
      "Gastos": {
        "Alquiler": 1200,
        "Comestibles": 300,
        "Servicios": 200,
        "Entretenimiento": 100
      }
    }
    '''

    # Leer datos JSON
    datos = json.loads(datos_json)
    
    # Calcular el presupuesto
    presupuesto = calcular_presupuesto(datos)

    # Imprimir resultados
    print(f"Ingreso Total: ${presupuesto['Ingreso Total']:.2f}")
    print(f"Gastos Totales: ${presupuesto['Gastos Totales']:.2f}")
    print(f"Ahorros Netos: ${presupuesto['Ahorros Netos']:.2f}")

if __name__ == "__main__":
    main()


import json
import csv

def json_a_csv(datos_json, archivo_csv):
    # Leer datos JSON
    datos = json.loads(datos_json)
    
    # Escribir datos en formato CSV
    with open(archivo_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Categoría", "Tipo", "Cantidad"])
        
        # Escribir ingresos
        for categoria, cantidad in datos["Ingresos"].items():
            writer.writerow([categoria, "Ingresos", cantidad])
        
        # Escribir gastos
        for categoria, cantidad in datos["Gastos"].items():
            writer.writerow([categoria, "Gastos", cantidad])

# Ejemplo: convertir el JSON a CSV
datos_json = '''
{
  "Ingresos": {
    "Salario": 3000,
    "Freelance": 500
  },
  "Gastos": {
    "Alquiler": 1200,
    "Comestibles": 300,
    "Servicios": 200,
    "Entretenimiento": 100
  }
}
'''

archivo_csv = "presupuesto.csv"
json_a_csv(datos_json, archivo_csv)