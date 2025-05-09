from datetime import datetime
def procesar_facturas(facturas):
    """
    Las facturas llegan como listas de facturas, cada una de esta es tambien una lista de elementos
    El orden de los elementos en cada factura es:
        - Cliente
        - Fecha de vencimiento
        - Monto
    """
    #Imprimir en orden
    print("Las facturas en orden de vencimiento son:")
    for factura in facturas:
        factura[1] = datetime.strptime(factura[1], '%m-%d-%Y')
    print(sorted(facturas, key= lambda x: x[1]))

    #Imprimir monto total
    monto_total = 0
    for factura in facturas: monto_total += factura[2]
    print("El total de las facturas es: $" + str(monto_total) + " dolares.")

#Ejemplo
facturas = [["Cliente A", "1-31-2020", 200],["Cliente B", "1-1-2020", 100]]
procesar_facturas(facturas)