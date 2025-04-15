import json
from collections import defaultdict

# Función para calcular la popularidad de cada banda
def calcular_popularidad(prefencias):
    popularidad = defaultdict(int)
    for preferencia in preferencias:
        for banda_id in preferencia['bandas_favoritas']:
            popularidad[banda_id] += 1
    return popularidad

# Función para optimizar el horario de actuaciones
def optimizar_horario(popularidad, horarios):
    # Ordenar las bandas por popularidad
    bandas_ordenadas = sorted(popularidad.items(), key=lambda x: x[1], reverse=True)
    
    # Crear un nuevo horario optimizado
    horario_optimizado = []
    for banda_id, _ in bandas_ordenadas:
        # Asignar la banda al escenario principal si es posible
        if len(horarios) < 2:
            escenario = "Escenario Principal"
        else:
            # Alternar entre escenarios
            escenario = "Escenario Secundario" if len(horarios) % 2 == 0 else "Escenario Principal"
        
        # Añadir la banda al horario optimizado
        horario_optimizado.append({
            "id": len(horario_optimizado) + 1,
            "id_banda": banda_id,
            "escenario": escenario,
            "fecha": "2024-09-15",  # Fija la fecha para ambos días
            "hora_inicio": "18:00",
            "duracion": 45
        })
    
    return horario_optimizado

# Función para identificar los géneros musicales más populares
def identificar_generos_populares(preferencias):
    generos = defaultdict(int)
    for preferencia in preferencias:
        for genero in preferencia['generos_favoritos']:
            generos[genero] += 1
    
    # Ordenar los géneros por popularidad
    generos_ordenados = sorted(generos.items(), key=lambda x: x[1], reverse=True)
    return generos_ordenados

# Ejemplo de uso
if __name__ == "__main__":
    # Cargar datos desde JSON
    with open('festival_datos.json', 'r') as file:
        festival_data = json.load(file)
    
    # Calcular popularidad de las bandas
    popularidad_bandas = calcular_popularidad(festival_data['preferencias_público'])
    print("Popularidad