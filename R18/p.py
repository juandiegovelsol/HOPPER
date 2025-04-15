ventas_globales = []

def agregar_venta(producto, cantidad, precio_unitario):

    total = cantidad * precio_unitario
    ventas_globales.append({
        "producto": producto,
        "cantidad": cantidad,
        "precio_unitario": precio_unitario,
        "total": total
    })

def mostrar_resumen_ventas():

    print("Resumen de Ventas:")
    total_general = 0
    for venta in ventas_globales:
        print(f"Producto: {venta['producto']} | "
              f"Cantidad: {venta['cantidad']} | "
              f"Precio Unitario: {venta['precio_unitario']} CLP | "
              f"Total: {venta['total']} CLP")
        total_general += venta['total']
    print(f"Total General de Ventas: {total_general} CLP")

# Ejemplo de uso
agregar_venta("Teclado", 2, 12500)
agregar_venta("Mouse", 3, 4500)
agregar_venta("Monitor", 1, 99990)

mostrar_resumen_ventas()