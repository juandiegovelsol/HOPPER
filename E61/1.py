import json
from collections import defaultdict

def reorganizar_asistentes(archivo_entrada, archivo_salida):
    """
    Lee un archivo JSON con información de asistentes y lo reorganiza en un formato más estructurado.
    Genera dos informes adicionales sobre preferencias de comida y estado de pago.

    Parámetros:
    - archivo_entrada (str): Ruta del archivo JSON de entrada.
    - archivo_salida (str): Ruta del archivo JSON de salida.

    Retorna:
    - dict: Objeto JSON reorganizado con la información de los asistentes.
    """
    try:
        # Leer el archivo JSON de entrada
        with open(archivo_entrada, 'r') as file:
            asistentes = json.load(file)

        # Reorganizar la información de los asistentes en un formato más estructurado
        asistentes_reorganizados = []
        resumen_preferencias_comida = defaultdict(int)
        resumen_estado_pago = defaultdict(int)

        for asistente in asistentes:
            # Convertir las sesiones a una lista de strings
            sesiones_lista = asistente.get("sesiones", [])
            
            # Agregar la información reorganizada a la lista de asistentes
            asistentes_reorganizados.append({
                "Nombre": asistente.get("nombre"),
                "Email": asistente.get("email"),
                "Pais": asistente.get("pais"),
                "EstadoPago": asistente.get("pago"),
                "PreferenciaComida": asistente.get("comida"),
                "SesionesInscritas": sesiones_lista
            })
            
            # Actualizar los resumos de preferencias de comida y estado de pago
            resumen_preferencias_comida[asistente.get("comida", "Desconocido")] += 1
            resumen_estado_pago[asistente.get("pago", "Desconocido")] += 1

        # Crear el objeto JSON final con la información reorganizada y los resumos
        resultado = {
            "Asistentes": asistentes_reorganizados,
            "ResumenPreferenciasComida": dict(resumen_preferencias_comida),
            "ResumenEstadoPago": dict(resumen_estado_pago)
        }

        # Guardar el objeto JSON reorganizado en el archivo de salida
        with open(archivo_salida, 'w') as file:
            json.dump(resultado, file, indent=4, ensure_ascii=False)

        print(f"Archivo reorganizado guardado en {archivo_salida}")
        return resultado

    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no se encontró.")
    except json.JSONDecodeError:
        print(f"Error: El archivo '{archivo_entrada}' no es un JSON válido.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    archivo_entrada = 'asistentes.json'  # Ruta del archivo de entrada
    archivo_salida = 'asistentes_reorganizados.json'  # Ruta del archivo de salida
    reorganizar_asistentes(archivo_entrada, archivo_salida)