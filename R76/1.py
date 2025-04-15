def calcular_mediana(numeros):
    if not numeros: 
        return "Lista vacía"  
    
    n = len(numeros)
    
    # Error 1: No se debe llamar al método sort() directamente sin asignarlo a una variable
    numeros.sort()  
    
    if n % 2 == 0: 
        mediana = (numeros[n//2 - 1] + numeros[n//2]) / 2
    else:
        mediana = numeros[n//2] 
    
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