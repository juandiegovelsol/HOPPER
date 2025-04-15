import json
from collections import defaultdict

# Función para reorganizar el archivo JSON de asistentes
def reorganizar_asistentes(archivo_json):
    try:
        # Abrir y cargar el archivo JSON
        with open(archivo_json, 'r', encoding='utf-8') as file:
            asistentes = json.load(file)
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_json}' no se encontró.")
        return None
    except json.JSONDecodeError:
        print(f"Error: El archivo '{archivo_json}' no contiene un JSON válido.")
        return None

    # Diccionarios para los resúmenes de preferencias y estado de pago
    resumen_preferencias_comida = defaultdict(int)
    resumen_estado_pago = defaultdict(int)

    # Procesar cada asistente
    for asistente in asistentes:
        nombre = asistente.get("nombre")
        email = asistente.get("email")
        pais = asistente.get("pais")
        pago = asistente.get("pago")
        comida = asistente.get("comida")
        sesiones = asistente.get("sesiones", [])

        # Reorganizar la información del asistente
        asistente_reorganizado = {
            "Nombre": nombre,
            "Email": email,
            "Pais": pais,
            "EstadoPago": pago,
            "PreferenciaComida": comida,
            "SesionesInscritas": sesiones
        }

        # Actualizar los resúmenes
        resumen_preferencias_comida[comida] += 1
        resumen_estado_pago[pago] += 1

    # Crear el objeto JSON final
    resultado = {
        "Asistentes": [asistente_reorganizado for asistente in asistentes],
        "ResumenPreferenciasComida": dict(resumen_preferencias_comida),
        "ResumenEstadoPago": dict(resumen_estado_pago)
    }

    return resultado

# Función para guardar el objeto JSON final en un archivo
def guardar_json(objeto_json, archivo_salida):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as file:
            json.dump(objeto_json, file, ensure_ascii=False, indent=4)
        print(f"El archivo '{archivo_salida}' se ha guardado exitosamente.")
    except IOError as e:
        print(f"Error al guardar el archivo '{archivo_salida}': {e}")

# Ejemplo de uso
archivo_json_entrada = 'asistentes.json'
archivo_json_salida = 'asistentes_reorganizados.json'

# Reorganizar los asistentes y guardar el resultado
resultado_json = reorganizar_asistentes(archivo_json_entrada)
if resultado_json:
    guardar_json(resultado_json, archivo_json_salida)
