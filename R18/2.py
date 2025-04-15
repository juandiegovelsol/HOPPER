class Venta:
    """Representa una venta en la tienda de electrónica."""

    def __init__(self, producto, cantidad, precio_unitario):
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.total = self.calcular_total()

    def calcular_total(self):
        """Calcula el total de la venta para un producto determinado."""
        return self.cantidad * self.precio_unitario


class GestorVentas:
    """Gestiona las ventas de la tienda de electrónica."""

    def __init__(self):
        self.ventas = []

    def agregar_venta(self, producto, cantidad, precio_unitario):
        """Agrega una nueva venta al gestor."""
        venta = Venta(producto, cantidad, precio_unitario)
        self.ventas.append(venta)

    def mostrar_resumen_ventas(self):
        """Muestra un resumen detallado de todas las ventas."""
        print("Resumen de Ventas:")
        total_general = 0
        for venta in self.ventas:
            self.imprimir_venta_detalle(venta)
            total_general += venta.total
        print(f"Total General de Ventas: {total_general} CLP")

    def imprimir_venta_detalle(self, venta):
        """Imprime los detalles de una venta individual."""
        print(f"Producto: {venta.producto} | "
              f"Cantidad: {venta.cantidad} | "
              f"Precio Unitario: {venta.precio_unitario} CLP | "
              f"Total: {venta.total} CLP")


# Ejemplo de uso
gestor = GestorVentas()
gestor.agregar_venta("Teclado", 2, 12500)
gestor.agregar_venta("Mouse", 3, 4500)
gestor.agregar_venta("Monitor", 1, 99990)

gestor.mostrar_resumen_ventas()