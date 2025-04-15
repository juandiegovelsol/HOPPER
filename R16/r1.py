import matplotlib.pyplot as plt

# Dicionarios para almacenar ingresos y gastos
ingresos = {'Sueldo': 0, 'Freelance': 0, 'Inversiones': 0, 'Regalos': 0, 'Otros': 0}
gastos = {'Arriendo': 0, 'Comida': 0, 'Transporte': 0, 'Entretenimiento': 0, 'Servicios': 0, 'Otros': 0}

def registrar_ingreso():
    print("\nCategorías de Ingresos: Sueldo, Freelance, Inversiones, Regalos, Otros")
    categoria = input("Ingrese la categoría del ingreso: ")
    monto = float(input("Ingrese el monto del ingreso: "))

    if categoria in ingresos:
        ingresos[categoria] += monto
        print(f"Ingreso registrado: {categoria} -> {monto}")
    else:
        print("Categoría no válida. Intente nuevamente.")

def registrar_gasto():
    print("\nCategorías de Gastos: Arriendo, Comida, Transporte, Entretenimiento, Servicios, Otros")
    categoria = input("Ingrese la categoría del gasto: ")
    monto = float(input("Ingrese el monto del gasto: "))

    if categoria in gastos:
        gastos[categoria] += monto
        print(f"Gasto registrado: {categoria} -> {monto}")
    else:
        print("Categoría no válida. Intente nuevamente.")

def mostrar_reporte():
    total_ingresos = sum(ingresos.values())
    total_gastos = sum(gastos.values())
    saldo = total_ingresos - total_gastos

    print("\nReporte Financiero")
    print("==================")
    print("\nIngresos:")
    for categoria, monto in ingresos.items():
        print(f"{categoria}: {monto}")
    print(f"Total Ingresos: {total_ingresos}")

    print("\nGastos:")
    for categoria, monto in gastos.items():
        print(f"{categoria}: {monto}")
    print(f"Total Gastos: {total_gastos}")

    print(f"\nSaldo Disponible: {saldo}")
    if saldo < 0:
        print("¡Advertencia: su saldo es negativo!")

    # Generar gráfico
    categorias_gastos = list(gastos.keys())
    valores_gastos = list(gastos.values())

    plt.figure(figsize=(8, 6))
    plt.pie(valores_gastos, labels=categorias_gastos, autopct='%1.1f%%', startangle=140)
    plt.title('Distribución de Gastos')
    plt.show()

def main():
    while True:
        print("\nOpciones:")
        print("1. Registrar Ingreso")
        print("2. Registrar Gasto")
        print("3. Mostrar Reporte")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_ingreso()
        elif opcion == '2':
            registrar_gasto()
        elif opcion == '3':
            mostrar_reporte()
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()