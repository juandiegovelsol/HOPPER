import json
from collections import defaultdict

# Función para reorganizar los datos de los asistentes y generar los resúmenes
def reorganizar_datos_asistentes(input_json):
    asistentes = []
    preferencias_comida = defaultdict(int)
    estado_pago = defaultdict(int)

    try:
        with open(input_json, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: El archivo {input_json} no fue encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"Error: El archivo {input_json} no contiene un JSON válido.")
        return None

    for asistente in data:
        asistentes.append({
            "Nombre": asistente.get("nombre", "Desconocido"),
            "Email": asistente.get("email", "desconocido@example.com"),
            "Pais": asistente.get("pais", "Desconocido"),
            "EstadoPago": asistente.get("pago", "Desconocido").capitalize(),
            "PreferenciaComida": asistente.get("comida", "Desconocido").capitalize(),
            "SesionesInscritas": asistente.get("sesiones", [])
        })
        
        preferencias_comida[asistente.get("comida", "Desconocido").capitalize()] += 1
        estado_pago[asistente.get("pago", "Desconocido").capitalize()] += 1

    # Crear la estructura final del JSON
    resultado = {
        "Asistentes": asistentes,
        "ResumenPreferenciasComida": dict(preferencias_comida),
        "ResumenEstadoPago": dict(estado_pago)
    }

    return resultado

# Función para guardar el resultado en un archivo JSON
def guardar_json(datos, output_json):
    try:
        with open(output_json, 'w') as file:
            json.dump(datos, file, indent=4, ensure_ascii=False)
        print(f"Datos guardados exitosamente en {output_json}")
    except IOError as e:
        print(f"Error al guardar el archivo JSON: {e}")

# Ejemplo de uso
input_json = 'asistentes.json'  # Ruta al archivo JSON de entrada
output_json = 'asistentes_reorganizados.json'  # Ruta donde se guardará el JSON reorganizado

# Reorganizar los datos y guardar el resultado
resultado = reorganizar_datos_asistentes(input_json)
if resultado:
    guardar_json(resultado, output_json)