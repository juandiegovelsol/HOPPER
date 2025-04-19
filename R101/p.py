def insertar_elemento(valor, lista):
    indice = -1
    contador = 0
    for item in lista:
        if (valor > item):
            indice = contador
        contador = contador + 1
    if (len(lista) ==0):
        lista.insert(indice,valor)
        return
    if (indice>=0):
        lista.insert(indice,valor)
        return
    

lista = [2, 3, 7, 9]
insertar_elemento(4, lista)  # El número 4 se insertará entre 3 y 7
print(lista)  # Salida: [2, 3, 4, 7, 9]