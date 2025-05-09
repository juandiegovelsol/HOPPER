import pytest

def validar_puntajes_eso(datos, umbral_aprobado=5.0):
    if not isinstance(datos, dict):
        raise TypeError("El parámetro 'datos' debe ser un diccionario.")

    aprobados = []
    reprobados = []
    errores = []

    for alumno, puntajes in datos.items():
        if not isinstance(alumno, str) or not alumno.strip():
            errores.append(alumno)
            continue
        if not isinstance(puntajes, (list, tuple)) or len(puntajes) == 0:
            errores.append(alumno)
            continue

        suma = 0.0
        valido = True
        for p in puntajes:
            if not isinstance(p, (int, float)) or p < 0 or p > 10:
                valido = False
                break
            suma += p

        if not valido:
            errores.append(alumno)
            continue

        promedio = suma / len(puntajes)

        if promedio >= umbral_aprobado:
            aprobados.append(alumno)
        else:
            reprobados.append(alumno)

    return {
        'aprobados': aprobados,
        'reprobados': reprobados,
        'errores': errores
    }

# Test caso 1: Todos los datos correctos
def test_todos_datos_correctos():
    datos_correctos = {
        'Juan': [6, 7, 8],
        'Ana': [5, 5, 5],
        'Luis': [8, 9, 7]
    }
    resultado = validar_puntajes_eso(datos_correctos)
    assert resultado == {
        'aprobados': ['Juan', 'Ana', 'Luis'],
        'reprobados': [],
        'errores': []
    }

# Test caso 2: Algunos datos incorrectos
def test_algunos_datos_incorrectos():
    datos_incorrectos = {
        'Juan': [6, 7, 8],
        'Ana': [-1, 5, 5],  # Puntaje negativo
        'Luis': [8, 9, 7],
        'Carmen': [],  # Lista vacía
        'Carlos': ''   # Nombre vacío
    }
    resultado = validar_puntajes_eso(datos_incorrectos)
    assert resultado == {
        'aprobados': ['Juan', 'Luis'],
        'reprobados': [],
        'errores': ['Ana', 'Carmen', 'Carlos']
    }

# Test caso 3: Todos los datos incorrectos
def test_todos_datos_incorrectos():
    datos_incorrectos = {
        'Pedro': [-1, -1, -1],  # Todos los puntajes negativos
        'María': [],  # Lista vacía
        'Lucía': [11, 5, 7],  # Puntaje inválido
        '': [10, 10],  # Nombre vacío
        None: [3, 3, 3]  # Clave nula
    }
    resultado = validar_puntajes_eso(datos_incorrectos)
    assert resultado == {
        'aprobados': [],
        'reprobados': [],
        'errores': ['Pedro', 'María', 'Lucía', '', None]
    }