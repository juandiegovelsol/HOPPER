import numpy as np

def nequalize(arreglo, p=5, valor_no_valido=-1):
    """
    Normaliza o escala arreglos, típicamente representando imágenes, para los casos 2D y 3D.

    Argumentos:
        arreglo (np.ndarray): El arreglo de entrada que será normalizado.
        p (float): Valor percentil para la escala, entre 0 y 50.
        valor_no_valido: Valor que se considera no válido en el arreglo.

    Retorna:
        np.ndarray: El arreglo normalizado.
    
    Excepciones:
        ValueError: Si el valor del percentil (p) no está entre 0 y 50,
                    o si el arreglo de entrada no es 2D o 3D.
    """
    if not 0 <= p <= 50:
        raise ValueError("El valor del percentil (p) debe estar entre 0 y 50.")

    arreglo_norm = np.array(arreglo, copy=True)  # Crea una copia para evitar modificar el arreglo original
    if len(arreglo_norm.shape) == 2:
        valores_validos = arreglo_norm[arreglo_norm != valor_no_valido]
        vmin = np.percentile(valores_validos, p)
        vmax = np.percentile(valores_validos, 100 - p)

        if vmin == vmax:
            arreglo_norm = np.where(arreglo_norm != valor_no_valido, 0.5, np.nan)
        else:
            arreglo_norm = (arreglo_norm - vmin) / (vmax - vmin)
            arreglo_norm = np.clip(arreglo_norm, 0, 1)  # Asegurarse que no se salga del rango [0, 1]
            arreglo_norm[arreglo_norm == valor_no_valido] = np.nan

    elif len(arreglo_norm.shape) == 3:
        for i in range(arreglo_norm.shape[0]):
            arreglo_norm[i] = nequalize(arreglo_norm[i], p, valor_no_valido)
    else:
        raise ValueError("El arreglo de entrada debe ser 2D o 3D.")

    return arreglo_norm

# Pruebas con arreglos 2D y 3D
np.random.seed(42)
a = np.random.randint(0, 10, size=(3, 3, 3))
a[:, 2, 2] = -1  # -1 será considerado un valor no válido
valor_no_valido = -1

# Prueba con un arreglo 2D
b = a[0]
b_escalado = nequalize(b, p=2)
print(b_escalado[1, 1])

# Prueba con un arreglo 3D
a_escalado = nequalize(a, p=2)
print(a_escalado[0, 1, 1])

# Prueba con p > 50 para lanzar una excepción
try:
    a_escalado2 = nequalize(a, p=70)
except ValueError as e:
    print(f"Error: {e}")