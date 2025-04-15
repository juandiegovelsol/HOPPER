def calcular_promedios(estudiantes):
    # Delimitación de código y ejemplos de uso
    # Ejemplos de uso:
    # calcular_promedios(lista_estudiantes)
    
    # Inicializamos acumuladores
    total_general = 0
    contador_notas = 0
    promedios_individuales = {}
    acum_cursos = {}
    cont_cursos = {}

    for estudiante in estudiantes:
        # Calculamos promedio individual
        promedio_individual = sum(nota for curso, nota in estudiante['cursos']) / len(estudiante['cursos'])
        promedios_individuales[estudiante['nombre']] = promedio_individual
        
        # Actualizamos el total general
        total_general += promedio_individual
        contador_notas += 1
        
        # Calculamos promedios por curso
        for curso, nota in estudiante['cursos']:
            if curso not in acum_cursos:
                acum_cursos[curso] = 0
                cont_cursos[curso] = 0
            acum_cursos[curso] += nota
            cont_cursos[curso] += 1

    # Calculamos el promedio general
    promedio_general = total_general / contador_notas if contador_notas else 0
    print(promedio_general)

    # Calculamos el promedio por curso
    promedios_cursos = {curso: acum / cont for curso, acum in acum_cursos.items() if cont > 0}

    return {
        'promedio_general': promedio_general,
        'promedios_individuales': promedios_individuales,
        'promedios_cursos': promedios_cursos
    }

# Ejemplo de uso:
lista_estudiantes = [
    {
        'nombre': 'Juan',
        'edad': 20,
        'cursos': [
            {'curso': 'Matemáticas', 'nota': 85},
            {'curso': 'Física', 'nota': 90}
        ]
    },
    {
        'nombre': 'Ana',
        'edad': 22,
        'cursos': [
            {'curso': 'Matemáticas', 'nota': 78},
            {'curso': 'Química', 'nota': 88}
        ]
    }
]

resultado = calcular_promedios(lista_estudiantes)
print(resultado)