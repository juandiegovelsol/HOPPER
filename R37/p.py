def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filtrar_primos(lista):
    return [x for x in lista if es_primo(x)]

print(filtrar_primos([2, 3, 4, 5, 6, 7, 8, 9]))
print(filtrar_primos([0, 1, -3, 11, 13, 15]))
print(filtrar_primos([17, 19, 20, 21, 22, 23, 24]))