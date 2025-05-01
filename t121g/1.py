import pygame
import sys

# Constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLATFORM_WIDTH = 200
PLATFORM_HEIGHT = 20
JUGADOR_WIDTH = 40
JUGADOR_HEIGHT = 40
GRAVEDAD = 0.5
VELOCIDAD_SALTO = -10

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)

class Jugador(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((JUGADOR_WIDTH, JUGADOR_HEIGHT))
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.vel_y = 0
        self.en_suelo = False

    def update(self, plataformas):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 5
        if keys[pygame.K_d]:
            self.rect.x += 5

        if self.en_suelo and keys[pygame.K_SPACE]:
            self.vel_y = VELOCIDAD_SALTO
            self.en_suelo = False

        self.vel_y += GRAVEDAD
        self.rect.y += self.vel_y

        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.vel_y = 0
            self.en_suelo = True

        self.colision_plataformas(plataformas)

    def colision_plataformas(self, plataformas):
        for plataforma in plataformas:
            if self.rect.colliderect(plataforma.rect):
                if self.vel_y > 0:
                    self.rect.bottom = plataforma.rect.top
                    self.vel_y = 0
                    self.en_suelo = True

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Juego de Plataformas")

    jugador = Jugador(100, SCREEN_HEIGHT - 150)
    plataformas = pygame.sprite.Group()
    plataforma1 = Plataforma(200, SCREEN_HEIGHT - 200)
    plataforma2 = Plataforma(400, SCREEN_HEIGHT - 300)
    plataforma3 = Plataforma(600, SCREEN_HEIGHT - 400)

    plataformas.add(plataforma1)
    plataformas.add(plataforma2)
    plataformas.add(plataforma3)

    todos_sprites = pygame.sprite.Group()
    todos_sprites.add(jugador)
    todos_sprites.add(plataformas)

    reloj = pygame.time.Clock()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        todos_sprites.update(plataformas)

        pantalla.fill(BLANCO)
        todos_sprites.draw(pantalla)
        pygame.display.flip()

        reloj.tick(30)

if __name__ == "__main__":
    main()