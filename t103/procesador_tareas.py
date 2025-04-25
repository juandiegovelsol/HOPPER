import json

def validar_tarea(tarea):
    if not isinstance(tarea, dict):
        print(f"Error: Rechazado - No es diccionario: {tarea}")
        return False


    claves_str_requeridas = ['descripcion', 'asignado_a']
    for clave in claves_str_requeridas:
        if clave not in tarea:
            print(f"Error: Rechazado - Falta clave '{clave}': {tarea}")
            return False
        if not isinstance(tarea[clave], str):
            print(f"Error: Rechazado - Clave '{clave}' no es texto: {tarea}")
            return False
        if not tarea[clave]:
            print(f"Error: Rechazado - Clave '{clave}' está vacía: {tarea}")
            return False

    clave_bool = 'entregada'
    if clave_bool not in tarea:
        print(f"Error: Rechazado - Falta clave booleana '{clave_bool}': {tarea}")
        return False
    if not isinstance(tarea[clave_bool], bool):
        print(f"Error: Rechazado - Clave '{clave_bool}' no es booleana: {tarea}")
        return False

    return True

def cargar_tareas(archivo_json):
    try:
        with open(archivo_json, 'r', encoding='utf-8') as archivo:
            tareas_crudas = json.load(archivo)
        if not isinstance(tareas_crudas, list):
            print(f"Error: El contenido del archivo '{archivo_json}' no es una lista JSON.")
            return []
        tareas_validas = [tarea for tarea in tareas_crudas if validar_tarea(tarea)]
        return tareas_validas
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_json}' no fue encontrado.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error: El archivo '{archivo_json}' no es un JSON válido. Detalles: {e}")
        return []
    except Exception as e:
        print(f"Error inesperado al cargar tareas: {e}")
        return []


def generar_resumen(tareas):
    total_tareas = len(tareas)
    tareas_entregadas = sum(1 for tarea in tareas if tarea.get('entregada', False))
    tareas_pendientes = total_tareas - tareas_entregadas

    personas_pendientes = {}
    for tarea in tareas:
        if not tarea.get('entregada', False):
            persona = tarea.get('asignado_a')
            if persona:
                personas_pendientes[persona] = personas_pendientes.get(persona, 0) + 1

    return {
        'total_tareas': total_tareas,
        'tareas_entregadas': tareas_entregadas,
        'tareas_pendientes': tareas_pendientes,
        'personas_pendientes': personas_pendientes
    }

def mostrar_resumen(resumen):
    print("-" * 30)
    print("      RESUMEN DE TAREAS")
    print("-" * 30)
    print(f"Tareas totales: {resumen['total_tareas']}")
    print(f"Tareas entregadas: {resumen['tareas_entregadas']}")
    print(f"Tareas pendientes: {resumen['tareas_pendientes']}")

    if resumen['personas_pendientes']:
        print("\nPersonas con tareas pendientes:")
        for persona, cantidad in sorted(resumen['personas_pendientes'].items()):
            plural = "tarea" if cantidad == 1 else "tareas"
            print(f"  - {persona}: {cantidad} {plural} pendiente/s")
    else:
        print("\nNo hay tareas pendientes asignadas.")
    print("-" * 30)

def main():
    archivo_json = 'tareas.json'
    print(f"Cargando tareas desde '{archivo_json}'...")
    tareas = cargar_tareas(archivo_json)

    if not tareas:

        if not any(err in cap.out for err in ["Error:", "Debug:"] for cap in [print]):
             print("\nNo se encontraron tareas válidas para procesar en el archivo.")
        return

    print(f"\nSe encontraron {len(tareas)} tareas válidas.")
    resumen = generar_resumen(tareas)
    mostrar_resumen(resumen)

if __name__ == "__main__":
    main()