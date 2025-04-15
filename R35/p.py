def contar_palabras(palabras):
    contador = {}
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] =+ 1
        else:
            contador[palabra] = 1
    return contador

lista = ["manzana", "pera", "manzana", "uva", "pera", "pera"]
print(contar_palabras(lista))