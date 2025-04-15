import re

def procesar_nombres(entrada):
    try:
        # Verificar que la entrada sea una cadena
        if not isinstance(entrada, str):
            raise ValueError("La entrada debe ser una cadena de texto.")

        # Separar los nombres por comas 
        nombres = [n.strip() for n in entrada.split(",") if n.strip()]
        
        # Verificar si hay nombres en la lista
        if not nombres:
            raise ValueError("No se ha introducido ningún nombre.") 
        if len(nombres) > 100: 
            raise ValueError("Se ha superado el límite de nombres. Como máximo, introduce 100 nombres.") 

        # Validar el formato de los nombres
        nombres_procesados = []
        for nombre in nombres:
            partes = nombre.split()
            if len(partes) < 2:
                raise ValueError(f"El nombre '{nombre}' no tiene apellidos.")
            nombres_procesados.append((partes[-1], nombre)) 
        
        print(nombres_procesados)
        # Ordenar por apellido
        nombres_ordenados = sorted(nombres_procesados, key=lambda x: x[0])

        print(nombres_ordenados)

        # Calcular medidas
        longitudes = [len(n[1]) for n in nombres_ordenados]
        palabras_por_nombre = [len(n[1].split()) for n in nombres_ordenados]
        longitud_media = sum(longitudes) / len(nombres_ordenados)
        palabras_media = sum(palabras_por_nombre) / len(nombres_ordenados)
        nombre_mas_corto = min(nombres_ordenados, key=lambda x: len(x[1]))[1]
        nombre_mas_largo = max(nombres_ordenados, key=lambda x: len(x[1]))[1]

        # Mostrar resultados
        print("\nNombres ordenados por apellidos:")
        for _, nombre in nombres_ordenados:
            print(nombre)

        print(f"\nLongitud media de los nombres: {longitud_media:.2f} letras.") 
        print(f"Media de palabras por nombre: {palabras_media:.2f}.") 
        print(f"Nombre más corto: {nombre_mas_corto}.")
        print(f"Nombre más largo: {nombre_mas_largo}.")

    except ValueError as e:
        print(f"Ha habido un error de valor: {e}") 

# Ejemplo de uso
entrada = input("Introduzca hasta 100 nombres y apellidos separados por comas: ") 
procesar_nombres(entrada)