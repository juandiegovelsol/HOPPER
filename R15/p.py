def juego_palabras_encadenadas():
    print("Juego de Palabras Encadenadas")
    print("------------------------------")
    print("Reglas: La siguiente palabra debe comenzar con la última letra de la palabra anterior.")
    
    # Pedir la primera palabra
    palabra_anterior = input("Introduce la primera palabra: ").lower()
    
    while True:
        # Pedir la siguiente palabra
        palabra_siguiente = input(f"Introduce una palabra que empiece por '{palabra_anterior[-1]}': ").lower()
        
        # Verificar si la palabra comienza con la letra correcta
        if palabra_siguiente[0] == palabra_anterior[-1]:
            print("¡Correcto! La cadena continúa.")
            palabra_anterior = palabra_siguiente
        else:
            print(f"¡Incorrecto! La palabra no empieza por '{palabra_anterior[-1]}'.")
            print("Juego terminado.")
            break

# Iniciar el juego
juego_palabras_encadenadas()