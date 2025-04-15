import json
from collections import defaultdict

def reorganizar_informacion_asistentes(archivo_json):
    try:
        # Leer el archivo JSON
        with open(archivo_json, 'r') as file:
            asistentes = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error al leer el archivo JSON: {e}")
        return None

    # Estructura de datos reorganizada
    asistentes_estructurados = []
    resumen_preferencias_comida = defaultdict(int)
    resumen_estado_pago = defaultdict(int)

    # Procesar cada asistente
    for asistente in asistentes:
        # Reorganizar los datos del asistente
        asistente_estructurado = {
            "Nombre": asistente.get("nombre", "Desconocido"),
            "Email": asistente.get("email", "Desconocido"),
            "Pais": asistente.get("pais", "Desconocido"),
            "EstadoPago": asistente.get("pago", "Desconocido"),
            "PreferenciaComida": asistente.get("comida", "Desconocido"),
            "SesionesInscritas": asistente.get("sesiones", [])
        }
        
        # Actualizar resúmenes
        resumen_preferencias_comida[asistente["comida"]] += 1
        resumen_estado_pago[asistente["pago"]] += 1
        
        # Añadir al arreglo estructurado
        asistentes_estructurados.append(asistente_estructurado)

    # Crear el objeto JSON final
    resultado = {
        "Asistentes": asistentes_estructurados,
        "ResumenPreferenciasComida": dict(resumen_preferencias_comida),
        "ResumenEstadoPago": dict(resumen_estado_pago)
    }

    return resultado

def guardar_json(datos, archivo_salida):
    try:
        with open(archivo_salida, 'w') as file:
            json.dump(datos, file, indent=4, ensure_ascii=False)
        print(f"Informe guardado exitosamente en {archivo_salida}")
    except IOError as e:
        print(f"Error al guardar el archivo JSON: {e}")

# Uso del script
archivo_json_entrada = 'asistentes.json'
archivo_json_salida = 'informe_asistentes.json'

# Reorganizar y generar el informe
informe_final = reorganizar_informacion_asistentes(archivo_json_entrada)
if informe_final:
    guardar_json(informe_final, archivo_json_salida)