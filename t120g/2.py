import pygame
import sys

# Constantes del juego
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
GRAVITY = 0.5
JUMP_STRENGTH = 10
OBSTACLE_SPEED = 5
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
FPS = 60

# Inicializar Pygame
pygame.init()

# Configurar pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juego de Saltos")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Reloj
clock = pygame.time.Clock()

# Clase del jugador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = SCREEN_HEIGHT - self.rect.height
        self.velocity_y = 0
        self.on_ground = False

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = -JUMP_STRENGTH
            self.on_ground = False

        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        if self.rect.y >= SCREEN_HEIGHT - self.rect.height:
            self.rect.y = SCREEN_HEIGHT - self.rect.height
            self.on_ground = True
            self.velocity_y = 0

    def jump(self):
        if self.on_ground:
            self.velocity_y = -JUMP_STRENGTH
            self.on_ground = False

# Clase de obstáculos
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -= OBSTACLE_SPEED
        if self.rect.x <= 0:
            self.kill()

# Grupos de sprites
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Función para crear obstáculos
def create_obstacle():
    x = SCREEN_WIDTH
    y = SCREEN_HEIGHT - OBSTACLE_HEIGHT
    obstacle = Obstacle(x, y)
    all_sprites.add(obstacle)
    obstacles.add(obstacle)

# Bucle principal del juego
running = True
spawn_timer = 0
while running:
    clock.tick(FPS)
    spawn_timer += 1

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar sprites
    all_sprites.update()

    # Verificar colisiones
    if pygame.sprite.spritecollideany(player, obstacles):
        print("Game Over")
        running = False

    # Crear obstáculos
    if spawn_timer >= 90:  # Ajusta la frecuencia de aparición de obstáculos
        create_obstacle()
        spawn_timer = 0

    # Dibujar todo
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()