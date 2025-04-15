import matplotlib.pyplot as plt

def dibujar_donut_doja(radio_externo, radio_interno, color_externo='r', color_interno='white'):
    """
    Dibuja una dónut doja utilizando matplotlib.

    Parámetros:
    - radio_externo (float): El radio exterior del dónut.
    - radio_interno (float): El radio interior del dónut (hueco).
    - color_externo (str): El color del dónut.
    - color_interno (str): El color del hueco.
    """
    # Crea un círculo grande que representará el dónut
    circulo1 = plt.Circle((0, 0), radio_externo, color=color_externo)
    
    # Crea un círculo pequeño que representará el hueco del dónut
    circulo2 = plt.Circle((0, 0), radio_interno, color=color_interno)

    # Crea la figura y el eje para colocar los círculos
    fig, ax = plt.subplots()
    
    # Agrega los círculos como capas en el gráfico
    ax.add_patch(circulo1)
    ax.add_patch(circulo2)
    
    # Establece los límites del eje x y y para que sean iguales, creando una proporción 1:1
    ax.set_xlim(-radio_externo * 1.2, radio_externo * 1.2)
    ax.set_ylim(-radio_externo * 1.2, radio_externo * 1.2)
    
    # Establece el aspecto de la figura para que sea igual en ambas direcciones ('equal', 'box')
    ax.set_aspect('equal', 'box')
    
    # Muestra la figura en pantalla
    plt.show()

# Ejemplo de uso de la función con parámetros específicos
dibujar_donut_doja(1, 0.2, 'purple', 'pink')