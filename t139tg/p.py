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


if __name__ == '__main__':
    datos_ejemplo = {
        'Juan': [],  # Lista vacía
        'María': [5, 5],  # Lista con menos de 3 notas
        'Carlos': [11, 10, 9],  # Puntajes inválidos
        'Ana': ''  # Nombre vacío
    }

    resultados = validar_puntajes_eso(datos_ejemplo)
    print(resultados)
    print("Aprobados:", resultados['aprobados'])
    print("Reprobados:", resultados['reprobados'])
    print("Errores:", resultados['errores'])