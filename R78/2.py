def calcular_promedios(estudiantes):
    # Delimitación de ejemplo de uso
    # --- Ejemplo de uso ---
    # estudiantes = [
    #     {
    #         'nombre': 'Juan',
    #         'edad': 20,
    #         'cursos': [
    #             {'curso': 'Matemáticas', 'nota': 80},
    #             {'curso': 'Física', 'nota': 90}
    #         ]
    #     },
    #     {
    #         'nombre': 'Ana',
    #         'edad': 22,
    #         'cursos': [
    #             {'curso': 'Matemáticas', 'nota': 75},
    #             {'curso': 'Química', 'nota': 85}
    #         ]
    #     }
    # ]
    # --- Ejemplo de uso ---
    
    promedio_general_estudiantes = []
    promedio_cursos = {}
    contadores = {'total_estudiantes': 0, 'total_cursos': 0}

    for estudiante in estudiantes:
        promedio_estudiante = sum(curso['nota'] for curso in estudiante['cursos']) / len(estudiante['cursos'])
        promedio_general_estudiantes.append(promedio_estudiante)
        
        for curso in estudiante['cursos']:
            curso_nombre = curso['curso']
            if curso_nombre not in promedio_cursos:
                promedio_cursos[curso_nombre] = {'total_notas': 0, 'cantidad_estudiantes': 0}
            
            promedio_cursos[curso_nombre]['total_notas'] += curso['nota']
            promedio_cursos[curso_nombre]['cantidad_estudiantes'] += 1
            contadores['total_cursos'] += 1
        
        contadores['total_estudiantes'] += 1

    promedio_general = sum(promedio_general_estudiantes) / contadores['total_estudiantes'] if contadores['total_estudiantes'] else 0

    for curso, valores in promedio_cursos.items():
        promedio_cursos[curso]['promedio'] = valores['total_notas'] / (valores['cantidad_estudiantes'] * contadores['total_estudiantes'])

    return {
        'promedio_general': promedio_general,
        'promedio_por_estudiante': promedio_general_estudiantes,
        'promedio_por_curso': promedio_cursos
    }

# Ejemplo de uso:
estudiantes = [
    {
        'nombre': 'Juan',
        'edad': 20,
        'cursos': [
            {'curso': 'Matemáticas', 'nota': 80},
            {'curso': 'Física', 'nota': 90}
        ]
    },
    {
        'nombre': 'Ana',
        'edad': 22,
        'cursos': [
            {'curso': 'Matemáticas', 'nota': 75},
            {'curso': 'Química', 'nota': 85}
        ]
    }
]

resultados = calcular_promedios(estudiantes)
print(resultados)