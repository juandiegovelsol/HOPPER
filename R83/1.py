def validar_codigo_postal(codigo_postal):
    # Eliminar espacios en blanco al inicio y al final de la cadena
    codigo_postal = codigo_postal.strip()
    
    # Verificar si el formato es XXXXX o XXXXX-XXXX
    if '-' in codigo_postal:
        partes = codigo_postal.split('-')
        if len(partes) != 2 or len(partes[0]) != 5 or len(partes[1]) != 4:
            return False
        primeros_digitos, segundos_digitos = partes
    else:
        primeros_digitos = codigo_postal
        segundos_digitos = ''

    # Verificar que los primeros 5 dígitos son numéricos
    if len(primeros_digitos) != 5 or not primeros_digitos.isdigit():
        return False
    
    # Si hay parte después del guion, verificar que son 4 dígitos numéricos
    if segundos_digitos and (len(segundos_digitos) != 4 or not segundos_digitos.isdigit()):
        return False

    return True

# Ejemplos de uso
print(validar_codigo_postal("90210"))            # True
print(validar_codigo_postal("10001-1234"))       # True
print(validar_codigo_postal("10001-123a"))       # False
print(validar_codigo_postal("1234"))             # False
print(validar_codigo_postal(" 90210 "))          # True
print(validar_codigo_postal("12345-12"))         # False