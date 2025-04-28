import random
import os

# Función para limpiar la consola
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para resaltar texto
def resaltar(texto, color):
    return f"\033[{color}m{texto}\033[0m"

# Función para crear un jugador
def crear_jugador(nombre):
    return {
        'nombre': nombre.strip(),
        'color': random.choice([31, 32, 33, 34, 35, 36]),  # Rojo, Verde, Amarillo, Azul, Morado, Cian
        'puntuacion': 0
    }

# Función para obtener los colores disponibles
def obtener_colores_disponibles(jugadores):
    colores = [31, 32, 33, 34, 35, 36]
    colores_usados = [jugador['color'] for jugador in jugadores]
    return [color for color in colores if color not in colores_usados]

# Función para inicializar jugadores
def inicializar_jugadores():
    print("Ingrese los nombres de los jugadores separados por una coma y un espacio:")
    nombres = input().split(", ")
    jugadores = [crear_jugador(nombre) for nombre in nombres]
    random.shuffle(jugadores)  # Mezclar jugadores para orden aleatorio
    return jugadores

# Función para elegir un jugador al azar
def elegir_jugador_aleatorio(jugadores):
    return random.choice(jugadores)

# Función para crear una oración inicial
def crear_oracion_inicial():
    return "La vida es bella"

# Función para añadir palabra a la oración
def añadir_palabra_a_oracion(oracion, nueva_palabra):
    return f"{oracion} {nueva_palabra}"

# Función principal del juego
def juego():
    jugadores = inicializar_jugadores()
    oracion_actual = crear_oracion_inicial()
    ronda = 1

    while True:
        limpiar_consola()
        print(f"Ronda {ronda}")
        print("Oración actual:", resaltar(oracion_actual, '32'))
        
        jugador_actual = elegir_jugador_aleatorio(jugadores)
        print(f"Turno de {resaltar(jugador_actual['nombre'], jugador_actual['color'])}")
        
        nueva_palabra = input("Agrega una nueva palabra a la oración: ").strip()
        oracion_actual = añadir_palabra_a_oracion(oracion_actual, nueva_palabra)
        
        # Aquí validarías si la oración es correcta o no
        # Por ejemplo, si la oración no coincide, termina el juego
        if "se" in oracion_actual:  # Ejemplo de validación simple
            print(f"Error en la oración: {resaltar(jugador_actual['nombre'], '31')} pierde!")
            break
        
        # Cambiar de turno (podrías implementar aquí cómo reordenar los jugadores si lo necesitas)
        input("Presiona Enter para continuar...")
        ronda += 1

juego()