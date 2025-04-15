import csv
import json
from typing import List, Dict

# Diccionario que contiene la información de los equipos
equipos: Dict[str, Dict] = {
    "Brasil": {"entrenador": "Carlos Alberto", "continente": "América del Sur", "jugadores": [
        {"nombre_jugador": "Fernando Gómez", "altura": 1.85, "edad": 26, "posicion": "Base", "equipo": "Uruguay"},
        {"nombre_jugador": "Rodrigo Ramos", "altura": 1.90, "edad": 28, "posicion": "Ala-pívot", "equipo": "Brasil"}
    ]},
    "España": {"entrenador": "Pau Gasol", "continente": "Europa", "jugadores": [
        {"nombre_jugador": "Marc Gasol", "altura": 2.06, "edad": 31, "posicion": "Pívot", "equipo": "España"},
        {"nombre_jugador": "Sergio Llull", "altura": 1.90, "edad": 27, "posicion": "Base", "equipo": "España"}
    ]}
}

# Función para leer el archivo CSV y convertirlo en un diccionario
def leer_csv(nombre_archivo: str) -> List[Dict]:
    datos: List[Dict] = []
    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                datos.append(fila)
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print(f"Error al leer el archivo '{nombre_archivo}': {e}")
    return datos

# Función para convertir el archivo CSV de jugadores en un diccionario
def leer_jugadores(nombre_archivo: str) -> Dict:
    jugadores: Dict = {}
    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                nombre_jugador = fila['nombre_jugador']
                jugadores[nombre_jugador] = {
                    "altura": float(fila['altura']),
                    "edad": int(fila['edad']),
                    "posicion": fila['posicion'],
                    "equipo": fila['equipo']
                }
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print(f"Error al leer el archivo '{nombre_archivo}': {e}")
    return jugadores

# Función para procesar los partidos y generar la estructura JSON
def procesar_partidos(partidos_csv: str, jugadores_csv: str) -> Dict:
    partidos: List[Dict] = leer_csv(partidos_csv)
    jugadores: Dict = leer_jugadores(jugadores_csv)
    resultado: Dict = {
        "partidos": []
    }
    
    for partido in partidos:
        equipos_enfrentados = partido['equipos_enfrentados'].split(',')
        partido_id = partido['id']
        etapa_partido = partido['etapa_partido']
        arbitro = partido['arbitro']
        
        equipo_1 = equipos_enfrentados[0]
        print(equipo_1)
        equipo_2 = equipos_enfrentados[1]
        
        jugadores_1 = jugadores.get(equipo_1, {})
        jugadores_2 = jugadores.get(equipo_2, {})
        
        resultado["partidos"].append({
            "id": partido_id,
            "etapa_partido": etapa_partido,
            "equipos_enfrentados": [equipo_1, equipo_2],
            "arbitro": arbitro,
            "jugadores": [
                {"nombre_jugador": jugador['nombre_jugador'], "altura": jugador['altura'], "edad": jugador['edad'], "posicion": jugador['posicion'], "equipo": jugador['equipo']}
                for jugador in jugadores_1.values()
            ],
            "jugadores": [
                {"nombre_jugador": jugador['nombre_jugador'], "altura": jugador['altura'], "edad": jugador['edad'], "posicion": jugador['posicion'], "equipo": jugador['equipo']}
                for jugador in jugadores_2.values()
            ]
        })
    
    return resultado

# Función para guardar el resultado en un archivo JSON
def guardar_json(datos: Dict, nombre_archivo: str) -> None:
    try:
        with open(nombre_archivo, mode='w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)
        print(f"El archivo '{nombre_archivo}' se ha guardado correctamente.")
    except Exception as e:
        print(f"Error al guardar el archivo '{nombre_archivo}': {e}")

# Nombre de los archivos CSV
partidos_csv = 'partidos.csv'
jugadores_csv = 'jugadores.csv'

# Procesar los partidos y generar el JSON
resultado = procesar_partidos(partidos_csv, jugadores_csv)

# Guardar el resultado en un archivo JSON
guardar_json(resultado, 'partidos_olimpicos.json')