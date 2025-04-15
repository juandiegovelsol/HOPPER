def invertir_cadena(texto):
    invertida = ""
    for i in range(len(texto)):
        invertida += texto[i]
    return invertida

print(invertir_cadena("Armagedon"))  # Debería devolver "modegamrA"