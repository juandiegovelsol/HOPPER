def calcular_mediana(numeros):
    if not numeros: 
        return "Lista vacía"
    
    # Verificar si todos los elementos en la lista son números
    if not all(isinstance(x, (int, float)) for x in numeros):
        return "Lista contiene elementos no numéricos"
    
    n = len(numeros)
    numeros.sort()  # Modifica la lista en el lugar
    
    if n % 2 == 0:  # Verifica si el número de elementos es par
        mediana = (numeros[n//2] + numeros[n//2 - 1]) / 2
    else:
        mediana = numeros[n//2]  # Si es impar, toma el elemento medio
    
    return mediana

# Prueba del código
listas_prueba = [
    [7, 3, 1, 9, 5],
    [8, 2, 4, 10, 6, 12],
    [],
    ["a", 2, 3] 
]

for lista in listas_prueba:
    print(f"Mediana de {lista}: {calcular_mediana(lista)}")