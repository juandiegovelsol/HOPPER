import json
from datetime import datetime, timezone

# Función para validar y procesar los datos del sensor
def procesar_datos_sensor(datos_sensores):
    resultados = {}
    errores = []

    # Validación de los datos del sensor
    for timestamp, sensores in datos_sensores.items():
        for id_sensor, valor in sensores.items():
            if not isinstance(valor, (int, float)) or valor <= 0:
                errores.append(f"Valor inválido para el sensor {id_sensor} en {timestamp}")
                datos_sensores[timestamp][id_sensor] = None  # Marcar como None si es inválido

    # Filtrado de datos válidos
    for timestamp, sensores in datos_sensores.items():
        for id_sensor, valor in sensores.items():
            if valor is not None:  # Solo considerar valores válidos
                if id_sensor not in resultados:
                    resultados[id_sensor] = {
                        'valores': [],
                        'fechas': []
                    }
                resultados[id_sensor]['valores'].append(valor)
                resultados[id_sensor]['fechas'].append(timestamp)

    # Encontrar valores máximo y mínimo para cada sensor
    resumen_sensores = {}
    for id_sensor, data in resultados.items():
        valores = data['valores']
        fechas = data['fechas']
        max_valor = max(valores)
        min_valor = min(valores)
        max_fecha = fechas[valores.index(max_valor)]
        min_fecha = fechas[valores.index(min_valor)]
        resumen_sensores[id_sensor] = {
            'max_valor': max_valor,
            'min_valor': min_valor,
            'max_fecha': max_fecha,
            'min_fecha': min_fecha
        }

    return resumen_sensores, errores

# Función para simular la obtención de datos de la API
def obtener_datos_api():
    # Estos datos simulan la estructura JSON que provendría de la API
    return {
        "2024-08-15T12:00:00Z": {
            "sensor1": 3.5,
            "sensor2": 7.2,
            "sensor3": 9.0
        },
        "2024-08-16T12:05:00Z": {
            "sensor1": 4.0,
            "sensor2": 6.8,
            "sensor3": 8.5
        },
        "2024-08-17T12:10:00Z": {
            "sensor1": 3.2,  # Valor inválido (0)
            "sensor2": 7.0,
            "sensor3": 0
        }
    }

# Función principal para ejecutar el programa
def main():
    datos_sensores = obtener_datos_api()
    resumen_sensores, errores = procesar_datos_sensor(datos_sensores)

    if errores:
        print("Se encontraron los siguientes errores en los datos:")
        for error in errores:
            print(error)
            print(resumen_sensores)
    else:
        print("Datos procesados correctamente:")
        for id_sensor, resumen in resumen_sensores.items():
            print(f"Sensor {id_sensor}:")
            print(f"  Valor máximo: {resumen['max_valor']} el {datetime.strptime(resumen['max_fecha'], '%Y-%m-%dT%H:%M:%SZ').strftime('%m/%d/%Y')}")
            print(f"  Valor mínimo: {resumen['min_valor']} el {datetime.strptime(resumen['min_fecha'], '%Y-%m-%dT%H:%M:%SZ').strftime('%m/%d/%Y')}")
    
    for id_sensor, resumen in resumen_sensores.items():
            print(f"Sensor {id_sensor}:")
            print(f"  Valor máximo: {resumen['max_valor']} el {datetime.strptime(resumen['max_fecha'], '%Y-%m-%dT%H:%M:%SZ').strftime('%m/%d/%Y')}")
            print(f"  Valor mínimo: {resumen['min_valor']} el {datetime.strptime(resumen['min_fecha'], '%Y-%m-%dT%H:%M:%SZ').strftime('%m/%d/%Y')}")
# Ejecutar el programa
if __name__ == "__main__":
    main()