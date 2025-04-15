import numpy as np

def nequalize(arreglo, p=5, valor_no_valido=-1):
    """
    Normaliza o escala arreglos, típicamente representando imágenes, 
    para los casos 2D y 3D, manejando valores no válidos.

    Argumentos:
        arreglo (np.ndarray): El arreglo de entrada que será normalizado.
        p (float): Valor percentil para la escala, entre 0 y 100.
        valor_no_valido: Valor que se considera no válido en el arreglo.

    Retorna:
        np.ndarray: El arreglo normalizado.
    
    Excepciones:
        ValueError: Si el valor del percentil (p) no está entre 0 y 50.
    """
    if not 0 <= p <= 50:
        raise ValueError("El valor del percentil (p) debe estar entre 0 y 50.")

    if len(arreglo.shape) == 2:
        # Excluir valores no válidos del cálculo percentil
        valores_validos = arreglo[arreglo != valor_no_valido]
        vmin = np.percentile(valores_validos, p)
        vmax = np.percentile(valores_validos, 100 - p)

        # Manejar casos donde vmin == vmax
        if vmin == vmax:
            arreglo_norm = np.where(arreglo != valor_no_valido, 0.5, np.nan)
        else:
            arreglo_norm = (arreglo - vmin) / (vmax - vmin)
            arreglo_norm = np.clip(arreglo_norm, 0, 1)  # Asegurarse que no haya valores fuera del rango [0, 1]
            arreglo_norm[arreglo == valor_no_valido] = np.nan 
    
    elif len(arreglo.shape) == 3:
        arreglo_norm = arreglo.copy()
        for i in range(arreglo.shape[0]):
            arreglo_norm[i] = nequalize(arreglo_norm[i], p=p, valor_no_valido=valor_no_valido)
    
    else:
        raise ValueError("El arreglo de entrada debe ser 2D o 3D.")

    return arreglo_norm

# Prueba de funcionamiento correcto
# Crear un arreglo de ejemplo:
np.random.seed(42)
a = np.random.randint(0, 10, size=(3, 3, 3))

# Asignar -1 a uno de los valores del arreglo:
a[:, 2, 2] = -1

# Probar la función con un arreglo 2D
b = a[0]
b_escalado = nequalize(b, p=2)
print(b_escalado[1,1])  # Imprime el valor normalizado en la posición [1, 1]

# Probar la función con el caso 3D:
a_escalado = nequalize(a, p=2) 
print(a_escalado[0, 1, 1])  # Imprime el valor normalizado en la posición [0, 1, 1]

# Prueba con p > 50, debería lanzar una excepción
try:
    a_escalado2 = nequalize(a, p=70) 
except ValueError as e:
    print(f"Error: {e}")