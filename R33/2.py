def orden_burbuja(lista):
    n = len(lista)
    # Recorremos la lista para mover los números más grandes hacia el final
    for i in range(n):
        # Establecemos un par de elementos y los comparamos
        for j in range(0, n - i - 1):
            # Si el elemento actual es mayor que el siguiente, los intercambiamos
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def orden_quick(lista):
    # Si la lista tiene un solo elemento o está vacía, se considera que está ordenada
    if len(lista) <= 1:
        return lista
    # Elegimos el primer elemento como pivote
    pivot = lista[0]
    # Ordenamos los elementos menores al pivote a la izquierda y los mayores a la derecha
    izquierda = [x for x in lista[1:] if x <= pivot]
    derecha = [x for x in lista[1:] if x > pivot]
    # Aplicamos recursivamente el mismo proceso a las sublistas izquierda y derecha
    return orden_quick(izquierda) + [pivot] + orden_quick(derecha)

def main():
    try:
        # Solicitamos al usuario que ingrese una lista de números enteros separados por comas
        lista_numeros = list(map(int, input("Ingrese una lista de números enteros separados por comas: ").split(',')))
    except ValueError:
        # Si se produce un error en la conversión, notificamos al usuario
        print("Error en el ingreso de datos. Debes ingresar solo números enteros.")
        return
    
    # Ordenamos la lista utilizando el algoritmo de burbuja
    lista_burbuja = orden_burbuja(lista_numeros.copy())
    # Ordenamos la lista utilizando el algoritmo QuickSort
    lista_quick_result = orden_quick(lista_numeros.copy())
    
    # Comparamos los resultados de ambos algoritmos
    if lista_burbuja != lista_quick_result:
        print("Discrepancia encontrada en el ordenamiento:")
        print("Bubble Sort:", lista_burbuja)
        print("Quick Sort:", lista_quick_result)
    else:
        print("Ambos métodos generaron la misma lista ordenada:")
        print(lista_burbuja)

if __name__ == "__main__":
    main()