class Organizador:
    def organizar_por_vencimiento(self, productos):
        # Función para convertir la fecha de vencimiento de formato `dd/mm/yyyy` a una tupla (yyyy, mm, dd) para comparar
        def parse_fecha(fecha_str):
            dia, mes, año = map(int, fecha_str.split('/'))
            return (año, mes, dia)
        
        # Implementación de un algoritmo simple de ordenación (insertion sort) para ordenar por fecha
        for i in range(1, len(productos)):
            clave_producto = productos[i]
            clave_fecha = parse_fecha(clave_producto['fechavencimiento'])
            j = i - 1
            while j >= 0 and parse_fecha(productos[j]['fechavencimiento']) > clave_fecha:
                productos[j + 1] = productos[j]
                j -= 1
            productos[j + 1] = clave_producto
        
        return productos

# Ejemplo de uso
productos = [
    {"nombre": "Producto A", "fechavencimiento": "12/12/2023"},
    {"nombre": "Producto B", "fechavencimiento": "08/11/2023"},
    {"nombre": "Producto C", "fechavencimiento": "15/10/2023"},
]

organizador = Organizador()
productos_ordenados = organizador.organizar_por_vencimiento(productos)

for producto in productos_ordenados:
    print(f"Nombre: {producto['nombre']}, Fecha de Vencimiento: {producto['fechavencimiento']}")