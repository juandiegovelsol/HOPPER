import json
from collections import defaultdict

def analizar_proveedores(proveedores):
    # Inicializar diccionario para almacenar información de cada proveedor
    proveedores_analizados = defaultdict(lambda: {'total_dias_retraso': 0, 'total_retrasos': 0})

    # Procesar cada proveedor y sus entregas
    for proveedor, entregas in proveedores.items():
        for entrega in entregas:
            if entrega['estado_entrega'] == 'retrasado':
                proveedores_analizados[proveedor]['total_dias_retraso'] += entrega['días_retraso']
                proveedores_analizados[proveedor]['total_retrasos'] += 1

    # Calcular el promedio de retrasos y crear una lista de proveedores
    proveedores_ordenados = []
    for proveedor, datos in proveedores_analizados.items():
        promedio_retraso = datos['total_dias_retraso'] / datos['total_retrasos']
        proveedores_ordenados.append({
            'proveedor': proveedor,
            'promedio_retraso [días]': round(promedio_retraso, 2),
            'cantidad_de_retrasos': datos['total_retrasos']
        })

    # Ordenar proveedores por cantidad de retrasos (descendente)
    proveedores_ordenados.sort(key=lambda x: x['cantidad_de_retrasos'], reverse=True)

    # Retornar los 10 proveedores con más retrasos
    return proveedores_ordenados[:5]

# Función para guardar el resultado en un archivo JSON
def guardar_resultado_en_json(resultado, archivo_json):
    with open(archivo_json, 'w') as f:
        json.dump(resultado, f, indent=4)

# Ejemplo de uso
if __name__ == "__main__":
    proveedores = {
        "proveedor_1": [
            {
                "fecha_entrega": "2024-07-20",
                "estado_entrega": "puntual",
                "días_retraso": 0
            },
            {
                "fecha_entrega": "2024-07-22",
                "estado_entrega": "retrasado",
                "días_retraso": 10
            }
        ],
        "proveedor_2": [
            {
                "fecha_entrega": "2024-07-21",
                "estado_entrega": "puntual",
                "días_retraso": 0
            },
            {
                "fecha_entrega": "2024-07-23",
                "estado_entrega": "retrasado",
                "días_retraso": 5
            }
        ],
        "proveedor_3": [
            {
                "fecha_entrega": "2024-07-24",
                "estado_entrega": "retrasado",
                "días_retraso": 15
            },
            {
                "fecha_entrega": "2024-07-25",
                "estado_entrega": "retrasado",
                "días_retraso": 8
            }
        ],
        "proveedor_4": [
            {
                "fecha_entrega": "2024-07-26",
                "estado_entrega": "puntual",
                "días_retraso": 0
            },
            {
                "fecha_entrega": "2024-07-27",
                "estado_entrega": "retrasado",
                "días_retraso": 20
            }
        ],
        "proveedor_5": [
            {
                "fecha_entrega": "2024-07-28",
                "estado_entrega": "retrasado",
                "días_retraso": 12
            }
        ],
        "proveedor_6": [
            {
                "fecha_entrega": "2024-07-29",
                "estado_entrega": "puntual",
                "días_retraso": 0
            },
            {
                "fecha_entrega": "2024-07-30",
                "estado_entrega": "retrasado",
                "días_retraso": 18
            }
        ],
        "proveedor_7": [
            {
                "fecha_entrega": "2024-07-31",
                "estado_entrega": "puntual",
                "días_retraso": 0
            },
            {
                "fecha_entrega": "2024-08-01",
                "estado_entrega": "retrasado",
                "días_retraso": 7
            }
        ],
        "proveedor_8": [
            {
                "fecha_entrega": "2024-08-02",
                "estado_entrega": "puntual",
                "días_retraso": 0
            },
            {
                "fecha_entrega": "2024-08-03",
                "estado_entrega": "retrasado",
                "días_retraso": 11
            }
        ],
        "proveedor_9": [
            {
                "fecha_entrega": "2024-08-04",
                "estado_entrega": "puntual",
                "días_retraso": 0
            },
            {
                "fecha_entrega": "2024-08-05",
                "estado_entrega": "retrasado",
                "días_retraso": 6
            }
        ],
        "proveedor_10": [
            {
                "fecha_entrega": "2024-08-06",
                "estado_entrega": "puntual",
                "días_retraso": 0
            },
            {
                "fecha_entrega": "2024-08-07",
                "estado_entrega": "retrasado",
                "días_retraso": 9
            }
        ]
    }

    # Analizar proveedores
    resultados = analizar_proveedores(proveedores)

    # Guardar resultados en archivo JSON
    guardar_resultado_en_json(resultados, "proveedores_retrasos.json")

    print("Resultados guardados en 'proveedores_retrasos.json'")