def menu():
    print("\n--- Menú Principal ---")
    print("1) Saludar")
    print("2) Suma acumulada")
    print("3) Gritar una frase")
    print("4) Salir del programa")

def saludo():
    nombre = input("¿Cuál es tu nombre? ")
    print(f"¡Hola, {nombre}!")

def suma_acumulada():
    while True:
        try:
            num = int(input("Ingresa un número positivo: "))
            if num < 0:
                raise ValueError("El número debe ser positivo.")
            total = sum(range(num + 1))
            print(f"La suma desde 0 hasta {num} es {total}")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}. Intenta de nuevo.")

def gritar():
    frase = input("¿Qué vas a gritar? ")
    print(frase.upper())

def main():
    while True:
        menu()
        opcion = input("Selecciona una opción (1-4): ").strip()
        
        if opcion == '1':
            saludo()
        elif opcion == '2':
            suma_acumulada()
        elif opcion == '3':
            gritar()
        elif opcion == '4':
            print("Programa terminado")
            break
        else:
            print("Opción incorrecta, intenta de nuevo.")
        
        print()  # Salto de línea adicional para separar las iteraciones del menú

main()