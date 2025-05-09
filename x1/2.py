import random

# Constantes del juego
NUM_CASILLAS = 63
FACES_DADO = 6
CASILLAS_OCA = [5, 9, 14, 18, 23, 27, 32, 36, 41, 45, 50, 54, 58]
CASILLAS_ESPECIALES = {
    6: "Puente",
    12: "Dados",
    19: "Posada",
    25: "Pozo",
    31: "Laberinto",
    42: "Muerte"
}

def lanzar_dado():
    """Simula el lanzamiento de un dado de seis caras."""
    return random.randint(1, FACES_DADO)

def mover_ficha(posicion_actual, dado):
    """Move la ficha según el resultado del dado y aplica las reglas del juego."""
    nueva_posicion = posicion_actual + dado
    
    if nueva_posicion > NUM_CASILLAS:
        nueva_posicion = 2 * NUM_CASILLAS - nueva_posicion  # Rebote

    if nueva_posicion in CASILLAS_ESPECIALES:
        rule = CASILLAS_ESPECIALES[nueva_posicion]
        print(f"¡Casilla especial! {rule}")
        if rule == "Puente":
            nueva_posicion = NUM_CASILLAS - (nueva_posicion % NUM_CASILLAS)
        elif rule == "Dados":
            dado2 = lanzar_dado()
            print(f"Lanzamiento adicional: {dado2}")
            nueva_posicion += dado2
            if nueva_posicion > NUM_CASILLAS:
                nueva_posicion = 2 * NUM_CASILLAS - nueva_posicion
        elif rule == "Posada":
            print("Pierdes un turno.")
            return posicion_actual  # Pierde un turno
        elif rule == "Pozo":
            print("Pierdes dos turnos.")
            return posicion_actual  # Pierde dos turnos
        elif rule == "Laberinto":
            nueva_posicion = 30
        elif rule == "Muerte":
            nueva_posicion = 1

    if nueva_posicion in CASILLAS_OCA:
        print("Casilla de la Oca, ¡avanza y tira de nuevo!")
        dado = lanzar_dado()
        nueva_posicion += dado
        if nueva_posicion > NUM_CASILLAS:
            nueva_posicion = 2 * NUM_CASILLAS - nueva_posicion
    
    return nueva_posicion

def jugar():
    """Función principal que gestiona el juego completo."""
    posiciones = [0, 0]  # Las posiciones iniciales de los dos jugadores
    turnos_perdidos = [0, 0]  # Los turnos perdidos de los dos jugadores
    turno = 0
    
    while True:
        input(f"Jugador {turno + 1}, presiona Enter para lanzar el dado...")
        
        if turnos_perdidos[turno] > 0:
            print(f"({turno + 1}) Pierde {turnos_perdidos[turno]} turno(s).")
            turnos_perdidos[turno] = 0  # Resetea los turnos perdidos al inicio del turno
        else:
            dado = lanzar_dado()
            print(f"({turno + 1}) Lanzamiento: {dado}")
            posiciones[turno] = mover_ficha(posiciones[turno], dado)
        
        print(f"Posición del jugador 1: {posiciones[0]}")
        print(f"Posición del jugador 2: {posiciones[1]}")
        
        if posiciones[turno] == NUM_CASILLAS:
            print(f"¡El jugador {turno + 1} ha ganado!")
            break
        
        turno = 1 - turno  # Alterna los turnos

# Inicia el juego
jugar()