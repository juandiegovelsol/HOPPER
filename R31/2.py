import random

class Jugador:
    def __init__(self, nombre, promedio_puntos):
        self.nombre = nombre
        self.promedio_puntos = promedio_puntos

jugadores_nba = [
    Jugador("LeBron James", 25.0),
    Jugador("Kevin Durant", 27.0),
    Jugador("Giannis Antetokounmpo", 28.0),
    Jugador("Stephen Curry", 26.0),
    Jugador("Luka Doncic", 29.0)
]

def calcular_probabilidades(puntos, jugador):
    for j in jugadores_nba:
        if j.nombre == jugador:
            probabilidad_superar = random.uniform(0.4, 0.6) if puntos > j.promedio_puntos else random.uniform(0.6, 0.8)
            probabilidad_no_alcanzar = 1 - probabilidad_superar
            resultado = "superar" if probabilidad_superar > probabilidad_no_alcanzar else "no alcanzar"
            return resultado
    return "Jugador no encontrado"

# Ejemplo de uso
print(calcular_probabilidades(24, 'LeBron James'))