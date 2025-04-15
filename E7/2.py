import json
from collections import defaultdict

def reorganizar_datos_asistentes(archivo_entrada, archivo_salida):
    try:
        # Leer el archivo JSON de entrada
        with open(archivo_entrada, 'r', encoding='utf-8') as file:
            datos = json.load(file)
        
        # Verificar si los datos son una lista
        if not isinstance(datos, list):
            raise ValueError("El archivo JSON debe contener una lista de asistentes.")
        
        # Inicializar estructuras para el resumen
        resumen_comida = defaultdict(int)
        resumen_pago = defaultdict(int)
        asistentes_reorganizados = []
        
        # Procesar cada asistente
        for asistente in datos:
            # Validar los campos requeridos
            campos_requeridos = ["nombre", "email", "pais", "pago", "comida", "sesiones"]
            for campo in campos_requeridos:
                if campo not in asistente:
                    raise KeyError(f"Falta el campo requerido: {campo}")
            
            # Normalizar los nombres de las claves
            asistente_normalizado = {
                "Nombre": asistente["nombre"],
                "Email": asistente["email"],
                "Pais": asistente["pais"],
                "EstadoPago": asistente["pago"].capitalize(),  # Capitalizar el estado de pago
                "PreferenciaComida": asistente["comida"].capitalize(),  # Capitalizar la preferencia de comida
                "SesionesInscritas": asistente["sesiones"]
            }
            
            # Actualizar los resúmenes
            resumen_comida[asistente_normalizado["PreferenciaComida"]] += 1
            resumen_pago[asistente_normalizado["EstadoPago"]] += 1
            
            # Añadir el asistente reorganizado a la lista
            asistentes_reorganizados.append(asistente_normalizado)
        
        # Crear el objeto de salida
        resultado = {
            "Asistentes": asistentes_reorganizados,
            "ResumenPreferenciasComida": dict(resumen_comida),
            "ResumenEstadoPago": dict(resumen_pago)
        }
        
        # Escribir el archivo JSON de salida
        with open(archivo_salida, 'w', encoding='utf-8') as file:
            json.dump(resultado, file, indent=4, ensure_ascii=False)
        
        print(f"Datos reorganizados y guardados en {archivo_salida}")
    
    except FileNotFoundError:
        print(f"Error: El archivo {archivo_entrada} no fue encontrado.")
    except json.JSONDecodeError:
        print(f"Error: El archivo {archivo_entrada} no es un JSON válido.")
    except ValueError as ve:
        print(f"Error de validación: {ve}")
    except KeyError as ke:
        print(f"Error: {ke}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Ejemplo de uso
archivo_entrada = 'asistentes.json'
archivo_salida = 'asistentes_reorganizados.json'
reorganizar_datos_asistentes(archivo_entrada, archivo_salida)