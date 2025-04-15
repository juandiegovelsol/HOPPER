import math

# Constantes globales
GRAVEDAD = 9.81  # Aceleración debida a la gravedad (m/s^2)
MASA = 0.5      # Masa del balón (kg)
RADIUS = 0.125  # Radio del balón (m)
COEF_ROZAMIENTO = 0.5  # Coeficiente de rozamiento
DENSIDAD_AIRE = 1.225  # Densidad del aire (kg/m^3)

def calcular_velocidad_ideal(fuerza):
    """Calcula la velocidad inicial ideal del balón sin considerar el rozamiento.

    Args:
        fuerza (float): Fuerza aplicada al balón en Newtons (N).

    Returns:
        float: Velocidad inicial del balón en m/s.
    """
    return fuerza / MASA

def calcular_distancia_ideal(velocidad):
    """Calcula la distancia de viaje ideal en un entorno sin rozamiento.

    Args:
        velocidad (float): Velocidad inicial del balón en m/s.

    Returns:
        float: Distancia ideal recorrida por el balón en metros.
    """
    angulo_radianes = math.radians(45)
    return (velocidad ** 2 * math.sin(2 * angulo_radianes)) / GRAVEDAD

def calcular_tiempo_ideal(velocidad):
    """Calcula el tiempo de vuelo ideal en un entorno sin rozamiento.

    Args:
        velocidad (float): Velocidad inicial del balón en m/s.

    Returns:
        float: Tiempo de vuelo del balón en segundos.
    """
    angulo_radianes = math.radians(45)
    return (2 * velocidad * math.sin(angulo_radianes)) / GRAVEDAD

def calcular_trayectoria_con_rozamiento(fuerza):
    """Calcula la trayectoria del balón considerando el rozamiento.

    Args:
        fuerza (float): Fuerza aplicada al balón en Newtons (N).

    Returns:
        tuple: Distancia recorrida y tiempo de vuelo con rozamiento.
    """
    angulo_radianes = math.radians(45)
    velocidad_inicial = fuerza / MASA
    vx = velocidad_inicial * math.cos(angulo_radianes)
    vy = velocidad_inicial * math.sin(angulo_radianes)
    x, y = 0, 0
    tiempo_total = 0
    dt = 0.01

    while y >= 0:
        velocidad_actual = math.sqrt(vx**2 + vy**2)
        fuerza_rozamiento = (0.5 * DENSIDAD_AIRE * math.pi * RADIUS**2 *
                             COEF_ROZAMIENTO * velocidad_actual**2)
        ax = -(fuerza_rozamiento / MASA) * (vx / velocidad_actual)
        ay = -GRAVEDAD - (fuerza_rozamiento / MASA) * (vy / velocidad_actual)
        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt
        tiempo_total += dt

    return x, tiempo_total

def main():
    """Función principal que ejecuta el programa y gestiona la entrada de datos y errores."""
    try:
        fuerza = float(input("Ingrese la fuerza del golpe (N): "))
        if not (1 <= fuerza <= 2000):
            raise ValueError("Error: La fuerza debe estar entre 1 y 2000 N.")
    except ValueError as e:
        print(e)
        return

    # Calcula las trayectorias ideal y con rozamiento
    distancia_ideal = calcular_distancia_ideal(calcular_velocidad_ideal(fuerza))
    distancia_roz, tiempo_roz = calcular_trayectoria_con_rozamiento(fuerza)

    # Calcula el tiempo ideal
    tiempo_ideal = calcular_tiempo_ideal(calcular_velocidad_ideal(fuerza))

    # Imprime los resultados
    print("\nResultados:")
    print(f"Distancia ideal: {distancia_ideal:.2f} m")
    print(f"Distancia con rozamiento: {distancia_roz:.2f} m")
    print(f"Tiempo ideal: {tiempo_ideal:.2f} s")
    print(f"Tiempo con rozamiento: {tiempo_roz:.2f} s")

if __name__ == "__main__":
    main()