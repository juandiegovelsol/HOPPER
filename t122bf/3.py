import pygame
import sys

ANCHO, ALTO = 800, 600
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 20
JUGADOR_WIDTH, JUGADOR_HEIGHT = 40, 40
VELOCIDAD_Y_SALTO = -15
GRAVEDAD = 0.8
VELOCIDAD_X = 5
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
GRIS_CIELO = (200, 200, 240) 

pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Plataformas Horizontal")
reloj = pygame.time.Clock()
fuente = pygame.font.Font(None, 36)

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
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.vel_x = -VELOCIDAD_X
        elif keys[pygame.K_d]:
            self.vel_x = VELOCIDAD_X
        else:
            self.vel_x = 0

        self.rect.x += self.vel_x
        lista_colisiones_x = pygame.sprite.spritecollide(self, plataformas, False)
        for plat in lista_colisiones_x:
            if self.vel_x > 0:
                self.rect.right = plat.rect.left
            elif self.vel_x < 0:
                self.rect.left = plat.rect.right
            self.vel_x = 0 

        self.en_suelo = False
        self.vel_y += GRAVEDAD
        if self.vel_y > 20:
            self.vel_y = 20

        self.rect.y += self.vel_y

        lista_colisiones_y = pygame.sprite.spritecollide(self, plataformas, False)
        for plat in lista_colisiones_y:
            if self.vel_y > 0 and self.rect.bottom <= plat.rect.top + self.vel_y + 1:
                 self.rect.bottom = plat.rect.top
                 self.vel_y = 0
                 self.en_suelo = True
            elif self.vel_y < 0 and self.rect.top >= plat.rect.bottom + self.vel_y - 1:
                 self.rect.top = plat.rect.bottom
                 self.vel_y = 0

        if keys[pygame.K_SPACE] and self.en_suelo:
            self.vel_y = VELOCIDAD_Y_SALTO
            self.en_suelo = False

    def reiniciar_posicion(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.vel_x = 0
        self.en_suelo = False

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

niveles = [
    [ (50, ALTO - 50, 'inicio'),
      (200, ALTO - 100, 'normal'),
      (350, ALTO - 150, 'normal'),
      (500, ALTO - 100, 'normal'),
      (650, ALTO - 50, 'meta') ],
    [ (50, ALTO - 50, 'inicio'),
      (150, ALTO - 120, 'normal'),
      (300, ALTO - 200, 'normal'),
      (400, ALTO - 280, 'normal'),
      (550, ALTO - 200, 'normal'),
      (700, ALTO - 150, 'meta') ],
     [ (20, ALTO - 40, 'inicio'),
      (150, ALTO - 100, 'normal'),
      (230, ALTO - 180, 'normal'),
      (350, ALTO - 120, 'normal'),
      (480, ALTO - 250, 'normal'),
      (600, ALTO - 350, 'normal'),
      (700, ALTO - 400, 'meta') ]
]

nivel_actual_indice = 0
estado_juego = "jugando"
plataformas = pygame.sprite.Group()
jugadores = pygame.sprite.Group()
jugador = None

def cargar_nivel(indice_nivel):
    global jugador, plataformas, jugadores, estado_juego
    plataformas.empty()
    jugadores.empty()

    if indice_nivel >= len(niveles):
        return "juego_ganado"

    nivel = niveles[indice_nivel]
    x_inicio, y_inicio = 0, 0

    for plat_info in nivel:
        x, y, tipo = plat_info
        plataforma = Plataforma(x, y, tipo)
        plataformas.add(plataforma)
        if tipo == 'inicio':
            x_inicio = plataforma.rect.centerx - JUGADOR_WIDTH // 2
            y_inicio = plataforma.rect.top - JUGADOR_HEIGHT

    if jugador is None:
        jugador = Jugador(x_inicio, y_inicio)
    else:
        jugador.reiniciar_posicion(x_inicio, y_inicio)

    jugadores.add(jugador)
    estado_juego = "jugando"
    return "jugando"

estado_juego = cargar_nivel(nivel_actual_indice)

while True:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                if estado_juego == "game_over":
                    estado_juego = cargar_nivel(nivel_actual_indice)
                elif estado_juego == "nivel_completado":
                    nivel_actual_indice += 1
                    estado_juego = cargar_nivel(nivel_actual_indice) 
                elif estado_juego == "juego_ganado":
                    nivel_actual_indice = 0
                    estado_juego = cargar_nivel(nivel_actual_indice)

    if estado_juego == "jugando":
        jugador.update(plataformas)

        if jugador.rect.top > ALTO:
            estado_juego = "game_over"

        for plat in plataformas: # Se comprueban colisiones en todas las pataformas
            if plat.tipo == 'meta' and jugador.en_suelo: # Se verifica que la plataforma sea del tipo correcto
                # Se conprueba si el jugador está sobre la plataforma meta
                if (jugador.rect.bottom == plat.rect.top and 
                    jugador.rect.right > plat.rect.left and 
                    jugador.rect.left < plat.rect.right):
                    estado_juego = "nivel_completado"
                    break


    pantalla.fill(GRIS_CIELO)
    plataformas.draw(pantalla)
    jugadores.draw(pantalla)

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

    pygame.display.flip()
    reloj.tick(60)