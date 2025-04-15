import csv
import json

def leer_csv(archivo_csv):
    """
    Lee los datos de un archivo CSV y devuelve una lista de diccionarios.
    """
    datos = []
    with open(archivo_csv, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            datos.append(row)
    return datos

def calcular_asignacion_recursos(datos):
    """
    Calcula la asignación de recursos para cada región y proyecto.
    """
    asignacion = {}
    for entrada in datos:
        region = entrada['región']
        proyecto = entrada['proyecto']
        severity = entrada['problema_severidad']
        necesidad_recursos = int(entrada['necesidad_recursos'])

        if region not in asignacion:
            asignacion[region] = {}
        if proyecto not in asignacion[region]:
            asignacion[region][proyecto] = {
                'issue_severity': severity,
                'necesidad_de_recursos': necesidad_recursos
            }

        # Calcular la necesidad total de recursos para la región
        asignacion[region]['necesidad_de_recursos_totales'] = sum(
            proyecto['necesidad_de_recursos'] for proyecto in asignacion[region].values()
        )

    return asignacion

def generar_json(asignacion, archivo_json):
    """
    Genera un archivo JSON con los resultados.
    """
    with open(archivo_json, mode='w') as file:
        json.dump(asignacion, file, indent=4)

def main():
    """
    Función principal que ejecuta el proceso completo.
    """
    # Archivo CSV de entrada
    archivo_csv = 'datos_recursos.csv'
    # Archivo JSON de salida
    archivo_json = 'asignacion_recursos.json'

    # Leer datos del CSV
    datos = leer_csv(archivo_csv)
    
    # Calcular la asignación de recursos
    asignacion = calcular_asignacion_recursos(datos)
    
    # Generar el JSON con los resultados
    generar_json(asignacion, archivo_json)

    print(f"Datos procesados y guardados en {archivo_json}")

if __name__ == "__main__":
    main()