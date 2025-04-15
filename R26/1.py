import math

# Constantes globales para parámetros físicos
MASA = 0.5  # kg
COEF_ROZAMIENTO = 0.5
GRAVEDAD = 9.81  # m/s^2
ANGULO = 45  # grados
DENSIDAD_AIRE = 1.225  # kg/m^3
RADIO_PELOTA = 0.25 / 2  # m

def calcular_entorno_ideal(fuerza):
    """
    Calcula la distancia y el tiempo de vuelo en un entorno ideal sin rozamiento.

    Args:
        fuerza (float): Fuerza del golpe en Newtons.

    Returns:
        tuple: Distancia y tiempo de vuelo en el entorno ideal (distancia, tiempo).
    """
    velocidad_ideal = fuerza / MASA
    angulo_rad = math.radians(ANGULO)
    tiempo_ideal = (2 * velocidad_ideal * math.sin(angulo_rad)) / GRAVEDAD
    distancia_ideal = (velocidad_ideal ** 2 * math.sin(2 * angulo_rad)) / GRAVEDAD
    return distancia_ideal, tiempo_ideal

def calcular_entorno_rozamiento(fuerza):
    """
    Calcula la distancia y el tiempo de vuelo en un entorno con rozamiento.

    Args:
        fuerza (float): Fuerza del golpe en Newtons.

    Returns:
        tuple: Distancia y tiempo de vuelo en el entorno con rozamiento (distancia, tiempo).
    """
    velocidad_roz = fuerza / MASA
    angulo_rad = math.radians(ANGULO)
    vx = velocidad_roz * math.cos(angulo_rad)
    vy = velocidad_roz * math.sin(angulo_rad)
    tiempo_roz, x, y = 0, 0, 0
    dt = 0.01

    # Simulación de la trayectoria de la pelota considerando el rozamiento
    while y >= 0:
        velocidad_actual = math.sqrt(vx**2 + vy**2)
        fuerza_roz = 0.5 * DENSIDAD_AIRE * math.pi * RADIO_PELOTA**2 * COEF_ROZAMIENTO * velocidad_actual**2
        ax = -(fuerza_roz / MASA) * (vx / velocidad_actual)
        ay = -GRAVEDAD - (fuerza_roz / MASA) * (vy / velocidad_actual)
        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt
        tiempo_roz += dt

    return x, tiempo_roz

def obtener_fuerza_usuario():
    """
    Solicita y valida la fuerza ingresada por el usuario.

    Returns:
        float: Fuerza del golpe en Newtons.
    """
    while True:
        try:
            fuerza = float(input("Ingrese la fuerza del golpe (N): "))
            if 1 <= fuerza <= 2000:
                return fuerza
            else:
                print("Error: La fuerza debe ser un número entre 1 y 2000.")
        except ValueError:
            print("Error: Por favor, ingrese un valor numérico.")

def main():
    """
    Función principal que coordina el cálculo de la trayectoria de la pelota
    en entornos ideal y con rozamiento.
    """
    fuerza = obtener_fuerza_usuario()
    
    distancia_ideal, tiempo_ideal = calcular_entorno_ideal(fuerza)
    distancia_roz, tiempo_roz = calcular_entorno_rozamiento(fuerza)

    print("\nResultados:")
    print(f"Distancia ideal: {distancia_ideal:.2f} m")
    print(f"Distancia con rozamiento: {distancia_roz:.2f} m")
    print(f"Tiempo ideal: {tiempo_ideal:.2f} s")
    print(f"Tiempo con rozamiento: {tiempo_roz:.2f} s")

if __name__ == "__main__":
    main()