import random

datos_jugadores = {
    'LeBron James': {'promedio_puntos': 27},
    'Stephen Curry': {'promedio_puntos': 30},
    'Kevin Durant': {'promedio_puntos': 29},
    'Giannis Antetokounmpo': {'promedio_puntos': 28},
    'Luka Doncic': {'promedio_puntos': 31}
}

def calcular_probabilidades(puntos_propuestos, jugador):
    if jugador not in datos_jugadores:
        return "Jugador no encontrado"
    
    promedio_puntos = datos_jugadores[jugador]['promedio_puntos']
    probabilidad_superar = random.uniform(0.5, 1.0)
    probabilidad_no_alcanzar = 1 - probabilidad_superar

    if puntos_propuestos < promedio_puntos:
        mensaje = "Es más probable que {0} supere los {1} puntos".format(jugador, puntos_propuestos)
    elif puntos_propuestos > promedio_puntos:
        mensaje = "Es más probable que {0} no alcance los {1} puntos".format(jugador, puntos_propuestos)
    else:
        mensaje = "Las probabilidades están equilibradas para {0} con {1} puntos".format(jugador, puntos_propuestos)
    
    return mensaje

# Ejemplo de uso
print(calcular_probabilidades(26, 'LeBron James'))