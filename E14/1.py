import json

# Datos en formato de texto
datos_texto = """
variedad uva: malbec, ph suelo: 6.5, análisis mosto: [ph: 4.0, acidez: 0.5 g/l, azúcares: 150 g/l], 
producción: 1000 kg/ha, fermentación: [temperatura: 20°C, duración: 20 días, levadura: Saccharomyces cerevisiae], 
cultivo: [plantación: verano, riego: verano], resultados cata: [visual: rojo teja, olfativa: [frutal, madera], gustativa: [amargo]]
"""

# Parsear los datos del texto
datos = json.loads(datos_texto)

# Crear un diccionario JSON con la estructura requerida
datos_json = {}
for clave, valor in datos.items():
    # Dividir la clave en variedad y otras propiedades
    try:
        variedad, resto = clave.split(': ', 1)
    except ValueError:
        continue  # En caso de que la clave no tenga el formato esperado
    
    # Organizar el resto en un diccionario anidado
    propiedades = {}
    if ',' in resto:
        for subclave, subvalor in (pair.split(': ', 1) for pair in resto.split(',')):
            propiedades[subclave.strip()] = subvalor.strip()
    else:
        propiedades = {resto.strip(): ''}
    
    # Agregar la variedad y sus propiedades al diccionario JSON
    datos_json[variedad.strip()] = propiedades

# Convertir el diccionario a JSON y formatear
json_final = json.dumps(datos_json, indent=4, ensure_ascii=False)

# Imprimir el JSON resultante
print(json_final)