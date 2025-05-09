import random

# Constantes del juego
NUM_CASILLAS = 63
FACES_DADO = 6
PLAYERS = ["Jugador 1", "Jugador 2"]

# Definición de las casillas especiales (numeración 1-63)
CASILLAS_OCA = [5, 9, 14, 18, 23, 27, 32, 36, 41, 45, 50, 54, 58]
CASILLAS_PUENTE = {6: 19, 19: 6, 12: 25, 25: 12}
CASILLAS_DADOS_PARES = {17: 33, 33: 17, 48: 62, 62: 48}
CASILLAS_POSADA = [11, 29, 47, 61]
CASILLAS_POZO = [20, 38, 56]
CASILLA_LABERINTO = 30
CASILLA_MUERTE = 52

# Función para lanzar el dado
def lanzar_dado():
    return random.randint(1, FACES_DADO)

# Función para mover a un jugador
def mover_jugador(pos_actual, lanzamiento):
    if pos_actual == 0:
        nueva_pos = lanzamiento
    else:
        nueva_pos = pos_actual + lanzamiento

    if nueva_pos > NUM_CASILLAS:
        nueva_pos = NUM_CASILLAS - (nueva_pos - NUM_CASILLAS) # Rebote
    return nueva_pos

# Función para aplicar reglas especiales
# Devuelve: (nombre_regla_aplicada, nueva_posicion, concede_turno_extra, turnos_a_perder)
def aplicar_reglas_especiales(posicion, jugador_actual_nombre):
    # Oca: "De oca a oca y tiro porque me toca"
    if posicion in CASILLAS_OCA:
        nombre_regla = "Oca"
        try:
            idx_oca_actual = CASILLAS_OCA.index(posicion)
            if idx_oca_actual < len(CASILLAS_OCA) - 1:
                siguiente_oca = CASILLAS_OCA[idx_oca_actual + 1]
                print(f"Avanza a la siguiente Oca en la casilla {siguiente_oca} y tira de nuevo.") # El "tira de nuevo" lo gestiona el turno extra
                return nombre_regla, siguiente_oca, True, 0
            else: # Última oca
                print(f"¡Es la última Oca! Avanza a la meta (casilla {NUM_CASILLAS}) y tira de nuevo.")
                return nombre_regla, NUM_CASILLAS, True, 0
        except ValueError:
             return None, posicion, False, 0 # No debería pasar

    # Puente: "De puente a puente y tiro porque me lleva la corriente"
    if posicion in CASILLAS_PUENTE:
        nombre_regla = "Puente"
        destino_puente = CASILLAS_PUENTE[posicion]
        print(f"Se mueve a la casilla {destino_puente} y tira de nuevo.")
        return nombre_regla, destino_puente, True, 0

    # Dados: "De dado a dado y tiro porque me ha tocado"
    if posicion in CASILLAS_DADOS_PARES:
        nombre_regla = "Dados"
        destino_dados = CASILLAS_DADOS_PARES[posicion]
        print(f"Se mueve a la otra casilla de Dados en {destino_dados} y tira de nuevo.")
        return nombre_regla, destino_dados, True, 0

    # Posada: "Pierde un turno"
    if posicion in CASILLAS_POSADA:
        nombre_regla = "Posada"
        print(f"¡{jugador_actual_nombre} ha caído en la Posada! Pierde 1 turno.")
        return nombre_regla, posicion, False, 1

    # Pozo: "Pierde dos turnos"
    if posicion in CASILLAS_POZO:
        nombre_regla = "Pozo"
        print(f"¡{jugador_actual_nombre} ha caído en el Pozo! Pierde 2 turnos.")
        return nombre_regla, posicion, False, 2

    # Laberinto: "Retrocede a la casilla 30"
    if posicion == CASILLA_LABERINTO:
        nombre_regla = "Laberinto"
        print(f"¡{jugador_actual_nombre} ha caído en el Laberinto! Retrocede a la casilla 30.")
        return nombre_regla, 30, False, 0

    # Muerte: "Vuelve al inicio"
    if posicion == CASILLA_MUERTE:
        nombre_regla = "Muerte"
        print(f"¡{jugador_actual_nombre} ha caído en la Muerte! Vuelve al inicio (casilla 0).")
        return nombre_regla, 0, False, 0

    return None, posicion, False, 0 # Ninguna regla especial aplicada

# Función principal del juego
def jugar_juego():
    posiciones = [0] * len(PLAYERS)
    turnos_perdidos = [0] * len(PLAYERS)
    turno_jugador_idx = 0

    print("¡Bienvenido al Juego de la Oca!")
    print(f"Tablero de {NUM_CASILLAS} casillas.")
    print("Los jugadores empiezan fuera del tablero (posición 0).")
    print("-" * 30)

    while True:
        jugador_actual_nombre = PLAYERS[turno_jugador_idx]
        posicion_actual_jugador_inicio_turno = posiciones[turno_jugador_idx]

        print(f"\n--- Turno de {jugador_actual_nombre} ---")
        print(f"Posición actual: Casilla {posicion_actual_jugador_inicio_turno if posicion_actual_jugador_inicio_turno > 0 else 'Salida'}")

        if turnos_perdidos[turno_jugador_idx] > 0:
            print(f"{jugador_actual_nombre} pierde este turno. Turnos restantes de penalización: {turnos_perdidos[turno_jugador_idx]-1}")
            turnos_perdidos[turno_jugador_idx] -= 1
            turno_jugador_idx = (turno_jugador_idx + 1) % len(PLAYERS)
            continue

        input(f"{jugador_actual_nombre}, presiona Enter para lanzar el dado...")
        lanzamiento = lanzar_dado()
        print(f"{jugador_actual_nombre} ha sacado un {lanzamiento} en el dado.")

        posicion_despues_de_mover = mover_jugador(posicion_actual_jugador_inicio_turno, lanzamiento)
        print(f"{jugador_actual_nombre} se mueve a la casilla {posicion_despues_de_mover}.")
        posiciones[turno_jugador_idx] = posicion_despues_de_mover
        
        concede_turno_extra_global = False
        
        # Bucle para procesar efectos de la casilla de aterrizaje.
        # Se detiene si una regla de "mover y tirar de nuevo" (Oca, Puente, Dados) se activa,
        # para permitir que la nueva tirada ocurra en el siguiente ciclo del turno.
        while True:
            posicion_antes_aplicar_regla_actual = posiciones[turno_jugador_idx]

            nombre_regla, nueva_posicion_tras_regla, regla_actual_concede_turno_extra, penalizacion_turnos = aplicar_reglas_especiales(
                posicion_antes_aplicar_regla_actual,
                jugador_actual_nombre
            )
            
            posiciones[turno_jugador_idx] = nueva_posicion_tras_regla

            if nombre_regla:
                 print(f"{jugador_actual_nombre} activó la regla '{nombre_regla}' en la casilla {posicion_antes_aplicar_regla_actual}.")

            if penalizacion_turnos > 0:
                print(f"Por la regla '{nombre_regla}', {jugador_actual_nombre} pierde {penalizacion_turnos} turno(s).")
                turnos_perdidos[turno_jugador_idx] = penalizacion_turnos
            
            if regla_actual_concede_turno_extra:
                concede_turno_extra_global = True # Marca que este jugador tendrá otro turno

            # Si la regla movió al jugador
            if posiciones[turno_jugador_idx] != posicion_antes_aplicar_regla_actual:
                print(f"Como resultado de '{nombre_regla}', {jugador_actual_nombre} ahora está en la casilla {posiciones[turno_jugador_idx]}.")

                if posiciones[turno_jugador_idx] == NUM_CASILLAS: # Si la regla lleva a la meta
                    break 

                # Si la regla que acaba de mover al jugador es una que concede turno extra (Oca, Puente, Dados),
                # el jugador se detiene en esa nueva casilla y el bucle de reglas termina aquí.
                # El turno extra se gestionará fuera de este bucle.
                if regla_actual_concede_turno_extra:
                    break 
                
                # Si la regla movió pero NO concedió turno extra (ej. Laberinto te mueve a 30),
                # el bucle continúa para ver si la casilla 30 (la nueva posición) es a su vez especial.
                # (Ej: Laberinto que lleva a una Posada).
            else:
                # La regla no movió al jugador (o no hubo regla aplicable en esta casilla). Salir del bucle de efectos.
                break
        
        print(f"Posición final de {jugador_actual_nombre} en esta acción: Casilla {posiciones[turno_jugador_idx] if posiciones[turno_jugador_idx] > 0 else 'Salida'}")

        if posiciones[turno_jugador_idx] == NUM_CASILLAS:
            print("-" * 30)
            print(f"¡¡¡{jugador_actual_nombre} ha llegado exactamente a la casilla {NUM_CASILLAS} y ha ganado el juego!!!")
            print("-" * 30)
            break

        if not concede_turno_extra_global:
            turno_jugador_idx = (turno_jugador_idx + 1) % len(PLAYERS)
        else:
            print(f"¡{jugador_actual_nombre} tiene un turno extra por la regla '{nombre_regla}'!") # nombre_regla aquí será la última que concedió turno extra

if __name__ == "__main__":
    jugar_juego()