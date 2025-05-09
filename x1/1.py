import random

# Constantes del juego
NUM_CASILLAS = 63
FACES_DADO = 6
PLAYERS = ["Jugador 1", "Jugador 2"]

# Definición de las casillas especiales
CASILLAS_Oca = [5, 9, 14, 18, 23, 27, 32, 36, 41, 45, 50, 54, 58]
CASILLAS_PUENTE = [(6, 19), (12, 25), (28, 42), (35, 49), (46, 59)]
CASILLAS_DADOS = [17, 33, 48, 62]
CASILLAS_POSADA = [11, 29, 47, 61]
CASILLAS_POZO = [20, 38, 56]
CASILLAS_LABERINTO = 30
CASILLAS_MUERTE = 52

# Inicializa el tablero
tablero = [0] * NUM_CASILLAS

# Función para lanzar el dado
def lanzar_dado():
    return random.randint(1, FACES_DADO)

# Función para mover a un jugador
def mover_jugador(pos_actual, lanzamiento):
    nueva_pos = pos_actual + lanzamiento
    if nueva_pos > NUM_CASILLAS:
        nueva_pos = 2 * NUM_CASILLAS - nueva_pos  # Rebote
    return nueva_pos

# Función para aplicar reglas especiales
def aplicar_reglas(posicion):
    if posicion in CASILLAS_Oca:  # Casilla de la Oca
        print("¡Oca!")
        return mover_jugador(posicion, lanzar_dado())
    elif (posicion, posicion + lanzar_dado()) in CASILLAS_PUENTE:  # Puente
        print("¡Puente!")
        return NUM_CASILLAS - posicion
    elif posicion in CASILLAS_DADOS:  # Casilla de los Dados
        print("¡Dados!")
        return mover_jugador(posicion, lanzar_dado() + lanzar_dado())
    elif posicion in CASILLAS_POSADA:  # Posada
        print("¡Posada! Pierdes un turno.")
        return posicion
    elif posicion in CASILLAS_POZO:  # Pozo
        print("¡Pozo! Pierdes dos turnos.")
        return posicion
    elif posicion == CASILLAS_LABERINTO:  # Laberinto
        print("¡Laberinto! Retrocedes a la casilla 30.")
        return 29
    elif posicion == CASILLAS_MUERTE:  # Muerte
        print("¡Muerte! Vuelves al inicio.")
        return 0
    return posicion

# Función principal del juego
def jugar_juego():
    posiciones = [0, 0]
    turnos_perdidos = [0, 0]
    turno = 0

    while True:
        input(f"{PLAYERS[turno]}, presiona Enter para lanzar el dado...")
        
        if turnos_perdidos[turno] > 0:
            turnos_perdidos[turno] -= 1
            print(f"{PLAYERS[turno]} pierde un turno.")
            turno = (turno + 1) % 2
            continue
        
        lanzamiento = lanzar_dado()
        print(f"{PLAYERS[turno]} ha sacado un {lanzamiento} en el dado.")
        
        posiciones[turno] = mover_jugador(posiciones[turno], lanzamiento)
        print(f"{PLAYERS[turno]} está en la casilla {posiciones[turno]}.")
        
        posiciones[turno] = aplicar_reglas(posiciones[turno])
        print(f"{PLAYERS[turno]} está en la casilla {posiciones[turno]} después de aplicar reglas.")
        
        if posiciones[turno] == NUM_CASILLAS:
            print(f"¡{PLAYERS[turno]} ha ganado el juego!")
            break
        
        turno = (turno + 1) % 2

# Ejecutar el juego
jugar_juego()