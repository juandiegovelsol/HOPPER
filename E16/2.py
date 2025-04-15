import json
from collections import defaultdict

def leer_json(ruta_archivo):
    """
    Lee un archivo JSON y retorna su contenido como un diccionario.

    Parámetros:
    ruta_archivo (str): Ruta al archivo JSON a leer.

    Retorna:
    dict: Contenido del archivo JSON como un diccionario.

    Lanza:
    FileNotFoundError: Si el archivo no se encuentra.
    json.JSONDecodeError: Si el archivo no contiene un JSON válido.
    """
    try:
        with open(ruta_archivo, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(f"Error: El archivo {ruta_archivo} no se encontró.")
        return None
    except json.JSONDecodeError:
        print(f"Error: El archivo {ruta_archivo} no contiene un JSON válido.")
        return None

def reorganizar_datos_asistentes(asistentes):
    """
    Reorganiza los datos de los asistentes en una estructura más lógica.

    Parámetros:
    asistentes (list): Lista de diccionarios representando a los asistentes.

    Retorna:
    dict:
        - 'Asistentes': Lista de diccionarios con la información reorganizada de cada asistente.
        - 'ResumenPreferenciasComida': Diccionario con el conteo de preferencias de comida.
        - 'ResumenEstadoPago': Diccionario con el conteo de estados de pago.
    """
    asistentes_reorganizados = []
    resumen_preferencias_comida = defaultdict(int)
    resumen_estado_pago = defaultdict(int)

    for asistente in asistentes:
        # Reorganizar datos del asistente
        asistente_reorganizado = {
            "Nombre": asistente["nombre"],
            "Email": asistente["email"],
            "Pais": asistente["pais"],
            "EstadoPago": asistente["pago"],
            "PreferenciaComida": asistente["comida"],
            "SesionesInscritas": asistente["sesiones"]
        }
        
        # Actualizar resúmenes
        resumen_preferencias_comida[asistente["comida"]] += 1
        resumen_estado_pago[asistente["pago"]] += 1
        
        # Añadir al lista de asistentes reorganizados
        asistentes_reorganizados.append(asistente_reorganizado)

    return {
        "Asistentes": asistentes_reorganizados,
        "ResumenPreferenciasComida": dict(resumen_preferencias_comida),
        "ResumenEstadoPago": dict(resumen_estado_pago)
    }

def guardar_json(datos, ruta_archivo):
    """
    Guarda un diccionario en un archivo JSON.

    Parámetros:
    datos (dict): Diccionario que se desea guardar en el archivo JSON.
    ruta_archivo (str): Ruta donde se guardará el archivo JSON.

    Lanza:
    OSError: Si ocurre un error al escribir en el archivo.
    """
    try:
        with open(ruta_archivo, 'w') as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        print(f"Archivo guardado exitosamente en {ruta_archivo}.")
    except OSError as e:
        print(f"Error al guardar el archivo JSON: {e}")

def main():
    # Ruta al archivo JSON de entrada
    ruta_archivo_entrada = 'asistentes.json'
    
    # Leer los datos de los asistentes desde el archivo JSON
    datos_asistentes = leer_json(ruta_archivo_entrada)
    
    if datos_asistentes is None:
        return
    
    # Reorganizar los datos de los asistentes
    resultados = reorganizar_datos_asistentes(datos_asistentes.get("Asistentes", []))
    
    # Guardar los resultados reorganizados en un nuevo archivo JSON
    ruta_archivo_salida = 'asistentes_reorganizados.json'
    guardar_json(resultados, ruta_archivo_salida)
    
    # Imprimir los informes adicionales
    print("\nResumen de Preferencias de Comida:")
    print(resultados["ResumenPreferenciasComida"])
    
    print("\nResumen de Estado de Pago:")
    print(resultados["ResumenEstadoPago"])

if __name__ == "__main__":
    main()