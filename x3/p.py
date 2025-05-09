def analizar_datos_accion(precios: list[float], umbral: float, porcentaje_quiebre: float) -> tuple[list[int], list[float], list[int]]:
    if len(precios) <= 1:
        return [], [], []

    # Calcular promedio móvil
    promedio_movil = sum(precios) / len(precios)

    # Detectar anomalías de precio (cuando se desvían más del umbral respecto al promedio)
    anomalias = [
        i for i, precio in enumerate(precios)
        if abs(precio - promedio_movil) / promedio_movil > umbral
    ]

    # Calcular retornos acumulados
    retornos_acumulados = []
    retorno_total = 0.0
    precio_inicial = precios[0]

    for i, precio in enumerate(precios):
        if i == 0:
            retornos_acumulados.append(0.0)
        else:
            retorno_diario = (precio - precio_inicial) / precio_inicial
            retorno_total += retorno_diario
            retornos_acumulados.append(retorno_total)

    # Identificar puntos de quiebre 
    puntos_quiebre = []
    maximo_anterior = precios[0]

    for i, precio in enumerate(precios):
        if precio > maximo_anterior:
            maximo_anterior = precio
        elif (maximo_anterior - precio) / maximo_anterior >= porcentaje_quiebre:
            print(precio, maximo_anterior, (maximo_anterior - precio) / maximo_anterior)
            puntos_quiebre.append(i)

    return anomalias, retornos_acumulados, puntos_quiebre

# Datos de prueba (valores en dólares)
precios1 = [150.0, 145.0, 160.0, 155.0, 170.0, 180.0]
umbral = 0.15
porcentaje_quiebre = 0.10

# Resultados esperados
resultado1 = analizar_datos_accion(precios1, umbral, porcentaje_quiebre)


# Mostrar resultados
print(" Resultados del caso de prueba :")
print(f"Anomalías: {resultado1[0]}")
print(f"Retornos acumulados: {[round(r, 4) for r in resultado1[1]]}")
print(f"Puntos de quiebre: {resultado1[2]}\n")



""" ) precios1 = [150.0, 145.0, 160.0, 155.0, 170.0, 180.0]
B) precios2 = [200.0, 190.0, 180.0, 210.0, 220.0, 230.0]
C) precios3 = [120.0, 125.0, 130.0, 128.0, 135.0, 140.0] """