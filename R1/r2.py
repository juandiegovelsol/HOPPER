class Organizador:
    def __init__(self):
        pass
    
    def organizar_por_fecha_vencimiento(self, productos):
        # Primero validamos que la lista de productos contiene diccionarios válidos
        for producto in productos:
            if not isinstance(producto, dict) or 'fechavencimiento' not in producto or 'nombre' not in producto:
                raise ValueError("Cada producto debe ser un diccionario con 'nombre' y 'fechavencimiento'")
        
        # Convertimos las fechas de vencimiento a un formato que permita comparación
        # Asumimos que las fechas están en formato 'YYYY-MM-DD'
        try:
            for producto in productos:
                # Dividimos la fecha en partes y la comparamos como un todo
                año, mes, dia = map(int, producto['fechavencimiento'].split('-'))
                producto['fecha_tuple'] = (año, mes, dia)
        except ValueError:
            raise ValueError("Formato de fecha incorrecto. Use YYYY-MM-DD.")
        
        # Ordenamos los productos basándonos en la tupla de fecha
        productos_ordenados = sorted(productos, key=lambda x: x['fecha_tuple'])
        
        # Retornamos la lista ordenada sin las tuplas de fechas
        for producto in productos_ordenados:
            del producto['fecha_tuple']
        
        return productos_ordenados

# Ejemplo de uso
productos = [
    {'nombre': 'Leche', 'fechavencimiento': '2023-12-30'},
    {'nombre': 'Pan', 'fechavencimiento': '2023-10-15'},
    {'nombre': 'Yogur', 'fechavencimiento': '2023-11-01'},
    {'nombre': 'Jugo', 'fechavencimiento': '2023-09-20'},
]

organizador = Organizador()
productos_ordenados = organizador.organizar_por_fecha_vencimiento(productos)
print(productos_ordenados)