import matplotlib.pyplot as plt

def dibujar_donut(tamano_exterior, tamano_interior, color_donut):
    """
    Dibuja una dona utilizando Matplotlib.
    
    Parámetros:
    - tamano_exterior: Radio del círculo exterior de la dona.
    - tamano_interior: Radio del círculo interior de la dona.
    - color_donut: Color de la dona.
    """
    # Círculo exterior de la dona
    circulo1 = plt.Circle((0, 0), tamano_exterior, color=color_donut)
    
    # Círculo interior de la dona (el hueco)
    circulo2 = plt.Circle((0, 0), tamano_interior, color='white')
    
    # Crear la figura y los ejes
    fig, ax = plt.subplots()
    
    # Añadir los círculos a la figura
    ax.add_patch(circulo1)
    ax.add_patch(circulo2)
    
    # Establecer los límites de los ejes para que la dona quede centrada
    ax.set_xlim(-tamano_exterior, tamano_exterior)
    ax.set_ylim(-tamano_exterior, tamano_exterior)
    
    # Establecer el aspecto de la figura para que los círculos sean proporcionales
    ax.set_aspect('equal', 'box')
    
    # Mostrar la figura
    plt.show()

# Ejemplo de uso de la función
dibujar_donut(1, 0.5, 'blue')