import json
from collections import defaultdict
from typing import Dict, List, Any

def calcular_ranking_retrasos(proveedores: Dict[str, List[Dict[str, Any]]]) -> Dict[str, List[Dict[str, Any]]]:
    """
    Calcula el ranking de proveedores con retrasos en las entregas.

    Args:
        proveedores (Dict[str, List[Dict[str, Any]]]): Diccionario con información de los proveedores y sus entregas.

    Returns:
        Dict[str, List[Dict[str, Any]]]: Diccionario con el ranking de proveedores y sus métricas de retrasos.
    """
    retrasos = defaultdict(lambda: {'dias_retraso_totales': 0, 'contador_retrasos': 0})

    # Procesar cada entrega del proveedor
    for proveedor, entregas in proveedores.items():
        for entrega in entregas:
            if entrega['estado_entrega'] == 'retrasado':
                retrasos[proveedor]['dias_retraso_totales'] += entrega['días_retraso']
                retrasos[proveedor]['contador_retrasos'] += 1

    # Calcular promedio de retraso y preparar los datos para el ranking
    ranking = []
    for proveedor, datos in retrasos.items():
        promedio_retraso = datos['dias_retraso_totales'] / datos['contador_retrasos'] if datos['contador_retrasos'] > 0 else 0
        ranking.append({
            "proveedor": proveedor,
            "promedio_retraso [días]": round(promedio_retraso, 2),
            "cantidad_de_retrasos": datos['contador_retrasos']
        })

    # Ordenar el ranking por cantidad de retrasos (descendente)
    ranking.sort(key=lambda x: x['cantidad_de_retrasos'], reverse=True)

    # Seleccionar los 10 proveedores con más retrasos
    ranking = ranking[:5]

    return {
        "proveedores": ranking
    }

def guardar_ranking_en_json(ranking: Dict[str, List[Dict[str, Any]]], archivo_json: str):
    """
    Guarda el ranking de proveedores en un archivo JSON.

    Args:
        ranking (Dict[str, List[Dict[str, Any]]]): Diccionario con el ranking de proveedores.
        archivo_json (str): Ruta del archivo JSON donde se guardará la información.
    """
    try:
        with open(archivo_json, 'w') as json_file:
            json.dump(ranking, json_file, indent=4, ensure_ascii=False)
        print(f"Ranking guardado exitosamente en '{archivo_json}'")
    except Exception as e:
        print(f"Error al guardar el archivo JSON: {e}")

# Ejemplo de uso
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
            "estado_entrega": "puntual",
            "días_retraso": 0
        },
        {
            "fecha_entrega": "2024-07-25",
            "estado_entrega": "retrasado",
            "días_retraso": 7
        },
        {
            "fecha_entrega": "2024-07-26",
            "estado_entrega": "puntual",
            "días_retraso": 0
        }
    ],
    "proveedor_4": [
        {
            "fecha_entrega": "2024-07-27",
            "estado_entrega": "retrasado",
            "días_retraso": 15
        },
        {
            "fecha_entrega": "2024-07-28",
            "estado_entrega": "puntual",
            "días_retraso": 0
        }
    ],
    "proveedor_5": [
        {
            "fecha_entrega": "2024-07-29",
            "estado_entrega": "puntual",
            "días_retraso": 0
        },
        {
            "fecha_entrega": "2024-07-30",
            "estado_entrega": "retrasado",
            "días_retraso": 12
        },
        {
            "fecha_entrega": "2024-07-31",
            "estado_entrega": "puntual",
            "días_retraso": 0
        }
    ],
    "proveedor_6": [
        {
            "fecha_entrega": "2024-08-01",
            "estado_entrega": "retrasado",
            "días_retraso": 8
        },
        {
            "fecha_entrega": "2024-08-02",
            "estado_entrega": "puntual",
            "días_retraso": 0
        },
        {
            "fecha_entrega": "2024-08-03",
            "estado_entrega": "retrasado",
            "días_retraso": 6
        }
    ],
    "proveedor_7": [
        {
            "fecha_entrega": "2024-08-04",
            "estado_entrega": "puntual",
            "días_retraso": 0
        },
        {
            "fecha_entrega": "2024-08-05",
            "estado_entrega": "retrasado",
            "días_retraso": 9
        }
    ],
    "proveedor_8": [
        {
            "fecha_entrega": "2024-08-06",
            "estado_entrega": "puntual",
            "días_retraso": 0
        },
        {
            "fecha_entrega": "2024-08-07",
            "estado_entrega": "retrasado",
            "días_retraso": 11
        }
    ],
    "proveedor_9": [
        {
            "fecha_entrega": "2024-08-08",
            "estado_entrega": "puntual",
            "días_retraso": 0
        },
        {
            "fecha_entrega": "2024-08-09",
            "estado_entrega": "retrasado",
            "días_retraso": 4
        },
        {
            "fecha_entrega": "2024-08-10",
            "estado_entrega": "puntual",
            "días_retraso": 0
        }
    ]
}

ranking = calcular_ranking_retrasos(proveedores)

guardar_ranking_en_json(ranking, "salida.json")