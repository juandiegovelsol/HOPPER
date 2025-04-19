import numpy as np

def remuestrear_imagen(imagen, factor_f, factor_c, *, recursive=False):
    # Validaciones de la imagen
    if not isinstance(imagen, np.ndarray):
        raise TypeError("La imagen debe ser un arreglo de NumPy.")
    
    # Validaciones de dimensión de la imagen
    if imagen.ndim not in [2, 3]:
        raise ValueError("La imagen solo puede ser de 2 o 3 dimensiones.")
    
    # Validaciones de los factores de remuestreo
    if not isinstance(factor_f, int) or not isinstance(factor_c, int):
        raise TypeError("Los factores de remuestreo deben ser enteros.")
    if factor_f <= 0 or factor_c <= 0:
        raise ValueError("Los factores de remuestreo deben ser positivos.")
    if factor_f > imagen.shape[0] or factor_c > imagen.shape[1]:
        raise ValueError("Los factores de remuestreo no deben ser mayores que las dimensiones de la imagen.")

    # Validación del parámetro recursive
    print(recursive, imagen.ndim != 3)
    if recursive and imagen.ndim != 3:
        raise ValueError("El parámetro '3d' solo puede ser True si la imagen es 3D.")
    if not recursive and imagen.ndim == 3:
        raise ValueError("El parámetro '3d' debe ser True si la imagen es 3D.")

    # Remuestreo 2D
    if imagen.ndim == 2:
        nuevas_filas = imagen.shape[0] // factor_f
        nuevas_columnas = imagen.shape[1] // factor_c
        return imagen[::factor_f, ::factor_c].reshape(nuevas_filas, nuevas_columnas)
    
    # Remuestreo 3D
    if recursive:
        p = imagen.ndim
        return np.array([remuestrear_imagen(imagen[i, :, :], factor_f, factor_c, recursive=True) for i in range(p)])

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una imagen 2D de ejemplo de 32x32
    imagen_2d = np.random.rand(32, 32)
    factor_f = 4
    factor_c = 4

    # Remuestrear la imagen 2D
    imagen_remuestreada_2d = remuestrear_imagen(imagen_2d, factor_f, factor_c)
    print("Imagen 2D remuestreada:")
    print(imagen_remuestreada_2d)

    # Crear una imagen 3D de ejemplo de 10x32x32
    imagen_3d = np.random.rand(10, 32, 32)
    print(imagen_3d.ndim)

    # Remuestrear la imagen 3D recursivamente
    imagen_remuestreada_3d = remuestrear_imagen(imagen_3d, factor_f, factor_c, recursive=True)
    print("Imagen 3D remuestreada:")
    print(imagen_remuestreada_3d)