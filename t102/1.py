import json

# Función para validar los datos de una tarea
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

# Función para cargar tareas desde un archivo JSON
def cargar_tareas(archivo_json):
    try:
        with open(archivo_json, 'r') as archivo:
            tareas = json.load(archivo)
        return [t for t in tareas if validar_tarea(t)]
    except Exception as e:
        print(f"Error al cargar el archivo JSON: {e}")
        return []

# Función para mostrar un resumen de las tareas
def resumen_tareas(tareas):
    total_tareas = len(tareas)
    tareas_entregadas = sum(1 for t in tareas if t['entregada'])
    tareas_pendientes = total_tareas - tareas_entregadas

    personas_pendientes = {}
    for t in tareas:
        if not t['entregada']:
            persona = t['asignado_a']
            if persona not in personas_pendientes:
                personas_pendientes[persona] = 0
            personas_pendientes[persona] += 1

    print(f"Tareas totales: {total_tareas}")
    print(f"Tareas entregadas: {tareas_entregadas}")
    print(f"Tareas pendientes: {tareas_pendientes}")
    print("\nPersonas con tareas pendientes:")
    for persona, cantidad in personas_pendientes.items():
        print(f"{persona}: {cantidad} tarea/s pendiente/s")

# Función principal del programa
def main():
    archivo_json = 'tareas.json'  # Cambio nombre de variable para que sea más descriptiva
    tareas = cargar_tareas(archivo_json)

    if not tareas:
        print("No se pudieron cargar las tareas. Asegúrate de que el archivo JSON esté correctamente formado.")
        return

    print("Resumen de tareas:")
    resumen_tareas(tareas)

if __name__ == '__main__':
    main()