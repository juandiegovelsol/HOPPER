import json
import re

# Función para leer el archivo FASTA y extraer la información
def read_fasta(file_path):
    with open(file_path, 'r') as file:
        content = file.read().strip()

    # Regex para encontrar secuencias en un archivo FASTA
    fasta_pattern = re.compile(r'>(\w+)\s+(\w+)')
    species_dict = {}

    for match in fasta_pattern.finditer(content):
        species_name = match.group(1)
        sequence = match.group(2)
        species_dict[species_name] = sequence

    return species_dict

# Función para convertir el diccionario de secuencias a JSON
def to_json(species_dict, file_name):
    data = {
        "gene": file_name,
        "contents": species_dict
    }

    with open(file_name.replace('.fasta', '.json'), 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Ejemplo de uso
fasta_file = 'drosophila_genes.fasta'
species_dict = read_fasta(fasta_file)
to_json(species_dict, fasta_file)