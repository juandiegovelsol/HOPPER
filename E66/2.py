import json
import os

def fasta_to_json(fasta_file):
    # Diccionario para almacenar el contenido del archivo FASTA
    contents = {}
    
    # Abrir el archivo FASTA en modo lectura
    with open(fasta_file, 'r') as file:
        # Leer el nombre del gen (el primer línea sin contenido)
        header = file.readline().strip()
        
        # Leer secuencias de nucleótidos hasta que se encuentre un nuevo nombre de gen
        sequence = []
        while True:
            line = file.readline().strip()
            if not line:  # Fin del archivo o nuevo nombre de gen
                if header not in contents:
                    contents[header] = ''.join(sequence)
                sequence = []
                header = line
            else:
                sequence.append(line)
        
        # Añadir la última secuencia si no se encuentra un nuevo nombre de gen al final
        if header not in contents:
            contents[header] = ''.join(sequence)
    
    # Crear el diccionario final con el nombre del archivo como clave para el gen
    gene = os.path.basename(fasta_file)
    result = {
        "gene": gene,
        "contents": contents
    }
    
    # Guardar el resultado en un archivo JSON
    with open(f'{gene}.json', 'w') as json_file:
        json.dump(result, json_file, indent=4)
    
    return result

# Ejemplo de uso
fasta_file = 'example.fasta'
json_output = fasta_to_json(fasta_file)
print(json.dumps(json_output, indent=4))