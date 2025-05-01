import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar dimensiones de la ventana
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Plataformas")

# Configurar colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Clase para el jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO // 2, ALTO // 2)
        self.velocidad_x = 0
        self.velocidad_y = 0
        self.en_suelo = False

    def update(self):
        self.velocidad_y += 1  # Gravedad
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        # Limitar el movimiento
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO

        # Si el jugador cae de la pantalla, reiniciar posición
        if self.rect.bottom > ALTO:
            self.rect.center = (ANCHO // 2, ALTO // 2)

    def saltar(self):
        if self.en_suelo:
            self.velocidad_y = -15
            self.en_suelo = False

# Crear grupos de sprites
todos_los_sprites = pygame.sprite.Group()
jugador = Jugador()
todos_los_sprites.add(jugador)

# Bucle principal del juego
reloj = pygame.time.Clock()
corriendo = True
while corriendo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corriendo = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                jugador.velocidad_x = -5
            if event.key == pygame.K_d:
                jugador.velocidad_x = 5
            if event.key == pygame.K_SPACE:
                jugador.saltar()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                jugador.velocidad_x = 0

    # Actualizar sprites
    todos_los_sprites.update()

    # Dibujar
    pantalla.fill(NEGRO)
    todos_los_sprites.draw(pantalla)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar los frames por segundo
    reloj.tick(60)

pygame.quit()
sys.exit()