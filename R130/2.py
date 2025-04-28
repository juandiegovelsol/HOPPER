import random

def iniciar_juego():
    """Inicializa el juego, asigna colores a los jugadores y comienza la primera ronda."""
    jugadores = [x.strip() for x in input("Ingrese los nombres de los jugadores separados por una coma y un espacio: ").split(",")]
    
    colores = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"]
    asignaciones_colores = {jugador: colores[i % len(colores)] for i, jugador in enumerate(jugadores)}
    
    print("\nAsignación de colores:")
    for jugador, color in asignaciones_colores.items():
        print(f"{color}{jugador}\033[0m")
    
    print("\n¡Que comience el juego!")
    iniciar_ronda(jugadores, asignaciones_colores)

def iniciar_ronda(jugadores, asignaciones_colores):
    """Inicia una ronda del juego, ordena a los jugadores y maneja la ejecución de turnos."""
    jugadores_shuffled = jugadores[:]
    random.shuffle(jugadores_shuffled)
    oracion = "Hola mundo"

    while True:
        print("\nNueva ronda:")
        for turno, jugador in enumerate(jugadores_shuffled, 1):
            print(f"\nTurno {turno}: {jugador} (Color: {asignaciones_colores[jugador]})")
            print(f"Oración actual: {oracion}")
            try:
                respuesta = input("Agrega una palabra al final de la oración: ")
                if not validar_respuesta(oracion, respuesta):
                    raise ValueError("La respuesta es incorrecta.")
                oracion += f" {respuesta}"
            except ValueError as e:
                print(f"\033[91m{jugador} ha perdido la partida!\033[0m")
                return

        print(f"\nLa oración completa es: {oracion}")
        jugadores_shuffled.append(jugadores_shuffled.pop(0))  # Rotar jugadores

def validar_respuesta(oracion_anterior, nueva_palabra):
    """Verifica que la nueva palabra no repita una anterior y no esté incompleta."""
    palabras_anteriores = oracion_anterior.split()[1:]
    return nueva_palabra.strip() not in palabras_anteriores

# Ejecutar el juego
iniciar_juego()