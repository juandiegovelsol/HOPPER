def crear_cacheador(max_items=3):
    cache = {}
    
    def cacheador(funcion):
        def wrapper(*args):
            if args in cache:
                print(f"Caché: {args}")
                return cache[args]
            
            resultado = funcion(*args)
            
            if len(cache) >= max_items:
                cache.pop(next(iter(cache)))
                
            cache[args] = resultado
            print(f"Calculado: {args}")
            return resultado
        return wrapper
    return cacheador

@crear_cacheador()
def calcular_cuadrado(x):
    return x * x

@crear_cacheador()
def calcular_cubo(x):
    return x * x * x

# Test 1
print("Test 1:")
for i in range(5):
    print(f"Cuadrado({i}) = {calcular_cuadrado(i)}")

# Test 2
print("\nTest 2:")
for i in range(3):
    print(f"Cubo({i}) = {calcular_cubo(i)}")
    print(f"Cuadrado({i}) = {calcular_cuadrado(i)}")