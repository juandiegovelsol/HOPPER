def bot_inversion_simple(precios):
    operaciones = []
    posicion_abierta = False

    for i in range(1, len(precios)):
        precio_anterior = precios[i - 1]
        precio_actual = precios[i]

        cambio_porcentaje = (precio_actual - precio_anterior) / precio_anterior * 100

        if cambio_porcentaje < -2:
            # Compra
            if not posicion_abierta:
                operaciones.append({
                    "accion": "compra",
                    "precio": precio_actual,
                    "indice": i
                })
                posicion_abierta = True

        elif cambio_porcentaje > 3:
            # Venta
            if posicion_abierta:
                operaciones.append({
                    "accion": "venta",
                    "precio": precio_actual,
                    "indice": i
                })
                posicion_abierta = False

    return operaciones

# Ejemplo de uso
precios = [100, 97, 99, 103, 106, 104, 108, 107]
operaciones = bot_inversion_simple(precios)
print(operaciones)