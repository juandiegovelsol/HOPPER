class Producto:
    def __init__(self, identificador, nombre, cantidad, precio):
        self.identificador = identificador
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

class Manejadordeinventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, identificador, nombre, cantidad, precio):
        if identificador in self.productos:
            print(f"El producto con ID {identificador} ya existe.")
        else:
            self.productos[identificador] = Producto(identificador, nombre, cantidad, precio)
            print(f"Producto {nombre} agregado exitosamente.")

    def actualizar_stock(self, identificador, cantidad):
        if identificador in self.productos:
            self.productos[identificador].cantidad = cantidad
            print(f"Stock de producto con ID {identificador} actualizado a {cantidad}.")
        else:
            print(f"Producto con ID {identificador} no encontrado.")
    
    def buscar_por_rango_de_precio(self, precio_min, precio_max):
        productos_en_rango = [prod for prod in self.productos.values() if precio_min <= prod.precio <= precio_max]
        productos_en_rango.sort(key=lambda x: x.precio, reverse=True)
        return productos_en_rango

    def obtener_productos_bajo_stock(self, umbral):
        bajo_stock = [prod for prod in self.productos.values() if prod.cantidad < umbral]
        return bajo_stock

# Ejemplo de uso
inventario = Manejadordeinventario()
inventario.agregar_producto(1, "Producto A", 20, 15.5)
inventario.agregar_producto(2, "Producto B", 5, 15.0)
inventario.agregar_producto(3, "Producto C", 50, 5.0)

# Actualización de stock
inventario.actualizar_stock(2, 3)

# Buscar productos por rango de precio
productos_en_precio = inventario.buscar_por_rango_de_precio(10, 30)
for prod in productos_en_precio:
    print(f"{prod.nombre} - Precio: {prod.precio}")

# Obtener productos con bajo stock
productos_bajo_stock = inventario.obtener_productos_bajo_stock(10)
for prod in productos_bajo_stock:
    print(f"{prod.nombre} tiene bajo stock con una cantidad de {prod.cantidad}.")