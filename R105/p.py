def menu():
    print("\n--- Menu Principal ---")
    print("1) Saludar")
    print("2) Suma acumulada")
    print("3) Gritar una frase")
    print("4) Salir del programa")
    
def saludo():
    nombre = input("¿Cual es tu nombre?")
    print("¡Hola, " + nombre + "!")
    
def suma_acumulada():
	num = input("Ingresa un numero positivo")
	total = 0
	for i in range(num + 1):
		total +=  i
	print("La suma desde 0 hasta "+ num + " es " + total)
 
def gritar():
    frase = input("¿Que vas a gritar?")
    print(frase.capitalize())
    
def main():
    while True:
        menu()
        opcion = input("Selecciona una opción (1-4):")
        
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
            print("Opción incorrecta")
            
main()