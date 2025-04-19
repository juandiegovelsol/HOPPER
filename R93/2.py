from datetime import datetime

def validar_eventos(eventos, capacidades):
    errores = []
    # Se ordenan los eventos por máquina y luego por timestamp
    eventos_ordenados = sorted(eventos, key=lambda e: (e['maquina'], e['timestamp']))

    eventos_por_maquina = {}
    for evento in eventos_ordenados:
        maquina = evento['maquina']
        if maquina not in capacidades:
            errores.append(f"Maquina desconocida: {maquina}")
            continue

        produccion = evento.get('produccion', 0)
        if produccion > capacidades[maquina]:
            errores.append(f"Produccion excedida para la maquina {maquina}")
            continue  # Se omite el resto de la validación para este evento

        # Se verifica que los eventos de la misma máquina no se superpongan
        if maquina not in eventos_por_maquina:
            eventos_por_maquina[maquina] = []

        for ev in eventos_por_maquina[maquina]:
            if evento['timestamp'] < ev['timestamp']:
                t1 = datetime.strptime(evento['timestamp'], '%m/%d/%Y %H:%M')
                t0 = datetime.strptime(ev['timestamp'], '%m/%d/%Y %H:%M')
                errores.append(f"Superposición de eventos para la maquina {maquina}")
                break

        eventos_por_maquina[maquina].append(evento)

    return errores

# Ejemplo de uso
eventos = [
    {'maquina': 'M1', 'timestamp': '08/02/2023 08:00', 'produccion': 100},
    {'maquina': 'M2', 'timestamp': '08/02/2023 07:00', 'produccion': 200},
    {'maquina': 'M1', 'timestamp': '08/02/2023 06:00', 'produccion': 90},
    {'maquina': 'M1', 'timestamp': '08/02/2023 08:00', 'produccion': 50}
]

capacidades = {'M1': 100, 'M2': 150}

print(validar_eventos(eventos, capacidades))