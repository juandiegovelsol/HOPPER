import csv
from typing import List, Union

def escribe_en_csv(renglones: List[List[Union[str, int]]], nombre_archivo: str = "calificaciones.csv") -> None:
    """Escribe las calificaciones en un archivo CSV.

    Args:
        renglones: Lista de listas donde cada lista interna contiene el nombre y las calificaciones.
        nombre_archivo: Nombre del archivo CSV donde se escribirán los datos.
    """
    # Definir los encabezados
    encabezados = ["Nombre", "Física", "Matemáticas", "Arte", "Español"]

    # Abrir el archivo CSV para escribir
    try:
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            
            # Escribir los encabezados
            writer.writerow(encabezados)
            
            # Escribir cada renglón en el archivo CSV
            for renglon in renglones:
                # Validar que cada renglón tenga la longitud correcta
                if len(renglon) != len(encabezados):
                    raise ValueError(f"Renglón inválido: {renglon}. Se esperaban {len(encabezados)} elementos.")
                writer.writerow(renglon)
    except IOError as e:
        print(f"Error al escribir en el archivo {nombre_archivo}: {e}")
    except ValueError as e:
        print(f"Error de validación de datos: {e}")

calificaciones = {
    "Alan": {"Física": "A", "Matemáticas": "A", "Arte": "C", "Español": "B",},
    "Edgar": {"Física": "C", "Matemáticas": "C", "Arte": "A", "Español": "C",},
    "Elena": {"Física": "C", "Matemáticas": "B", "Arte": "B", "Español": "A",},
}

orden = ["Física", "Matemáticas", "Arte", "Español"]
nuevos_renglones = list()
for nombre, materias in calificaciones.items():
    nuevo_renglon = [nombre,]
    for materia in orden:
        nuevo_renglon.append(materias[materia])
    nuevos_renglones.append(nuevo_renglon)
        
# Llamar a la función con la lista completa
escribe_en_csv(nuevos_renglones)