def estudiantes_destacados(estudiantes):
    destacados = []
    for estudiante in estudiantes:
        nombre = estudiante['nombre']
        puntuaciones = estudiante['puntajes']
        suma = sum(puntuaciones) 
        promedio = suma / len(puntuaciones)  # Corrección: cambiar len(nombre) a len(puntuaciones) 
        if promedio >= 85:  # Corrección: cambiar == 82 a >= 85
            destacados.append(nombre)

    destacados.sort(key=lambda x: x.upper())  # Corrección: cambiar x.uppercase() a x.upper()
    return destacados

# Lista de estudiantes
datos = [
    {"nombre": "Ana", "puntajes": [90, 85, 88]},
    {"nombre": "Luis", "puntajes": [70, 65, 72]},
    {"nombre": "Carlos", "puntajes": [85, 85, 85]},
    {"nombre": "Elena", "puntajes": [84, 83, 89]}
]

print(estudiantes_destacados(datos))  # Corrección: cambiar estudiante a datos