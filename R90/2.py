import numpy as np

def remuestrear_imagen(imagen, factor_f, factor_c, *, threeD=False):
    # Validación de la imagen
    if not isinstance(imagen, np.ndarray):
        raise ValueError("La imagen debe ser un arreglo de NumPy.")
    
    # Validación de dimensiones
    if imagen.ndim not in (2, 3):
        raise ValueError("La imagen solo puede ser de 2 o 3 dimensiones.")
    
    # Validación de los factores de remuestreo
    if not isinstance(factor_f, int) or not isinstance(factor_c, int):
        raise ValueError("Los factores de remuestreo deben ser enteros.")
    if factor_f <= 0 or factor_c <= 0:
        raise ValueError("Los factores de remuestreo deben ser positivos.")
    if factor_f > imagen.shape[0] or factor_c > imagen.shape[1]:
        raise ValueError("Los factores de remuestreo no deben ser mayores que las dimensiones de la imagen.")
    
    # Caso 3D con recursividad
    if threeD and imagen.ndim == 3:
        return np.array([remuestrear_imagen(imagen[i, :, :], factor_f, factor_c, threeD=False) for i in range(imagen.shape[0])])
    
    # Remuestreo para 2D
    nuevas_filas = imagen.shape[0] // factor_f
    nuevas_columnas = imagen.shape[1] // factor_c
    
    nueva_imagen = np.zeros((nuevas_filas, nuevas_columnas))
    
    for i in range(nuevas_filas):
        for j in range(nuevas_columnas):
            nueva_imagen[i, j] = np.mean(imagen[i * factor_f:(i + 1) * factor_f, j * factor_c:(j + 1) * factor_c])
    
    return nueva_imagen

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una imagen de prueba en 2D
    imagen_2d = np.arange(32 * 32).reshape(32, 32)
    factor_f = 4
    factor_c = 4
    resultado_2d = remuestrear_imagen(imagen_2d, factor_f, factor_c)
    print("Imagen remuestreada 2D:", resultado_2d)

    # Crear una imagen de prueba en 3D
    imagen_3d = np.array([imagen_2d, imagen_2d * 2, imagen_2d * 3])
    resultado_3d = remuestrear_imagen(imagen_3d, factor_f, factor_c, threeD=True)
    print("Imagen remuestreada 3D:", resultado_3d)