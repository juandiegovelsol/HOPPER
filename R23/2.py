import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

def dibujar_arcoiris(numero_colores, ancho_banda):
    """
    Dibuja un arcoíris con la cantidad de colores y el ancho de banda especificado.

    Parameters:
    numero_colores (int): Número de colores que tendrá el arcoíris (máximo 7).
    ancho_banda (int): Ancho de cada banda de color.

    Nota: Si se especifica más de 7 colores, se utilizarán solo los primeros 7.
    """

    # Se define el tamaño del gráfico y se ajusta la relación de aspecto para mantener los círculos proporcionales
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    # Se establecen los límites del gráfico para mostrar el arcoíris completo
    ax.set_xlim([-90, 90])
    ax.set_ylim([0, 100])

    # Centro del arcoíris
    centro = (0, 0)

    # Ángulos del arcoíris (un semicírculo)
    angulo1, angulo2 = 0, 180

    # Lista de colores basada en un arcoíris
    colores = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

    # Asegurarse de no exceder el número máximo de colores
    numero_colores = min(numero_colores, len(colores))

    # Calcular el radio del arco más grande
    radio_exterior = ancho_banda * (numero_colores + 1)

    # Dibuja cada banda de color, comenzando con el radio más externo
    for color in reversed(colores[:numero_colores]):
        wedge = Wedge(centro, radio_exterior, angulo1, angulo2, facecolor=color, edgecolor='none')
        ax.add_patch(wedge)

        # Reduce el radio para la siguiente banda de color
        radio_exterior -= ancho_banda

    # Dibujar el centro blanco del arcoíris
    wedge = Wedge(centro, 10, angulo1, angulo2, facecolor="white", edgecolor='none')
    ax.add_patch(wedge)

    # Mostrar el gráfico con el arcoíris
    plt.show()

# Ejemplo de uso de la función:
dibujar_arcoiris(8, 10)