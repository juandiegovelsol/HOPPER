import random

# Verifica si un número es primo
def es_primo(n):
    if n <= 1:
        return False  # Los números menores o iguales a 1 no son primos
    if n <= 3:
        return True  # 2 y 3 son números primos
    if n % 2 == 0 or n % 3 == 0:
        return False  # Números divisibles por 2 o 3 no son primos
    i = 5 # Incia el bucle desde 5
    # Bucle para verificar divisibilidad de n por números >= 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True  # Si no fue divisible, es primo

# Genera un número primo de un número determinado de bits
def generar_primo(bits):
    # Genera un número primo de un tamaño específico en bits
    while True:
        num = random.getrandbits(bits)
        if es_primo(num):
            return num

# Calcula el máximo común divisor de dos números
def mcd(a, b):
    # Bucle para encontrar el máximo común divisor
    while b != 0:
        a, b = b, a % b
    return a # Retorna el MCD encontrado

# Calcula el inverso modular de e y phi
def inverso_modular(e, phi):
    # Implementación del algoritmo extendido de Euclides
    def extended_gcd(a, b):
        if b == 0:
            return (a, 1, 0)  # Caso base del algoritmo recursivo
        else:
            g, x, y = extended_gcd(b, a % b) # Llamada recursiva
            return (g, y, x - (a // b) * y) # Retorna el resultado del GCD extendido

    g, x, y = extended_gcd(e, phi) # Obtiene el GCD y coeficientes
    if g != 1:
        return None  # Si e y phi no son coprimos, no hay inverso
    else:
        return x % phi  # Retorna el inverso modular

# Genera las claves públicas y privadas RSA 
def generar_claves(bits):
    p = generar_primo(bits)  # Genera el primer primo p
    q = generar_primo(bits)  # Genera el segundo primo q

    # Asegura que p ≠ q
    while p == q:
        q = generar_primo(bits) 

    n = p * q  # Calcula n = p * q

    phi = (p - 1) * (q - 1)  # Calcula el totiente de n

    e = random.randint(2, phi - 1)  # Selecciona e desde 2 hasta phi-1
    # Bucle para encontrar un e coprimo con phi
    while mcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    d = inverso_modular(e, phi)  # Calcula el inverso modular de e

    return ((e, n), (d, n))  # Retorna las claves pública y privada

# Encripta un mensaje usando la clave pública
def encriptar(mensaje, clave_publica):
    e, n = clave_publica  # Paso 1 - Descomponer la clave pública
    mensaje_encriptado = [] # Paso 2 - Inicializar la lista del mensaje encriptado
    
    # Paso 3 - Iterar sobre cada carácter en el mensaje
    for caracter in mensaje:
        if caracter.isalpha(): 
            es_mayuscula = caracter.isupper() 
            valor = ord(caracter.upper()) 
            valor_encriptado = pow(valor, e, n)
            mensaje_encriptado.append((valor_encriptado, es_mayuscula)) 
    return mensaje_encriptado  # Paso 4 - Retornar el mensaje encriptado

# Desencripta un mensaje usando la clave privada
def desencriptar(mensaje_encriptado, clave_privada):
    d, n = clave_privada # Paso 1 - Descomponer la clave privada
    mensaje = '' # Paso 2 - Inicializar la cadena del mensaje desencriptado
    
    # Paso 3 - Iterar sobre cada par en el mensaje encriptado
    for valor_encriptado, es_mayuscula in mensaje_encriptado:
        valor = pow(valor_encriptado, d, n) 
        caracter = chr(valor)

        if not es_mayuscula:
            caracter = caracter.lower()
        mensaje += caracter
    return mensaje  # Paso 4 - Retornar el mensaje desencriptado

if __name__ == "__main__":
    bits = 8  # Número de bits para los números primos
    clave_publica, clave_privada = generar_claves(bits)  # Genera las claves
    print("Clave pública (e, n):", clave_publica)  # Muestra la clave pública
    print("Clave privada (d, n):", clave_privada)  # Muestra la clave privada

    mensaje = "HolaMundo"  # Mensaje original para encriptar
    print("Mensaje original:", mensaje)  # Muestra el mensaje original

    mensaje_encriptado = encriptar(mensaje, clave_publica)  # Encripta el mensaje
    print("Mensaje encriptado:", mensaje_encriptado)  # Muestra el mensaje encriptado

    mensaje_desencriptado = desencriptar(mensaje_encriptado, clave_privada)  # Desencripta el mensaje
    print("Mensaje desencriptado:", mensaje_desencriptado)  # Muestra el mensaje desencriptado