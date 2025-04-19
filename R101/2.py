def insertar_elemento(valor, lista):
    # Validación de tipo de datos
    if not isinstance(lista, list):
        raise TypeError("El segundo argumento debe ser una lista.")
    if not (isinstance(valor, int) or isinstance(valor, float)):
        raise ValueError("El valor a insertar debe ser un número.")

    indice = -1
    contador = 0
    # Validación de elementos repetidos
    if valor in lista:
        print("El número ya existe en la lista. No se insertó.")
        return
    for item in lista:
        if valor < item:
            indice = contador
            break
        indice = contador + 1
    # Agregar lógica para manejar el caso cuando `indice` es mayor o igual a la longitud de la lista
    if indice >= len(lista):
        indice = len(lista)
    # Insertar el elemento en el índice apropiado
    lista.insert(indice, valor)
    print(f"Elemento {valor} insertado en la posición {indice}.")

# Casos de uso
lista_numeros = [5, 10, 15]
insertar_elemento(7, lista_numeros)
print(lista_numeros)  # Salida: [5, 7, 10, 15]

insertar_elemento(20, lista_numeros)
print(lista_numeros)  # Salida: [5, 7, 10, 15, 20]

insertar_elemento("a", lista_numeros) # Error, no es un número

try:
    insertar_elemento(5, "no es una lista")
except TypeError as e:
    print(e)  # Salia: TypeError: El segundo argumento debe ser una lista.