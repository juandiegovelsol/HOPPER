import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

def dibujar_arcoiris(tamaño_base=10, cantidad_colores=7, colores=None):
    """
    Dibuja un arcoíris utilizando segmentos de arcos (cuñas) con distintos colores.
    
    Parámetros:
    - tamaño_base (int): El ancho de cada banda de color en el arcoíris.
    - cantidad_colores (int): La cantidad de colores a mostrar en el arcoíris.
    - colores (list): Lista de colores en formato de cadena reconocidos por Matplotlib.
                      Si no se especifica, se usará la lista predeterminada de 7 colores.
                      
    Notas:
    - La cantidad de colores se ajustará automáticamente para no exceder los 7 colores disponibles.
    - Si se especifica una cantidad de colores mayor a 7, se utilizarán solo los primeros 7 colores
      de la lista predeterminada.
    """
    
    if colores is None:
        colores = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    
    # Limita la cantidad de colores a un máximo de 7
    cantidad_colores = min(cantidad_colores, len(colores))
    
    # Configura el entorno de dibujo
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlim([-90, 90])
    ax.set_ylim([0, tamaño_base * (cantidad_colores + 1)])
    centro = (0, 0)
    angulo1, angulo2 = 0, 180

    # Calcula el radio exterior basado en el tamaño base y la cantidad de colores
    radio_exterior = tamaño_base * (cantidad_colores + 1)

    # Dibuja cada banda de color del arcoíris
    for i in range(cantidad_colores):
        color = colores[i]
        wedge = Wedge(centro, radio_exterior, angulo1, angulo2, facecolor=color, edgecolor='none')
        ax.add_patch(wedge)
        radio_exterior -= tamaño_base

    # Dibuja la nube (cuña blanca) al final del arcoíris
    wedge = Wedge(centro, tamaño_base, angulo1, angulo2, facecolor="white", edgecolor='none')
    ax.add_patch(wedge)
    
    # Muestra el gráfico
    plt.show()

# Ejemplo de uso:
dibujar_arcoiris(20, 2)