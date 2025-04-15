import csv
import json
from typing import List, Dict

def leer_csv(ruta_archivo: str) -> List[Dict[str, str]]:
    """
    Lee un archivo CSV y lo convierte en una lista de diccionarios.

    Args:
        ruta_archivo (str): Ruta del archivo CSV.

    Returns:
        List[Dict[str, str]]: Lista de diccionarios con la información del archivo CSV.

    Raises:
        FileNotFoundError: Si el archivo CSV no se encuentra.
        csv.Error: Si hay un error al leer el archivo CSV.
    """
    try:
        with open(ruta_archivo, mode='r') as archivo:
            lector = csv.DictReader(archivo)
            return list(lector)
    except FileNotFoundError:
        print(f"Error: El archivo {ruta_archivo} no se encontró.")
        return []
    except csv.Error as e:
        print(f"Error al leer el archivo CSV: {e}")
        return []

def generar_estructura_json(partidos: List[Dict[str, str]], jugadores: List[Dict[str, str]]) -> Dict[str, Any]:
    """
    Genera la estructura JSON a partir de los partidos y jugadores.

    Args:
        partidos (List[Dict[str, str]]): Lista de diccionarios con la información de los partidos.
        jugadores (List[Dict[str, str]]): Lista de diccionarios con la información de los jugadores.

    Returns:
        Dict[str, Any]: Estructura JSON generada.
    """
    estructura_json = {
        "partidos": []
    }

    for partido in partidos:
        id_partido = partido["id"]
        etapa_partido = partido["etapa_partido"]
        equipos_enfrentados = partido["equipos_enfrentados"]
        arbitro = partido["arbitro"]

        jugadores_partido = []
        for jugador in jugadores:
            if jugador["equipo"] in equipos_enfrentados:
                nombre_jugador = jugador["nombre_jugador"]
                altura = jugador["altura"]
                edad = jugador["edad"]
                posicion = jugador["posicion"]
                equipo = jugador["equipo"]

                jugadores_partido.append({
                    "nombre_jugador": nombre_jugador,
                    "altura": altura,
                    "edad": edad,
                    "posicion": posicion,
                    "equipo": equipo
                })

        partido_json = {
            "id": id_partido,
            "etapa_partido": etapa_partido,
            "equipos_enfrentados": equipos_enfrentados,
            "arbitro": arbitro,
            "jugadores": jugadores_partido
        }

        estructura_json["partidos"].append(partido_json)

    return estructura_json

def escribir_json(ruta_archivo: str, datos: Dict[str, Any]):
    """
    Escribe la estructura JSON en un archivo.

    Args:
        ruta_archivo (str): Ruta del archivo JSON a escribir.
        datos (Dict[str, Any]): Datos a escribir en el archivo JSON.

    Raises:
        IOError: Si hay un error al escribir el archivo JSON.
    """
    try:
        with open(ruta_archivo, mode='w') as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        print(f"JSON generado exitosamente en {ruta_archivo}")
    except IOError as e:
        print(f"Error al escribir el archivo JSON: {e}")

# Rutas de los archivos CSV
ruta_partidos_csv = 'partidos.csv'
ruta_jugadores_csv = 'jugadores.csv'
ruta_json_salida = 'partidos_olimpicos.json'

# Leer los archivos CSV
partidos = leer_csv(ruta_partidos_csv)
jugadores = leer_csv(ruta_jugadores_csv)

print(jugadores, partidos)

# Validar que los archivos CSV no estén vacíos
if partidos and jugadores:
    # Generar la estructura JSON
    estructura_json = generar_estructura_json(partidos, jugadores)

    # Escribir la estructura JSON en un archivo
    escribir_json(ruta_json_salida, estructura_json)
else:
    print("Error: Uno de los archivos CSV está vacío.")