class Venta:
    """Clase para representar una venta de un producto en la tienda."""
    
    def __init__(self, producto, cantidad, precio_unitario):
        """
        Inicializa una nueva instancia de Venta.

        Args:
            producto (str): El nombre del producto vendido.
            cantidad (int): La cantidad de productos vendidos.
            precio_unitario (float): El precio unitario del producto en CLP.
        """
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.total = self.calcular_total()
    
    def calcular_total(self):
        """Calcula el total de la venta."""
        return self.cantidad * self.precio_unitario


class GestionVentas:
    """Clase para gestionar las ventas en la tienda."""

    def __init__(self):
        """Inicializa la gestión de ventas con una lista vacía."""
        self.ventas = []

    def agregar_venta(self, producto, cantidad, precio_unitario):
        """
        Agrega una nueva venta a la lista de ventas.

        Args:
            producto (str): El nombre del producto vendido.
            cantidad (int): La cantidad de productos vendidos.
            precio_unitario (float): El precio unitario del producto en CLP.
        """
        venta = Venta(producto, cantidad, precio_unitario)
        self.ventas.append(venta)

    def mostrar_resumen_ventas(self):
        """Muestra un resumen de todas las ventas realizadas."""
        print("Resumen de Ventas:")
        total_general = 0

        for venta in self.ventas:
            print(f"Producto: {venta.producto} | "
                  f"Cantidad: {venta.cantidad} | "
                  f"Precio Unitario: {venta.precio_unitario} CLP | "
                  f"Total: {venta.total} CLP")
            total_general += venta.total
        
        print(f"Total General de Ventas: {total_general} CLP")


# Ejemplo de uso
if __name__ == '__main__':
    gestion_ventas = GestionVentas()
    gestion_ventas.agregar_venta("Teclado", 2, 12500)
    gestion_ventas.agregar_venta("Mouse", 3, 4500)
    gestion_ventas.agregar_venta("Monitor", 1, 99990)

    gestion_ventas.mostrar_resumen_ventas()