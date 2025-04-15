import random
import math

def es_primo(n):
    # Verifica si un número es primo
    if n <= 1:
        return False  # Los números menores o iguales a 1 no son primos
    if n <= 3:
        return True  # 2 y 3 son primos
    if n % 2 == 0 or n % 3 == 0:
        return False  # Descarta los múltiplos de 2 y 3
    i = 5
    while i * i <= n:  # Verifica divisibilidad sólo hasta la raíz cuadrada de n
        if n % i == 0 or n % (i + 2) == 0:
            return False  # Si es divisible, no es primo
        i += 6  # Aumenta i para verificar los siguientes candidatos
    return True  # Si no fue divisible, es primo

def generar_primo(bits):
    # Genera un número primo de un tamaño específico en bits
    while True:
        num = random.getrandbits(bits)  # Genera un número aleatorio de bits
        if es_primo(num):  # Verifica si el número es primo
            return num  # Retorna el número primo encontrado

def mcd(a, b):
    # Calcula el máximo común divisor (MCD) usando el algoritmo de Euclides
    while b != 0:  # Mientras b no sea cero
        a, b = b, a % b  # Aplica el algoritmo de Euclides
    return a  # Retorna el MCD encontrado

def inverso_modular(e, phi):
    # Calcula el inverso modular usando el algoritmo extendido de Euclides
    def extended_gcd(a, b):
        if b == 0:
            return (a, 1, 0)  # Caso base del algoritmo
        else:
            g, x, y = extended_gcd(b, a % b)  # Llamada recursiva
            return (g, y, x - (a // b) * y)  # Retorna el resultado del GCD extendido

    g, x, y = extended_gcd(e, phi)  # Obtiene el GCD y coeficientes
    if g != 1:
        return None  # Si no es coprimo, no hay inverso
    else:
        return x % phi  # Retorna el inverso modular

def generar_claves(bits):
    # Genera un par de claves (pública y privada)
    p = generar_primo(bits)  # Genera el primer número primo
    q = generar_primo(bits)  # Genera el segundo número primo
    while p == q:  # Asegura que p y q sean diferentes
        q = generar_primo(bits)  # Regenera q si es igual a p

    n = p * q  # Calcula n como el producto de p y q
    phi = (p - 1) * (q - 1)  # Calcula phi para el sistema RSA

    e = random.randint(2, phi - 1)  # Selecciona e aleatoriamente
    while mcd(e, phi) != 1:  # Asegura que e y phi sean coprimos
        e = random.randint(2, phi - 1)  # Regenera e si no son coprimos

    d = inverso_modular(e, phi)  # Calcula el inverso modular de e

    return ((e, n), (d, n))  # Retorna las claves públicas y privadas

def encriptar(mensaje, clave_publica):
    # Encripta un mensaje usando la clave pública
    e, n = clave_publica  # Descompone la clave pública
    mensaje_encriptado = []  # Inicializa la lista del mensaje encriptado
    for caracter in mensaje:  # Itera sobre cada carácter del mensaje
        if caracter.isalpha():  # Comprueba que el carácter sea una letra
            es_mayuscula = caracter.isupper()  # Verifica si es mayúscula
            valor = ord(caracter.upper())  # Obtiene el valor ASCII del carácter
            valor_encriptado = pow(valor, e, n)  # Aplica la encriptación
            mensaje_encriptado.append((valor_encriptado, es_mayuscula))  # Añade el resultado a la lista
    return mensaje_encriptado  # Retorna el mensaje encriptado

def desencriptar(mensaje_encriptado, clave_privada):
    # Desencripta un mensaje usando la clave privada
    d, n = clave_privada  # Descompone la clave privada
    mensaje = ''  # Inicializa la cadena del mensaje desencriptado
    for valor_encriptado, es_mayuscula in mensaje_encriptado:  # Itera sobre cada valor encriptado
        valor = pow(valor_encriptado, d, n)  # Aplica la desencriptación
        caracter = chr(valor)  # Convierte el valor de vuelta al carácter

        if not es_mayuscula:  # Si no es mayúscula, lo convierte a minúscula
            caracter = caracter.lower()
        mensaje += caracter  # Añade el carácter al mensaje desencriptado
    return mensaje  # Retorna el mensaje desencriptado


if __name__ == "__main__":
    bits = 8  # Define el tamaño de las claves en bits
    clave_publica, clave_privada = generar_claves(bits)  # Genera las claves
    print("Clave pública (e, n):", clave_publica)  # Muestra la clave pública
    print("Clave privada (d, n):", clave_privada)  # Muestra la clave privada

    mensaje = "HolaMundo"  # Mensaje a encriptar
    print("Mensaje original:", mensaje)  # Muestra el mensaje original

    mensaje_encriptado = encriptar(mensaje, clave_publica)  # Encripta el mensaje
    print("Mensaje encriptado:", mensaje_encriptado)  # Muestra el mensaje encriptado

    mensaje_desencriptado = desencriptar(mensaje_encriptado, clave_privada)  # Desencripta el mensaje
    print("Mensaje desencriptado:", mensaje_desencriptado)  # Muestra el mensaje desencriptado