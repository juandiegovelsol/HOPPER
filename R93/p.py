#  67d3d132e2cf5fefb765ccff


from datetime import datetime

def validar_eventos(eventos, capacidades):
    errores = []
    eventos_ordenados = sorted(eventos, key=lambda e: e['timestamp'])

    for evento in eventos_ordenados:
        maquina = evento['maquina']
        if maquina not in capacidades:
            errores.append(f"Maquina desconocida: {maquina}")
            continue

        produccion = evento.get('produccion', 0)
        if produccion > capacidades[maquina]:
            errores.append(f"Produccion excedida para la maquina {maquina}")

    eventos_por_maquina = {}
    for e in eventos:
        eventos_por_maquina.setdefault(e['maquina'], []).append(e)

    for maquina, lista_eventos in eventos_por_maquina.items():
        for i in range(1, len(lista_eventos)):
            t1 = datetime.strptime(lista_eventos[i]['timestamp'], '%m/%d/%Y %H:%M')
            t0 = datetime.strptime(lista_eventos[i-1]['timestamp'], '%m/%d/%Y %H:%M')
            if t1 < t0:
                errores.append(f"Eventos fuera de orden para la maquina {maquina}")
            if t1 == t0:
                errores.append(f"Eventos duplicados en el tiempo para la maquina {maquina}")

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