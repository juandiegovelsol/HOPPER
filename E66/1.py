import json
import os

def fasta_a_json(archivo_fasta):
    """
    Convierte un archivo FASTA a formato JSON, estructurando las secuencias por especie.

    Parámetros:
    archivo_fasta (str): Ruta al archivo FASTA que contiene las secuencias genéticas.

    Retorna:
    dict: Un diccionario en formato JSON que contiene las secuencias organizadas por especie.
    """
    contenido = {}
    
    if not os.path.exists(archivo_fasta):
        raise FileNotFoundError(f"El archivo {archivo_fasta} no existe.")
    
    with open(archivo_fasta, 'r') as file:
        current_species = None
        current_sequence = ""
        
        for line in file:
            line = line.strip()
            
            if not line:
                continue  # Ignora líneas vacías
            
            if line.startswith('>'):
                if current_species:
                    contenido[current_species] = current_sequence
                # Inicia una nueva especie
                current_species = line[1:]  # El nombre de la especie es todo lo que sigue después del '>'
                current_sequence = ""
            else:
                # Acumula los nucleótidos de la secuencia
                current_sequence += line
        
        # Asegúrate de guardar la última secuencia si no se cerró un bloque de especies
        if current_species:
            contenido[current_species] = current_sequence
    
    return {"gene": os.path.basename(archivo_fasta), "contents": contenido}

# Datos falsos en formato FASTA para prueba
archivo_fasta_prueba = 'prueba.fasta'

# Crear el archivo FASTA de prueba con datos falsos
with open(archivo_fasta_prueba, 'w') as f:
    f.write(">species_A\n")
    f.write("ATGTCAAAATTTGTTTTCGATAGTATGCTGCCAAAGTATCCACAGTTCCAGCCGTTTATCAGTTCG\n")
    f.write(">species_B\n")
    f.write("ATGTCAAAATTTGTTTTCGATAGTATGCTGCCAAAGTATCCACAGTTCCAGCCGTTTATCAGTTCG\n")
    f.write(">species_C\n")
    f.write("------------------------ATGCTGCCAAAGTATCCACAGTTCCAGCCGTTTATCAGTTCG\n")
    f.write(">species_D\n")
    f.write("ATGTCAAAATTTGTTTTCGATAGTATGCTGCCAAAGTATCCACAGTTCCAGCCGTTTATCAGTTCG\n")

# Convertir FASTA a JSON
resultado_json = fasta_a_json(archivo_fasta_prueba)

# Imprimir el resultado en formato JSON
print(json.dumps(resultado_json, indent=4))