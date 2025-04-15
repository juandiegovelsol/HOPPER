filePath = "./" + input("nombre del archivo .txt:\n-> ") + ".txt"

file = open(filePath, "r", encoding="utf-8")

line = file.readline()

gastosMensuales = {}

while line != "":
    line = line.strip()

    # Intentamos convertir a número, eliminando posibles separadores de miles
    try:
        # Elimina separadores de miles usando replace
        numero = line.replace('.', '').replace(',', '').replace(' ', '') 
        # Convertir a float
        valor = float(numero)
        
        # Sumamos al último nombre de categoría conocido
        gastosMensuales[nombreCategoria] += valor
    except ValueError:
        # Si no es un número, consideramos que es el nombre de la categoría
        nombreCategoria = line
        gastosMensuales[nombreCategoria] = 0.0
        
    line = file.readline()

file.close()

# Calcular el total mensual
totalMensual = sum(gastosMensuales.values())

print("\nGastos por categoría:")
for key in gastosMensuales:
    print(f"{key}: {gastosMensuales[key]:.2f}")

print(f"\nEl total del mes es: {totalMensual:.2f}\n")