class Manejadordeinventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, identificador, nombre, cantidad, precio):
        """Agrega un nuevo producto al inventario."""
        producto = {
            'identificador': identificador,
            'nombre': nombre,
            'cantidad': cantidad,
            'precio': precio
        }
        self.productos.append(producto)

    def actualizar_stock(self, identificador, cantidad_nueva):
        """Actualiza la cantidad en stock de un producto dado su identificador."""
        for producto in self.productos:
            if producto['identificador'] == identificador:
                producto['cantidad'] = cantidad_nueva
                print(f"Stock actualizado para {producto['nombre']}.")
                return
        print(f"Producto con identificador {identificador} no encontrado.")

    def buscar_productos_por_precio(self, precio_minimo, precio_maximo):
        """Devuelve una lista de productos cuyo precio está en el rango especificado, ordenados de mayor a menor precio."""
        productos_filtrados = [p for p in self.productos if precio_minimo <= p['precio'] <= precio_maximo]
        productos_ordenados = sorted(productos_filtrados, key=lambda x: x['precio'], reverse=True)
        return productos_ordenados

    def obtener_productos_bajo_stock(self, umbral_bajo_stock):
        """Devuelve una lista de productos cuyo stock está por debajo del umbral definido."""
        productos_bajo_stock = [p for p in self.productos if p['cantidad'] < umbral_bajo_stock]
        return productos_bajo_stock

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        for producto in self.productos:
            print(f"ID: {producto['identificador']}, Nombre: {producto['nombre']}, "
                  f"Cantidad: {producto['cantidad']}, Precio: {producto['precio']}")


# Ejemplo de uso
if __name__ == "__main__":
    umbral_bajo_stock = 10  # Ejemplo de umbral para bajo stock

    manejador = Manejadordeinventario()
    manejador.agregar_producto(1, 'Producto A', 5, 15.50)
    manejador.agregar_producto(2, 'Producto B', 20, 5.50)
    manejador.agregar_producto(3, 'Producto C', 7, 15.00)

    print("Inventario completo:")
    manejador.mostrar_inventario()

    print("\nProductos con bajo stock:")
    productos_bajo_stock = manejador.obtener_productos_bajo_stock(umbral_bajo_stock)
    for producto in productos_bajo_stock:
        print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}")

    print("\nBuscar productos entre precios 10 y 20:")
    productos_filtrados = manejador.buscar_productos_por_precio(10, 20)
    for producto in productos_filtrados:
        print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}")