import math  

def main():  
    fuerza = float(input("Ingrese la fuerza del golpe (N): "))  
    if fuerza <= 0:  
        print("Error: La fuerza debe ser un número positivo.")  
        return  

    angulo = 45  
    gravedad = 9.81  
    coef_rozamiento = 0.5  
    masa = 0.5  

    # Cálculos para entorno ideal  
    velocidad_ideal = fuerza / 0.5  
    angulo_rad = math.radians(angulo)  
    tiempo_ideal = (2 * velocidad_ideal * math.sin(angulo_rad)) / gravedad  
    distancia_ideal = (velocidad_ideal ** 2 * math.sin(2 * angulo_rad)) / gravedad  

    # Cálculos para entorno con rozamiento  
    velocidad_roz = fuerza / masa  
    vx = velocidad_roz * math.cos(angulo_rad)  
    vy = velocidad_roz * math.sin(angulo_rad)  
    tiempo_roz, x, y = 0, 0, 0  
    dt = 0.01  

    while y >= 0:  
        velocidad_actual = math.sqrt(vx**2 + vy**2)  
        fuerza_roz = 0.5 * 1.225 * math.pi * (0.25/2)**2 * coef_rozamiento * velocidad_actual**2  
        ax = -(fuerza_roz / masa) * (vx / velocidad_actual)  
        ay = -gravedad - (fuerza_roz / masa) * (vy / velocidad_actual)  
        vx += ax * dt  
        vy += ay * dt  
        x += vx * dt  
        y += vy * dt  
        tiempo_roz += dt  

    print("\nResultados:")  
    print(f"Distancia ideal: {distancia_ideal:.2f} m")  
    print(f"Distancia con rozamiento: {x:.2f} m")  
    print(f"Tiempo ideal: {tiempo_ideal:.2f} s")  
    print(f"Tiempo con rozamiento: {tiempo_roz:.2f} s")  

if __name__ == "__main__":  
    main()  