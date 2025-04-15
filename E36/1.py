import json
from collections import defaultdict

def generar_ranking_retrasos(proveedores):
    # Diccionario para almacenar datos agregados por proveedor
    datos_proveedores = defaultdict(lambda: {
        'retrasos': 0,
        'días_retrasos': 0
    })

    # Procesar cada proveedor y sus entregas
    for proveedor, entregas in proveedores.items():
        for entrega in entregas:
            if entrega['estado_entrega'] == 'retrasado':
                datos_proveedores[proveedor]['retrasos'] += 1
                datos_proveedores[proveedor]['días_retrasos'] += entrega['días_retraso']

    # Calcular promedio de retraso y crear ranking
    ranking_retrasos = []
    for proveedor, datos in datos_proveedores.items():
        promedio_retraso = datos['días_retrasos'] / datos['retrasos'] if datos['retrasos'] > 0 else 0
        ranking_retrasos.append({
            'proveedor': proveedor,
            'promedio_retraso [días]': promedio_retraso,
            'cantidad_de_retrasos': datos['retrasos']
        })
    
    # Ordenar por cantidad de retrasos (mayor primero)
    ranking_retrasos.sort(key=lambda x: x['cantidad_de_retrasos'], reverse=True)

    return ranking_retrasos

# Función para guardar el ranking en un archivo JSON
def guardar_en_json(ranking, archivo_json):
    with open(archivo_json, 'w') as f:
        json.dump({
            "proveedores": ranking
        }, f, indent=4)

# Ejemplos de uso
if __name__ == "__main__":
    proveedores = {
        "proveedor_1": [
            { "fecha_entrega": "2024-07-20", "estado_entrega": "puntual", "días_retraso": 0 },
            { "fecha_entrega": "2024-07-22", "estado_entrega": "retrasado", "días_retraso": 10 }
        ],
        "proveedor_2": [
            { "fecha_entrega": "2024-07-21", "estado_entrega": "puntual", "días_retraso": 0 },
            { "fecha_entrega": "2024-07-23", "estado_entrega": "retrasado", "días_retraso": 5 }
        ],
        "proveedor_3": [
            { "fecha_entrega": "2024-07-24", "estado_entrega": "puntual", "días_retraso": 0 },
            { "fecha_entrega": "2024-07-25", "estado_entrega": "retrasado", "días_retraso": 2 },
            { "fecha_entrega": "2024-07-26", "estado_entrega": "retrasado", "días_retraso": 3 }
        ]
    }

    ranking = generar_ranking_retrasos(proveedores)
    guardar_en_json(ranking, 'ranking_retrasos.json')

    print("Ranking de proveedores con retrasos generado y guardado en 'ranking_retrasos.json'")