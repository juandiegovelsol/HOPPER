def bot_inversion_simple(precios):
    operaciones = []
    i = 1
    while i < len(precios):
        # Calculamos la variación porcentual
        variacion_percentual = (precios[i] - precios[i - 1]) / precios[i - 1] * 100
        
        # Decidir si compramos o vendemos
        if variacion_percentual < -2.0 and 'compra' not in operaciones[-1]:
            # Comprar
            operaciones.append({
                'accion': 'compra',
                'precio': precios[i],
                'indice': i
            })
        elif variacion_percentual > 3.0 and 'venta' not in operaciones[-1]:
            # Vender
            operaciones.append({
                'accion': 'venta',
                'precio': precios[i],
                'indice': i
            })
        
        i += 1
    
    return operaciones


precios_criptomoneda = [100, 95, 110, 115, 108, 125]
operaciones = bot_inversion_simple(precios_criptomoneda)
print(operaciones)