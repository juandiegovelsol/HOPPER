import ast

def procesar_pedido(pedido):
    try:
        total = 0
        for id_plato, cantidad_deseada in pedido.items():
            if id_plato not in platos:
                raise ValueError(f"El plato con id {id_plato} no existe")
            if cantidad_deseada > platos[id_plato]["cantidad"]:
                raise ValueError(f"Cantidad insuficiente para el plato {id_plato}")
            total += cantidad_deseada * platos[id_plato]["precio"]
        for id_plato, cantidad_deseada in pedido.items():
            platos[id_plato]["cantidad"] -= cantidad_deseada
        print("Total del pedido: $", total)
    except Exception as error:
        print("Error:", error)

platos = {
    1: {"nombre": "Ensalada", "precio": 5.0, "cantidad": 10},
    2: {"nombre": "Hamburguesa", "precio": 10.0, "cantidad": 5},
    3: {"nombre": "Pizza", "precio": 12.0, "cantidad": 8}
}

if __name__ == "__main__":
    try:
        entrada = input("Ingrese el pedido: ")
        pedido = ast.literal_eval(entrada)
        if not isinstance(pedido, dict):
            raise ValueError("La entrada no es un diccionario")
    except Exception as error:
        print("Error en la entrada:", error)
    else:
        procesar_pedido(pedido)