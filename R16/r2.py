import matplotlib.pyplot as plt

# Categorías predefinidas
CATEGORIAS_INGRESOS = ["Sueldo", "Freelance", "Inversiones", "Regalos", "Otros"]
CATEGORIAS_GASTOS = ["Arriendo", "Comida", "Transporte", "Entretenimiento", "Servicios", "Otros"]

# Diccionarios para acumular totales
ingresos = {categoria: 0 for categoria in CATEGORIAS_INGRESOS}
gastos = {categoria: 0 for categoria in CATEGORIAS_GASTOS}

def ingresar_ingreso():
    print("\n--- Ingresar Ingreso ---")
    categoria = input("Categoría del ingreso (seleccione una de las siguientes): " + 
                      ", ".join(CATEGORIAS_INGRESOS) + ": ")
    if categoria in ingresos:
        monto = float(input("Ingrese el monto del ingreso: "))
        ingresos[categoria] += monto
        print(f"Ingreso de ${monto} en la categoría '{categoria}' registrado.")
    else:
        print("Categoría inválida. Intentelo de nuevo.")

def ingresar_gasto():
    print("\n--- Ingresar Gasto ---")
    categoria = input("Categoría del gasto (seleccione una de las siguientes): " + 
                      ", ".join(CATEGORIAS_GASTOS) + ": ")
    if categoria in gastos:
        monto = float(input("Ingrese el monto del gasto: "))
        gastos[categoria] += monto
        print(f"Gasto de ${monto} en la categoría '{categoria}' registrado.")
    else:
        print("Categoría inválida. Intentelo de nuevo.")

def generar_reporte():
    print("\n--- Reporte Financiero ---")
    
    # Calcular el saldo disponible
    saldo_disponible = sum(ingresos.values()) - sum(gastos.values())
    
    # Mostrar ingresos y gastos
    print("\nIngresos:")
    for categoria, total in ingresos.items():
        print(f"  {categoria}: ${total}")
    
    print("\nGastos:")
    for categoria, total in gastos.items():
        print(f"  {categoria}: ${total}")
    
    # Mostrar saldo
    print(f"\nSaldo disponible: ${saldo_disponible}")
    if saldo_disponible < 0:
        print("¡Advertencia: Saldo negativo!")

    # Gráfico de distribución de gastos
    categorias_gastos = list(gastos.keys())
    montos_gastos = [gastos[categoria] for categoria in categorias_gastos]
    
    plt.figure(figsize=(10, 5))
    plt.bar(categorias_gastos, montos_gastos, color='orange')
    plt.title('Distribución de Gastos')
    plt.xlabel('Categorías')
    plt.ylabel('Monto (USD)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Ingresar Ingreso")
        print("2. Ingresar Gasto")
        print("3. Generar Reporte y Gráfico")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            ingresar_ingreso()
        elif opcion == "2":
            ingresar_gasto()
        elif opcion == "3":
            generar_reporte()
        elif opcion == "4":
            print("Gracias por usar el programa de gestión financiera. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intentelo de nuevo.")

# Ejecutar el programa
menu()