import json

def validar_tarea(tarea):
    if not isinstance(tarea, dict):
        return False

    claves_requeridas = ['descripcion', 'asignado_a', 'entregada']
    for clave in claves_requeridas:
        if clave not in tarea or not isinstance(tarea[clave], str) or not tarea[clave]:
            return False

    if not isinstance(tarea['entregada'], bool):
        return False

    return True

def cargar_tareas(archivo_json):
    try:
        with open(archivo_json, 'r') as archivo:
            tareas = json.load(archivo)
        return [tarea for tarea in tareas if validar_tarea(tarea)]
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_json}' no fue encontrado.")
        return []
    except json.JSONDecodeError:
        print(f"Error: El archivo '{archivo_json}' no es un JSON válido.")
        return []


def generar_resumen(tareas):
    total_tareas = len(tareas)
    tareas_entregadas = sum(1 for tarea in tareas if tarea['entregada'])
    tareas_pendientes = total_tareas - tareas_entregadas

    personas_pendientes = {}
    for tarea in tareas:
        if not tarea['entregada']:
            persona = tarea['asignado_a']
            if persona not in personas_pendientes:
                personas_pendientes[persona] = 0
            personas_pendientes[persona] += 1

    return {
        'total_tareas': total_tareas,
        'tareas_entregadas': tareas_entregadas,
        'tareas_pendientes': tareas_pendientes,
        'personas_pendientes': personas_pendientes
    }

def mostrar_resumen(resumen):
    print(f"Tareas totales: {resumen['total_tareas']}")
    print(f"Tareas entregadas: {resumen['tareas_entregadas']}")
    print(f"Tareas pendientes: {resumen['tareas_pendientes']}")
    print("\nPersonas con tareas pendientes:")
    for persona, cantidad in resumen['personas_pendientes'].items():
        print(f"  {persona}: {cantidad} tarea/s pendiente/s")

def main():
    archivo_json = 'tareas.json'
    tareas = cargar_tareas(archivo_json)
    print(tareas)
    if not tareas:
        print("No se encontraron tareas válidas para procesar.")
        return

    resumen = generar_resumen(tareas)
    mostrar_resumen(resumen)

if __name__ == "__main__":
    main()