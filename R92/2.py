def estudiantes_destacados(estudiantes):
    destacados = []
    for estudiante in estudiantes:
        nombre = estudiante['nombre']
        puntuaciones = estudiante['puntajes']
        suma = sum(puntuaciones)
        promedio = suma / len(puntuaciones)  # Corrección: dividir por la cantidad de puntuaciones
        if promedio >= 85:  # Corrección: cambiar el valor para identificar estudiantes destacados
            destacados.append(nombre)

    destacados.sort(key=lambda x: x.lower())  # Corrección: ordenar nombres en minúsculas
    return destacados

# Lista de estudiantes
datos = [
    {"nombre": "Ana", "puntajes": [90, 85, 88]},
    {"nombre": "Luis", "puntajes": [70, 65, 72]},
    {"nombre": "Carlos", "puntajes": [95, 92, 88]},
    {"nombre": "Elena", "puntajes": [84, 83, 89]}
]

print(estudiantes_destacados(datos))