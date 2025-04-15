def factorial(n):
    if not isinstance(n, int) or n < 0:
        print("ERROR: El valor debe ser un número entero positivo") 
        return None 

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

#pruebas
factorial(0) # resultado : 1
factorial(1) # resultado : 1
factorial(-5) # resultado : "El valor debe ser un número entero positivo"
factorial(5.5) # resultado : "El valor debe ser un número entero positivo"
factorial(10) # resultado : 3628800