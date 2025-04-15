def contar_palabras(texto):
    palabras = texto.split()
    contador = {}
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    return contador

print(contar_palabras("ab,c ab,c abc AB.C ABC 123 123 1234 123456"))