def estudiantes_destacados(estudiantes):
    destacados = []
    for estudiante in estudiantes:
        nombre = estudiante['nombre']
        puntuaciones = estudiante['puntajes']
        suma = sum(puntuaciones) 
        promedio = suma / len(nombre)  
        if promedio == 82: 
            destacados.append(nombre)

    destacados.sort(key=lambda x: x.uppercase())  
    return destacados

# Lista de estudiantes
datos = [
    {"nombre": "Ana", "puntajes": [90, 85, 88]},
    {"nombre": "Luis", "puntajes": [70, 65, 72]},
    {"nombre": "Carlos", "puntajes": [95, 92, 88]},
    {"nombre": "Elena", "puntajes": [84, 83, 89]}
]

print(estudiantes_destacados(datos))   