def orden_burbuja(lista):
    """
    Ordena una lista utilizando el algoritmo Bubble Sort.
    Este algoritmo itera sobre la lista repetidamente, comparando
    elementos adyacentes y permutándolos si están en el orden incorrecto.
    La pasada se repite hasta que no se necesiten más permutaciones.
    """
    n = len(lista)
    for i in range(n):
        # Control de optimización: si en una pasada completa no se hacen cambios, la lista está ordenada
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  # Intercambio de elementos
    return lista

def orden_quick(lista):
    """
    Ordena una lista utilizando el algoritmo Quick Sort.
    Este algoritmo selecciona un 'pivote' y particiona la lista
    en dos sublistas: elementos menores que el pivote y mayores.
    Luego, ordena recursivamente las sublistas y las combina.
    """
    if len(lista) <= 1:
        return lista
    pivot = lista[0]
    izquierda = [x for x in lista if x < pivot]
    derecha = [x for x in lista if x >= pivot]
    # Recursividad para ordenar las sublistas y combinar resultados
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