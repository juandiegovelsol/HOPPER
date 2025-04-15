import ast

def procesar_orden(orden):
    try:
        total = 0
        for id_plato, cantidad_deseada in orden.items():
            if id_plato not in platos:
                raise ValueError("El plato con id {} no existe".format(id_plato))
            if cantidad_deseada > platos[id_plato]["cantidad"]:
                raise ValueError("Cantidad insuficiente para el plato {}".format(id_plato))
            total += cantidad_deseada * platos[id_plato]["precio"]
        for id_plato, cantidad_deseada in orden.items():
            platos[id_plato]["cantidad"] -= cantidad_deseada
        print("Total de la orden: $", total)
    except Exception as error:
        print("Error:", error)

platos = {
    1: {"nombre": "Ensalada", "precio": 5.0, "cantidad": 10},
    2: {"nombre": "Hamburguesa", "precio": 10.0, "cantidad": 5},
    3: {"nombre": "Pizza", "precio": 12.0, "cantidad": 8}
}

if __name__ == "__main__":
    while True:
        entrada = input("Ingrese la orden en formato diccionario o 'salir' para terminar: ")
        if entrada.lower() == "salir":
            break
        try:
            orden = ast.literal_eval(entrada)
            if not isinstance(orden, dict):
                raise ValueError("La entrada no es un diccionario")
        except Exception as error:
            print("Error en la entrada:", error)
        else:
            procesar_orden(orden)
