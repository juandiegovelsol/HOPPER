def calcular_precio_final(precio, descuento, impuesto_ventas):
    """
    Calcula el precio final de un producto aplicando un descuento y luego agregando el impuesto sobre las ventas.
    
    :param precio: Precio base del producto (float).
    :param descuento: Porcentaje de descuento a aplicar (ej. 0.10 para 10%).
    :param impuesto_ventas: Porcentaje de impuesto sobre las ventas a agregar (ej. 0.16 para 16%).
    :return: Precio final después de aplicar el descuento y sumar el impuesto sobre las ventas.
    """
    precio_descuento = precio * (1 - descuento)
    precio_final = precio_descuento * (1 + impuesto_ventas)
    return precio_final

if __name__ == "__main__":
    # Caso de Prueba 1: Producto de $100, con 10% de descuento y 16% de impuesto sobre las ventas.
    precio1 = 100.0
    descuento1 = 0.10   # 10% de descuento
    impuesto1 = 0.16    # 16% de impuesto sobre las ventas
    resultado1 = calcular_precio_final(precio1, descuento1, impuesto1)
    print("Caso de Prueba 1 - Precio final:", resultado1)
    
    # Caso de Prueba 2: Producto de $250, con 20% de descuento y 16% de impuesto sobre las ventas.
    precio2 = 250.0
    descuento2 = 0.20   # 20% de descuento
    impuesto2 = 0.16    # 16% de impuesto sobre las ventas
    resultado2 = calcular_precio_final(precio2, descuento2, impuesto2)
    print("Caso de Prueba 2 - Precio final:", resultado2)
    
    # Caso de Prueba 3: Producto de $50, sin descuento y con 16% de impuesto sobre las ventas.
    precio3 = 50.0
    descuento3 = 0.0    # Sin descuento
    impuesto3 = 0.16    # 16% de impuesto sobre las ventas
    resultado3 = calcular_precio_final(precio3, descuento3, impuesto3)
    print("Caso de Prueba 3 - Precio final:", resultado3)