import pygame
import sys

# Constantes
ANCHO, ALTO = 800, 600
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 20
JUGADOR_WIDTH, JUGADOR_HEIGHT = 40, 40
VELOCIDAD_Y_SALTO = -15  # Velocidad de salto inicial
GRAVEDAD = 0.8
VELOCIDAD_X = 5

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0) # Para la plataforma de inicio
ROJO = (255, 0, 0) # Para la plataforma meta
GRIS_CIELO = (200, 200, 240) # Color de fondo

# Inicializar pygame
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Plataformas Horizontal")
reloj = pygame.time.Clock()
fuente = pygame.font.Font(None, 36) # Fuente para mensajes

# Clase Jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self, x_inicial, y_inicial):
        super().__init__()
        self.image = pygame.Surface((JUGADOR_WIDTH, JUGADOR_HEIGHT))
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.x = x_inicial
        self.rect.y = y_inicial
        self.vel_y = 0
        self.vel_x = 0
        self.en_suelo = False

    def update(self, plataformas):
        # Movimiento Horizontal
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.vel_x = -VELOCIDAD_X
        elif keys[pygame.K_d]:
            self.vel_x = VELOCIDAD_X
        else:
            self.vel_x = 0 # Detenerse si no se presiona A o D

        self.rect.x += self.vel_x

        # Colisiones Horizontales
        lista_colisiones_x = pygame.sprite.spritecollide(self, plataformas, False)
        for plat in lista_colisiones_x:
            if self.vel_x > 0: # Moviéndose a la derecha
                self.rect.right = plat.rect.left
            elif self.vel_x < 0: # Moviéndose a la izquierda
                self.rect.left = plat.rect.right
            self.vel_x = 0 # Detener movimiento horizontal al chocar


        # Movimiento Vertical y Gravedad
        self.en_suelo = False

        # Aplicar gravedad
        self.vel_y += GRAVEDAD
        # Limitar velocidad de caída
        if self.vel_y > 20:
            self.vel_y = 20

        self.rect.y += self.vel_y

        # Colisiones Verticales
        lista_colisiones_y = pygame.sprite.spritecollide(self, plataformas, False)
        for plat in lista_colisiones_y:
            # Comprobar si colisionamos por ABAJO (aterrizando)
            # Usamos un pequeño margen para asegurar que la colisión sea desde arriba
            if self.vel_y > 0 and self.rect.bottom <= plat.rect.top + self.vel_y + 1:
                 self.rect.bottom = plat.rect.top
                 self.vel_y = 0
                 self.en_suelo = True
            # Comprobar si colisionamos por ARRIBA (golpeando con la cabeza)
            elif self.vel_y < 0 and self.rect.top >= plat.rect.bottom + self.vel_y - 1:
                 self.rect.top = plat.rect.bottom
                 self.vel_y = 0 # Detener el salto al golpear techo

        # Salto
        if keys[pygame.K_SPACE] and self.en_suelo:
            self.vel_y = VELOCIDAD_Y_SALTO
            self.en_suelo = False # Ya no está en el suelo después de saltar

    def reiniciar_posicion(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.vel_x = 0
        self.en_suelo = False


# Clase Plataforma
class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, tipo='normal'):
        super().__init__()
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.tipo = tipo

        if self.tipo == 'inicio':
            self.image.fill(VERDE)
        elif self.tipo == 'meta':
            self.image.fill(ROJO)
        else:
            self.image.fill(NEGRO)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Definición de Niveles
niveles = [
    # Nivel 1
    [ (50, ALTO - 50, 'inicio'),
      (200, ALTO - 100, 'normal'),
      (350, ALTO - 150, 'normal'),
      (500, ALTO - 100, 'normal'),
      (650, ALTO - 50, 'meta') ],
    # Nivel 2
    [ (50, ALTO - 50, 'inicio'),
      (150, ALTO - 120, 'normal'),
      (300, ALTO - 200, 'normal'),
      (400, ALTO - 280, 'normal'),
      (550, ALTO - 200, 'normal'),
      (700, ALTO - 150, 'meta') ],
    # Nivel 3 (Más difícil)
     [ (20, ALTO - 40, 'inicio'),
      (150, ALTO - 100, 'normal'),
      (230, ALTO - 180, 'normal'),
      (350, ALTO - 120, 'normal'),
      (480, ALTO - 250, 'normal'),
      (600, ALTO - 350, 'normal'),
      (700, ALTO - 400, 'meta') ]
]

# Estado del Juego
nivel_actual_indice = 0
estado_juego = "jugando"

# Grupos de Sprites
plataformas = pygame.sprite.Group()
jugadores = pygame.sprite.Group()
jugador = None

# Función para cargar nivel
def cargar_nivel(indice_nivel):
    global jugador, plataformas, jugadores, estado_juego

    # Limpiar sprites anteriores
    plataformas.empty()
    jugadores.empty()

    if indice_nivel >= len(niveles):
        # Si no hay más niveles, el juego se ha ganado
        return "juego_ganado"

    nivel = niveles[indice_nivel]
    x_inicio, y_inicio = 0, 0 # Valores por defecto

    for plat_info in nivel:
        x, y, tipo = plat_info
        plataforma = Plataforma(x, y, tipo)
        plataformas.add(plataforma)
        if tipo == 'inicio':
            # Guardamos la posición de inicio para el jugador
            # Colocamos al jugador un poco encima de la plataforma de inicio
            x_inicio = plataforma.rect.centerx - JUGADOR_WIDTH // 2
            y_inicio = plataforma.rect.top - JUGADOR_HEIGHT

    # Crear/Recrear el jugador en la posición de inicio
    if jugador is None:
        jugador = Jugador(x_inicio, y_inicio)
    else:
        jugador.reiniciar_posicion(x_inicio, y_inicio)

    jugadores.add(jugador)
    estado_juego = "jugando" # Asegurarse de que el estado vuelve a 'jugando'
    return "jugando" # Devuelve el nuevo estado

# Cargar el primer nivel
estado_juego = cargar_nivel(nivel_actual_indice)

# Bucle principal del juego
while True:
    # Manejo de Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Reiniciar/Avanzar con Tecla Enter
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN: # Tecla Enter
                if estado_juego == "game_over":
                    estado_juego = cargar_nivel(nivel_actual_indice) # Reinicia nivel actual
                elif estado_juego == "nivel_completado":
                    nivel_actual_indice += 1
                    estado_juego = cargar_nivel(nivel_actual_indice) # Carga siguiente nivel
                elif estado_juego == "juego_ganado":
                    nivel_actual_indice = 0
                    estado_juego = cargar_nivel(nivel_actual_indice)

    # Lógica del Juego
    if estado_juego == "jugando":
        jugador.update(plataformas)

        # Comprobar Condiciones
        # 1. Caída (Derrota)
        if jugador.rect.top > ALTO:
            estado_juego = "game_over"

        # 2. Llegar a la meta (Victoria de Nivel)
        for plat in plataformas:
            if plat.tipo == 'meta' and jugador.en_suelo:
                # Comprobamos si el jugador está sobre la plataforma meta
                if (jugador.rect.bottom == plat.rect.top and 
                    jugador.rect.right > plat.rect.left and 
                    jugador.rect.left < plat.rect.right):
                    estado_juego = "nivel_completado"
                    break

    # Renderizado
    pantalla.fill(GRIS_CIELO)

    # Dibujar plataformas y jugador
    plataformas.draw(pantalla)
    jugadores.draw(pantalla)

    # Mostrar Mensajes según Estado
    mensaje = ""
    if estado_juego == "game_over":
        mensaje = "¡Has perdido! Presiona Enter para reiniciar."
    elif estado_juego == "nivel_completado":
        mensaje = f"¡Nivel {nivel_actual_indice + 1} superado! Presiona Enter."
    elif estado_juego == "juego_ganado":
        mensaje = "¡Felicidades! ¡Has ganado! Presiona Enter para volver a jugar."

    if mensaje:
        texto_renderizado = fuente.render(mensaje, True, NEGRO)
        rect_texto = texto_renderizado.get_rect(center=(ANCHO // 2, ALTO // 2))
        pantalla.blit(texto_renderizado, rect_texto)

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar FPS
    reloj.tick(60)