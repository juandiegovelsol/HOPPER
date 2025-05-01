import json
from datetime import datetime

def read_data_from_json(filepath):
    with open(filepath, 'r') as f:
        raw = json.load(f)

    data = {}
    for ts_str, readings in raw.items():
        dt = datetime.fromtimestamp(int(ts_str))
        formatted_ts = dt.strftime('%m/%d/%Y %H:%M:%S')
        data[formatted_ts] = readings

    return data

def validate_and_process_data(data):
    sensor_max_min = {}

    for timestamp, sensors in data.items():
        valid = True
        for sensor_id, value in sensors.items():
            if not isinstance(value, int) or value <= 0:
                print(f"Ignorando {timestamp} porque {sensor_id} tiene un valor inválido: {value}")
                valid = False
                break

        if valid:
            for sensor_id, value in sensors.items():
                if sensor_id not in sensor_max_min:
                    sensor_max_min[sensor_id] = {
                        'max': (value, timestamp),
                        'min': (value, timestamp)
                    }
                else:
                    if value > sensor_max_min[sensor_id]['max'][0]:
                        sensor_max_min[sensor_id]['max'] = (value, timestamp)
                    if value < sensor_max_min[sensor_id]['min'][0]:
                        sensor_max_min[sensor_id]['min'] = (value, timestamp)

    return sensor_max_min

def main():
    json_file = 'sensores.json'
    data = read_data_from_json(json_file)
    resultados = validate_and_process_data(data)
    print("\nResumen de valores máximo y mínimo por sensor:")
    for sensor_id, vals in resultados.items():
        max_val, max_ts = vals['max']
        min_val, min_ts = vals['min']
        print(f"{sensor_id} → Máximo: {max_val} en {max_ts}; Mínimo: {min_val} en {min_ts}")

if __name__ == "__main__":
    main()
