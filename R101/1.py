def insertar_elemento(valor, lista):
    # Inicializar el índice en -1 para indicar que no se ha encontrado una posición válida
    indice = -1
    # Verificar que 'lista' sea una lista
    if not isinstance(lista, list):
        raise TypeError("El segundo argumento debe ser una lista")
    # Verificar que 'valor' sea un número (int o float)
    if not isinstance(valor, (int, float)):
        raise TypeError("El primer argumento debe ser un número")

    contador = 0
    for item in lista:
        # Verificar que 'item' sea un número
        if not isinstance(item, (int, float)):
            raise TypeError("Todos los elementos de la lista deben ser números")
        # Identificar la posición donde el 'valor' es mayor que el elemento 'item' de la lista
        if valor < item:
            indice = contador
            break
        contador += 1

    # Insertar el 'valor' en la posición identificada si se encontró una posición válida
    if indice != -1:
        lista.insert(indice, valor)
    else:
        # Si no se encontró una posición, insertar el 'valor' al final de la lista
        lista.append(valor)

# Casos de uso
lista = [2, 3, 7, 9]
insertar_elemento(1, lista)  # El número 4 se insertará entre 3 y 7
print(lista)  # Salida: [2, 3, 4, 7, 9]

insertar_elemento(10, lista)  # El número 10 se agregará al final de la lista
print(lista)  # Salida: [2, 3, 4, 7, 9, 10]

insertar_elemento(5.5, lista)  # El número 5.5 se insertará entre 4 y 7
print(lista)  # Salida: [2, 3, 4, 5.5, 7, 9, 10]