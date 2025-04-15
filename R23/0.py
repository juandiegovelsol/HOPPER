import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim([-90, 90])
ax.set_ylim([0, 100])
centro = (0, 0)
angulo1, angulo2 = 0, 180
ancho_banda = 10
colores = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
radio_exterior = ancho_banda * (len(colores)+1)
for color in reversed(colores):
    wedge = Wedge(centro, radio_exterior, angulo1, angulo2, facecolor=color, edgecolor='none')
    ax.add_patch(wedge)

    radio_exterior -= ancho_banda
wedge = Wedge(centro, 10, angulo1, angulo2, facecolor="white", edgecolor='none')
ax.add_patch(wedge)
plt.show()