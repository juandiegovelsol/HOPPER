from datetime import datetime

def procesar_facturas(facturas):
    """
    Procesa una lista de facturas y retorna una lista de facturas 
    preparadas para su uso.

    Args:
        facturas (list): Lista de facturas, donde cada factura es un diccionario
                         con claves 'cliente', 'fecha_vencimiento', y 'monto'.

    Returns:
        list: Lista de facturas preparadas para ser ordenadas o sumadas.
    """
    facturas_preparadas = []
    for factura in facturas:
        try:
            fecha_vencimiento = datetime.strptime(factura['fecha_vencimiento'], '%m-%d-%Y')
            monto = float(factura['monto'])
            facturas_preparadas.append({
                'cliente': factura['cliente'],
                'fecha_vencimiento': fecha_vencimiento,
                'monto': monto
            })
        except ValueError as e:
            print(f"Error al procesar la factura: {e}")
    return facturas_preparadas

def ordenar_facturas_por_vencimiento(facturas):
    """
    Ordena una lista de facturas por su fecha de vencimiento.

    Args:
        facturas (list): Lista de facturas procesadas, con la clave 'fecha_vencimiento'.

    Returns:
        list: Lista de facturas ordenadas por fecha de vencimiento.
    """
    return sorted(facturas, key=lambda x: x['fecha_vencimiento'])

def calcular_total_facturas(facturas):
    """
    Calcula el total del monto de una lista de facturas.

    Args:
        facturas (list): Lista de facturas procesadas, con la clave 'monto'.

    Returns:
        float: Suma total del monto de las facturas.
    """
    return sum(factura['monto'] for factura in facturas)

def imprimir_facturas(facturas):
    """
    Imprime la información de las facturas.

    Args:
        facturas (list): Lista de facturas procesadas.
    """
    for factura in facturas:
        print(f"Cliente: {factura['cliente']}, Vencimiento: {factura['fecha_vencimiento'].strftime('%m-%d-%Y')}, Monto: ${factura['monto']}")

# Ejemplo de uso
facturas = [
    {'cliente': 'Cliente A', 'fecha_vencimiento': '1-31-2020', 'monto': 200},
    {'cliente': 'Cliente B', 'fecha_vencimiento': '1-1-2020', 'monto': 100}
]

facturas_procesadas = procesar_facturas(facturas)

if facturas_procesadas:
    facturas_ordenadas = ordenar_facturas_por_vencimiento(facturas_procesadas)
    imprimir_facturas(facturas_ordenadas)
    
    total_facturas = calcular_total_facturas(facturas_procesadas)
    print(f"El total de las facturas es: ${total_facturas:.2f} dólares.")
else:
    print("No hay facturas válidas para procesar.")