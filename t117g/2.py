import random
import json
from datetime import datetime, timedelta

def simulate_api_data(num_sensors, num_entries):
    data = {}
    current_time = datetime.now()
    for _ in range(num_entries):
        timestamp = (current_time - timedelta(days=_)).strftime('%m/%d/%Y')
        print(timestamp)
        readings = {}
        for sensor_id in range(1, num_sensors + 1):
            readings[f'sensor_{sensor_id}'] = random.uniform(1, 100)  # Genera un valor mayor que cero
        data[timestamp] = readings
    return data

def validate_and_process_data(data):
    sensor_max_min = {}

    for timestamp, sensors in data.items():
        valid = True

        # Validación de los datos de los sensores
        for sensor_id, value in sensors.items():
            if value <= 0:
                print(f"Ignorando {timestamp} porque {sensor_id} tiene un valor inválido: {value}")
                valid = False
                break
        
        # Procesamiento de los datos válidos
        if valid:
            for sensor_id, value in sensors.items():
                if sensor_id not in sensor_max_min:
                    sensor_max_min[sensor_id] = {'max': (value, timestamp), 'min': (value, timestamp)}
                else:
                    # Verificando el máximo
                    if value > sensor_max_min[sensor_id]['max'][0]:
                        sensor_max_min[sensor_id]['max'] = (value, timestamp)
                    # Verificando el mínimo
                    if value < sensor_max_min[sensor_id]['min'][0]:
                        sensor_max_min[sensor_id]['min'] = (value, timestamp)

    return sensor_max_min

def main():
    # Simulación de datos de la API
    num_sensors = 5
    num_entries = 10
    simulated_data = simulate_api_data(num_sensors, num_entries)

    print("Datos simulados:")
    print(json.dumps(simulated_data, indent=2))

    # Validación y procesamiento de los datos simulados
    sensor_max_min = validate_and_process_data(simulated_data)

    # Imprimiendo los resultados
    print("\nResumen de valores máximo y mínimo por sensor:")
    for sensor_id, values in sensor_max_min.items():
        print(f"{sensor_id} - Máximo: {values['max'][0]} en {values['max'][1]}, Mínimo: {values['min'][0]} en {values['min'][1]}")

if __name__ == "__main__":
    main()