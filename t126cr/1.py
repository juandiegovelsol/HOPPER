import pygame
import sys
import random

# Constantes de configuración del juego
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
GRAVITY = 0.5
JUMP_STRENGTH = 10
MAX_JUMPS = 5
OBSTACLE_SPEED = 5
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
FPS = 60

# Inicializar Pygame
pygame.init()

# Configurar pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juego de Saltos Múltiples")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

# Definir la clase Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = SCREEN_HEIGHT - self.rect.height
        self.velocity_y = 0
        self.on_ground = False
        self.jumps_left = MAX_JUMPS

    def update(self):
        # Aplicar gravedad
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y
        
        # Verificar colisión con el suelo
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height:
            self.rect.y = SCREEN_HEIGHT - self.rect.height
            self.on_ground = True
            self.velocity_y = 0
            self.jumps_left = MAX_JUMPS

    def jump(self):
        # Hacer saltar al jugador si está en el suelo
        if self.jumps_left > 0 and self.on_ground:
            self.velocity_y = -JUMP_STRENGTH
            self.jumps_left -= 1
            self.on_ground = False

# Definir la clase Obstacle
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # Mover obstáculo hacia la izquierda
        self.rect.x -= OBSTACLE_SPEED
        
        # Eliminar obstáculo si sale de la pantalla
        if self.rect.x <= -OBSTACLE_WIDTH:
            self.kill()

# Crear grupos de sprites
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Función para crear un obstáculo aleatorio
def create_obstacle():
    x = SCREEN_WIDTH
    level = random.choice([0, 1, 2])
    
    if level == 0:
        y = SCREEN_HEIGHT - OBSTACLE_HEIGHT
    elif level == 1:
        y = SCREEN_HEIGHT - OBSTACLE_HEIGHT - 100
    else:
        y = SCREEN_HEIGHT - OBSTACLE_HEIGHT - 200
        
    obstacle = Obstacle(x, y)
    all_sprites.add(obstacle)
    obstacles.add(obstacle)

# Función principal del juego
def main_game_loop():
    # Variables de juego
    running = True
    spawn_timer = 0
    score = 0
    
    while running:
        clock.tick(FPS)
        spawn_timer += 1
        score += 0.1

        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()
        
        # Actualizar sprites
        all_sprites.update()

        # Verificar colisiones
        if pygame.sprite.spritecollideany(player, obstacles):
            print(f"Game Over - Puntuación: {int(score)}")
            running = False

        # Crear obstáculos
        if spawn_timer >= random.randint(60, 120):
            create_obstacle()
            spawn_timer = 0

        # Renderizar pantalla
        screen.fill(BLACK)
        all_sprites.draw(screen)
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Puntuación: {int(score)}", True, WHITE)
        jumps_text = font.render(f"Saltos: {player.jumps_left}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(jumps_text, (10, 50))
        pygame.display.flip()

# Iniciar el juego
if __name__ == "__main__":
    main_game_loop()
    pygame.quit()
    sys.exit()