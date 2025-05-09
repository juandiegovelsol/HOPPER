import pygame
import sys
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
GRAVITY = 0.5
JUMP_STRENGTH = 10
MAX_JUMPS = 5
OBSTACLE_SPEED = 5
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

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
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height:
            self.rect.y = SCREEN_HEIGHT - self.rect.height
            self.on_ground = True
            self.velocity_y = 0
            self.jumps_left = MAX_JUMPS
    
    def jump(self):
        if self.jumps_left > 0:
            self.velocity_y = -JUMP_STRENGTH
            self.jumps_left -= 1
            self.on_ground = False

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self):
        self.rect.x -= OBSTACLE_SPEED
        if self.rect.x <= -OBSTACLE_WIDTH:
            self.kill()

def initialize_game():
    """Inicializa pygame y crea la ventana de juego"""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Juego de Saltos Múltiples")
    clock = pygame.time.Clock()
    return screen, clock

def create_sprites():
    """Crea y devuelve los grupos de sprites y el jugador"""
    all_sprites = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    return all_sprites, obstacles, player

def create_obstacle(all_sprites, obstacles):
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

def handle_events(player):
    """Procesa los eventos de pygame y retorna si el juego debe continuar"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
    return True

def update_game_state(all_sprites, player, obstacles, score, spawn_timer):
    """Actualiza el estado del juego y verifica colisiones"""
    all_sprites.update()
    spawn_timer += 1
    score += 0.1
    
    if pygame.sprite.spritecollideany(player, obstacles):
        print(f"Fin del juego - Puntuación: {int(score)}")
        return score, spawn_timer, False

    if spawn_timer >= random.randint(60, 120):
        create_obstacle(all_sprites, obstacles)
        spawn_timer = 0
        
    return score, spawn_timer, True

def render_game(screen, all_sprites, score, player):
    """Dibuja todos los elementos en pantalla"""
    screen.fill(BLACK)
    all_sprites.draw(screen)
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Puntuación: {int(score)}", True, WHITE)
    jumps_text = font.render(f"Saltos: {player.jumps_left}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(jumps_text, (10, 50))
    
    pygame.display.flip()

def main():
    """Función principal que ejecuta el juego"""
    screen, clock = initialize_game()
    all_sprites, obstacles, player = create_sprites()
    
    running = True
    spawn_timer = 0
    score = 0
    
    while running:
        clock.tick(FPS)
        running = handle_events(player)
        score, spawn_timer, game_active = update_game_state(all_sprites, player, obstacles, score, spawn_timer)
        running = running and game_active
        render_game(screen, all_sprites, score, player)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()