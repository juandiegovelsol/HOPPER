import json
import os

def fasta_to_json(fasta_file_path):
    """
    Convierte un archivo FASTA en un diccionario JSON con las secuencias de nucleótidos por especie.

    Args:
    fasta_file_path (str): Ruta al archivo FASTA a convertir.

    Returns:
    dict: Diccionario JSON con las secuencias de nucleótidos por especie.
    """
    contents = {}

    # Abre el archivo FASTA en modo lectura
    with open(fasta_file_path, 'r') as file:
        current_species = None
        current_sequence = ""

        # Lee cada línea del archivo FASTA
        for line in file:
            line = line.strip()

            # Si la línea comienza con '>', es un nuevo gen
            if line.startswith('>'):
                if current_species:
                    # Agrega la secuencia de la especie actual al diccionario
                    contents[current_species] = current_sequence
                # Actualiza el nombre de la especie y reinicia la secuencia
                current_species = line[1:]  # Elimina el '>'
                current_sequence = ""
            else:
                # Si la línea no comienza con '>', es una secuencia de nucleótidos
                current_sequence += line

        # Agrega la secuencia de la última especie
        if current_species:
            contents[current_species] = current_sequence

    return contents

def save_to_json(data, output_file_path):
    """
    Guarda los datos en un archivo JSON.

    Args:
    data (dict): Datos a guardar en el archivo JSON.
    output_file_path (str): Ruta al archivo JSON de salida.
    """
    with open(output_file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Datos de prueba
fasta_data = {
    "species_A": "ATGTCAAAATTTGTTTTCGATAGTATGCTGCCAAAGTATCCACAGTTCCAGCCGTTTATCAGTTCG",
    "species_B": "ATGTCAAAATTTGTTTTCGATAGTATGCTGCCAAAGTATCCACAGTTCCAGCCGTTTATCAGTTCG",
    "species_C": "------------------------ATGCTGCCAAAGTATCCACAGTTCCAGCCGTTTATCAGTTCG",
    "species_D": "ATGTCAAAATTTGTTTTCGATAGTATGCTGCCAAAGTATCCACAGTTCCAGCCGTTTATCAGTTCG"
}

# Ruta al archivo FASTA de prueba
fasta_file_path = 'test.fasta'

# Crea el archivo FASTA de prueba
with open(fasta_file_path, 'w') as file:
    for species, sequence in fasta_data.items():
        file.write(f">{species}\n{sequence}\n")

# Convierte el archivo FASTA a JSON
json_data = fasta_to_json(fasta_file_path)

# Guarda los datos en un archivo JSON
save_to_json(json_data, 'output.json')