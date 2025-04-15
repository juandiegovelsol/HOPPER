def limpiar_valor(valor):
    """Limpia el valor numérico eliminando comas y puntos, y lo convierte en un entero."""
    # Eliminar espacios en blanco
    valor = valor.strip()
    # Reemplazar puntos y comas adecuadamente
    valor = valor.replace('.', '').replace(',', '')
    return int(valor)

filePath = "./" + input("Nombre del archivo .txt:\n-> ") + ".txt"

# Se intenta abrir el archivo
try:
    with open(filePath, "r", encoding="utf-8") as file:
        gastosMensuales = {}
        nombreCategoria = None

        for line in file:
            line = line.strip()  # Limpiar espacios en blanco al inicio y final de la línea
            
            if not line:  # Si la línea está vacía, continuar
                continue
                
            # Verificar si la línea es una categoría o un gasto
            if not any(char.isdigit() for char in line):  # No tiene dígitos, por lo tanto, es una categoría
                nombreCategoria = line
                gastosMensuales[nombreCategoria] = 0
            else:  # Debe ser un gasto
                try:
                    valor_gasto = limpiar_valor(line)
                    if nombreCategoria:  # Asegurarse de que haya una categoría
                        if nombreCategoria in gastosMensuales:
                            gastosMensuales[nombreCategoria] += valor_gasto
                        else:
                            gastosMensuales[nombreCategoria] = valor_gasto
                except ValueError:
                    print(f"Error al procesar el gasto: {line}")

except FileNotFoundError:
    print("El archivo no fue encontrado. Asegúrate de que la ruta y el nombre del archivo sean correctos.")
    exit(1)

# Calcular y mostrar resultados
totalMensual = sum(gastosMensuales.values())  # Sumar todas las categorías

print("\nGastos por categoría:")
for key, value in gastosMensuales.items():
    print(f"{key}: {value}")

print(f"\nEl total del mes es: {totalMensual}\n")