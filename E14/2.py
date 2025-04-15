import json

# Datos en formato texto
datos_texto = """
variedad uva: malbec, ph suelo: 6.5, análisis mosto: [ph: 4.0, acidez: 0.5 g/l, azúcares: 150 g/l], 
producción: 1000 kg/ha, fermentación: [temperatura: 20°C, duración: 20 días, levadura: Saccharomyces cerevisiae], 
cultivo: [plantación: verano, riego: verano], resultados cata: [visual: rojo teja, olfativa: [frutal, madera], gustativa: [amargo]]
"""

# Extraer información relevante de los datos de texto
def extraer_informacion(linea):
    # Eliminar comillas y split por comas para obtener campos
    campos = linea.replace('"', '').split(',')
    diccionario = {}
    for campo in campos:
        key, value = campo.split(': ')
        diccionario[key] = value
    return diccionario

# Procesar cada línea del texto para construir el JSON
informacion_por_variedad = {}
lineas = datos_texto.split('\n')
for linea in lineas:
    if 'variedad uva:' in linea:
        # Extraer la variedad de uva
        variedad = linea.split('variedad uva: ')[1].strip()
        # Iniciar un nuevo diccionario para esta variedad
        if variedad not in informacion_por_variedad:
            informacion_por_variedad[variedad] = {}
    else:
        # Procesar los datos de cada categoría
        try:
            clave, valor = linea.split(': ')
            valor = valor.strip()
            if clave == 'ANALISIS MOSTO':
                # Convertir la lista de valores del análisis mosto a un diccionario
                valores_mosto = valor.replace('[', '').replace(']', '').split(',')
                diccionario_mosto = {v.split(': ')[0]: v.split(': ')[1].strip() for v in valores_mosto}
                informacion_por_variedad[variedad]['ANALISIS MOSTO'] = diccionario_mosto
            else:
                # Añadir el valor a la estructura de diccionario correspondiente
                informacion_por_variedad[variedad][clave] = valor
        except ValueError as e:
            # Manejo de errores en caso de formato inválido
            print(f"Error procesando línea: {linea} - {e}")

# Convertir la información estructurada a un diccionario JSON
json_final = json.dumps(informacion_por_variedad, indent=4, ensure_ascii=False)

# Imprimir o guardar el JSON final
print(json_final)