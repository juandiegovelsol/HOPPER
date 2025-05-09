from datetime import datetime

def ordenar_facturas_por_vencimiento(facturas):
    """
    Ordena las facturas en orden de su fecha de vencimiento.

    Args:
        facturas (list): Lista de facturas, donde cada factura es una lista con los elementos
                         [cliente, fecha_vencimiento, monto].

    Returns:
        list: Facturas ordenadas por fecha de vencimiento.
    """
    for factura in facturas:
        factura[1] = datetime.strptime(factura[1], '%m-%d-%Y')
    return sorted(facturas, key=lambda x: x[1])

def calcular_total_facturas(facturas):
    """
    Calcula el total de todas las facturas.

    Args:
        facturas (list): Lista de facturas, donde cada factura es una lista con los elementos
                         [cliente, fecha_vencimiento, monto].

    Returns:
        float: Total acumulado de los montos de las facturas.
    """
    total = sum(factura[2] for factura in facturas)
    return total

def imprimir_reporte_facturas(facturas, total, monto_total_previo=0):
    """
    Imprime un reporte de las facturas en orden de vencimiento y el total a pagar.

    Args:
        facturas (list): Lista de facturas ordenadas por vencimiento.
        total (float): Total acumulado de las facturas.
        monto_total_previo (float): Monto total previo a sumar, por si se acumulan varias sumas.
    """
    print("Las facturas en orden de vencimiento son:")
    for factura in facturas:
        print(f"Cliente: {factura[0]}, Vencimiento: {factura[1].strftime('%m-%d-%Y')}, Monto: ${factura[2]}")
        
    monto_total = monto_total_previo + total
    print("El total de las facturas es: $" + str(round(monto_total, 2)) + " dolares.")
    return monto_total

def procesar_facturas(facturas, monto_total_previo=0):
    """
    Función principal que coordina el procesamiento de facturas.
    
    Args:
        facturas (list): Lista de facturas a procesar.
        monto_total_previo (float): Monto total previo a sumar, si se acumulan varias sumas.
    """
    facturas_ordenadas = ordenar_facturas_por_vencimiento(facturas)
    total_facturas = calcular_total_facturas(facturas_ordenadas)
    imprimir_reporte_facturas(facturas_ordenadas, total_facturas, monto_total_previo)

# Ejemplo de uso
facturas = [["Cliente A", "01-31-2020", 200.00], ["Cliente B", "01-01-2020", 100.00]]
procesar_facturas(facturas)

# Acumulando totales
nuevas_facturas = [["Cliente C", "02-15-2020", 150.00]]
procesar_facturas(nuevas_facturas, monto_total_previo=200.00)