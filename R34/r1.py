def contar_palabras(texto):
    palabras = texto.lower().split()
    contador = {}
    for palabra in palabras:
        palabra = palabra.strip('.,!?¿¡":;()[]{}') 
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    return contador