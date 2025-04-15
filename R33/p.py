def orden_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j] = lista[j + 1]
                lista[j + 1] = lista[j]
    return lista

def orden_quick(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[0]
    izquierda = [x for x in lista if x < pivot]
    derecha = [x for x in lista if x > pivot]
    return orden_quick(izquierda) + [pivot] + orden_quick(derecha)

def main():
    try:
        lista_numeros = list(map(int, input("Ingrese una lista de números enteros separados por comas: ").split()))
    except ValueError:
        print("Error en el ingreso de datos. Debes ingresar solo números enteros.")
        return
    lista_burbuja = orden_burbuja(lista_numeros.copy())
    lista_quick_result = orden_quick(lista_numeros)
    if lista_burbuja != lista_quick_result:
        print("Discrepancia encontrada en el ordenamiento:")
        print("Bubble Sort:", lista_burbuja)
        print("Quick Sort:", lista_quick_result)
    else:
        print("Ambos métodos generaron la misma lista ordenada:")
        print(lista_burbuja)

if __name__ == "__main__":
    main()