import random

# Constantes del juego
NUM_CASILLAS = 63
FACES_DADO = 6
CASILLAS_OCA = [5, 9, 14, 18, 23, 27, 32, 36, 41, 45, 50, 54, 58] # Casillas de Oca
# Casillas especiales y sus reglas (Puente, Dados, Posada, Pozo, Laberinto, Muerte)
CASILLAS_ESPECIALES = {
    6: "Puente",    # De puente a puente y tiro porque me lleva la corriente (va a la 12 y tira)
    12: "Dados",    # De dado a dado y tiro porque me ha tocado (avanza lo mismo y tira)
    19: "Posada",   # Pierde 1 turno
    25: "Pozo",     # Pierde 2 turnos
    31: "Laberinto",# Retrocede a la casilla 30
    42: "Muerte"    # Vuelve a la casilla 1
}
POSICION_INICIAL = 1

def lanzar_dado():
    """Simula el lanzamiento de un dado de seis caras."""
    return random.randint(1, FACES_DADO)

def mover_ficha(posicion_actual, tirada_dado, jugador_num):
    """
    Mueve la ficha según el resultado del dado y aplica las reglas del juego.
    Devuelve: (posición_final, turnos_a_perder, conceder_turno_extra)
    """
    print(f"Jugador {jugador_num}: Estaba en {posicion_actual}, sacó un {tirada_dado}.")
    posicion_intermedia = posicion_actual + tirada_dado
    
    # Mensaje de avance inicial
    if posicion_intermedia == posicion_actual: # Caso de tirada 0 si se implementara
        print(f"Jugador {jugador_num}: Se queda en la casilla {posicion_actual}.")
    elif posicion_intermedia < posicion_actual: # Caso de retroceso por alguna regla futura
         print(f"Jugador {jugador_num}: Retrocede de {posicion_actual} a {posicion_intermedia}.")
    else:
        print(f"Jugador {jugador_num}: Avanza de {posicion_actual} a {posicion_intermedia}.")

    # Rebote si se pasa de la casilla final
    if posicion_intermedia > NUM_CASILLAS:
        rebote = posicion_intermedia - NUM_CASILLAS
        posicion_intermedia = NUM_CASILLAS - rebote
        print(f"Jugador {jugador_num}: ¡Se pasó! Rebota y va a la casilla {posicion_intermedia}.")
    
    if posicion_intermedia == NUM_CASILLAS:
        print(f"Jugador {jugador_num}: ¡Ha llegado justo a la meta en la casilla {NUM_CASILLAS}!")
        return NUM_CASILLAS, 0, False # Ganador

    posicion_efecto = posicion_intermedia
    turnos_a_perder = 0
    conceder_turno_extra = False

    # Bucle para manejar efectos en cascada (Oca -> Oca, Puente -> Dados, etc.)
    while True:
        efecto_aplicado_en_iteracion = False # Para saber si hubo un cambio que requiera re-evaluar

        # 1. Regla de la Oca
        if posicion_efecto in CASILLAS_OCA:
            print(f"Jugador {jugador_num}: ¡Oca en la casilla {posicion_efecto}! De oca a oca y tiro porque me toca.")
            conceder_turno_extra = True
            efecto_aplicado_en_iteracion = True
            try:
                indice_oca_actual = CASILLAS_OCA.index(posicion_efecto)
                if indice_oca_actual + 1 < len(CASILLAS_OCA):
                    siguiente_oca = CASILLAS_OCA[indice_oca_actual + 1]
                    print(f"Jugador {jugador_num}: Avanza a la siguiente oca en {siguiente_oca}.")
                    posicion_efecto = siguiente_oca
                else:
                    print(f"Jugador {jugador_num}: ¡Es la última oca! Se queda en {posicion_efecto} y tira de nuevo.")
                    # No hay más ocas a donde saltar, pero el turno extra se mantiene.
                    # Se sale del bucle de cascada porque no hay más movimiento automático por Oca.
                    break 
            except ValueError: # No debería ocurrir si está en CASILLAS_OCA
                break

        # 2. Reglas de Casillas Especiales
        elif posicion_efecto in CASILLAS_ESPECIALES:
            regla = CASILLAS_ESPECIALES[posicion_efecto]
            print(f"Jugador {jugador_num}: ¡Casilla especial en {posicion_efecto}! Es '{regla}'.")
            efecto_aplicado_en_iteracion = True

            if regla == "Puente": # Casilla 6
                print(f"Jugador {jugador_num}: De puente (6) a puente (12) y tiro porque me lleva la corriente.")
                posicion_efecto = 12 # Va a la casilla 12 (Dados)
                conceder_turno_extra = True
                # Continúa el bucle para aplicar la regla de Dados en la casilla 12
            
            elif regla == "Dados": # Casilla 12
                print(f"Jugador {jugador_num}: De dado a dado y tiro porque me ha tocado.")
                print(f"Jugador {jugador_num}: Avanza {tirada_dado} casillas más (lo que sacó en el dado).")
                posicion_efecto += tirada_dado
                conceder_turno_extra = True
                # Comprobar rebote de nuevo por este movimiento adicional
                if posicion_efecto > NUM_CASILLAS:
                    rebote = posicion_efecto - NUM_CASILLAS
                    posicion_efecto = NUM_CASILLAS - rebote
                    print(f"Jugador {jugador_num}: ¡Se pasó por el efecto Dados! Rebota a {posicion_efecto}.")
                if posicion_efecto == NUM_CASILLAS:
                    print(f"Jugador {jugador_num}: ¡Ha llegado justo a la meta en la casilla {NUM_CASILLAS} por efecto Dados!")
                    # Sale del bucle de cascada, el turno extra se mantiene si no gana
                    break
                # Continúa el bucle para ver si la nueva casilla es especial

            elif regla == "Posada": # Casilla 19
                print(f"Jugador {jugador_num}: Pierde 1 turno en la Posada.")
                turnos_a_perder = 1
                break # La Posada detiene el movimiento y los efectos en cascada.
            
            elif regla == "Pozo": # Casilla 25
                print(f"Jugador {jugador_num}: ¡Cayó en el Pozo! Pierde 2 turnos.")
                turnos_a_perder = 2
                break # El Pozo detiene el movimiento y los efectos en cascada.
            
            elif regla == "Laberinto": # Casilla 31
                print(f"Jugador {jugador_num}: ¡En el Laberinto! Retrocede a la casilla 30.")
                posicion_efecto = 30
                # Continúa el bucle para ver si la casilla 30 es especial
            
            elif regla == "Muerte": # Casilla 42
                print(f"Jugador {jugador_num}: ¡Casilla de la Muerte! Vuelve al inicio (casilla {POSICION_INICIAL}).")
                posicion_efecto = POSICION_INICIAL
                # Continúa el bucle para ver si la casilla 1 es especial (Oca, etc.)
        
        # Si no se aplicó ningún efecto que cambie la posición o conceda turno, salir del bucle
        if not efecto_aplicado_en_iteracion:
            break
        
        # Si se aplicó un efecto y la nueva posición es la meta
        if posicion_efecto == NUM_CASILLAS:
             print(f"Jugador {jugador_num}: ¡Ha llegado justo a la meta en la casilla {NUM_CASILLAS} tras un efecto!")
             break


    return posicion_efecto, turnos_a_perder, conceder_turno_extra

def jugar():
    """Función principal que gestiona el juego completo."""
    posiciones = [POSICION_INICIAL, POSICION_INICIAL]  # Posiciones iniciales de los dos jugadores
    turnos_perdidos = [0, 0]  # Turnos perdidos de los dos jugadores
    jugador_actual = 0  # 0 para Jugador 1, 1 para Jugador 2

    print("¡Bienvenido al Juego de la Oca!")
    print(f"El tablero tiene {NUM_CASILLAS} casillas.")
    print(f"Casillas de Oca: {CASILLAS_OCA}")
    print(f"Casillas Especiales: {CASILLAS_ESPECIALES}")
    print("-" * 30)

    while True:
        num_jugador_actual = jugador_actual + 1
        
        print(f"\n--- Turno del Jugador {num_jugador_actual} ---")
        print(f"Posición Jugador 1: {posiciones[0]}, Posición Jugador 2: {posiciones[1]}")

        if turnos_perdidos[jugador_actual] > 0:
            print(f"Jugador {num_jugador_actual}: Estás penalizado. Te saltas este turno.")
            print(f"Te quedan {turnos_perdidos[jugador_actual] - 1} turnos de penalización.")
            turnos_perdidos[jugador_actual] -= 1
            jugador_actual = 1 - jugador_actual  # Pasa al siguiente jugador
            continue

        input(f"Jugador {num_jugador_actual}, presiona Enter para lanzar el dado...")
        
        tirada = lanzar_dado()
        
        posicion_final, penalizacion, turno_extra = mover_ficha(
            posiciones[jugador_actual], tirada, num_jugador_actual
        )
        
        posiciones[jugador_actual] = posicion_final
        print(f"Jugador {num_jugador_actual} termina en la casilla {posiciones[jugador_actual]}.")

        if penalizacion > 0:
            turnos_perdidos[jugador_actual] = penalizacion
            print(f"Jugador {num_jugador_actual}: Penalizado con {penalizacion} turno(s).")

        if posiciones[jugador_actual] == NUM_CASILLAS:
            print(f"\n¡¡¡Felicidades, Jugador {num_jugador_actual}!!!")
            print(f"¡Has llegado a la casilla {NUM_CASILLAS} y ganado el juego!")
            break
        
        if turno_extra:
            print(f"Jugador {num_jugador_actual}: ¡Tienes un turno extra!")
            # No se cambia de jugador, continúa el mismo.
        else:
            jugador_actual = 1 - jugador_actual  # Alterna los turnos

# Inicia el juego
if __name__ == "__main__":
    jugar()