import pygame
import sys
import random

# Constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
GRAVITY = 0.5
JUMP_STRENGTH = 10
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
OBSTACLE_SPEED = 5

pygame.init()

# Configuración de pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juego de Saltos")

# Cargar recursos
player_image = pygame.Surface((50, 50))
player_image.fill((255, 0, 0))
obstacle_image = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
obstacle_image.fill((0, 255, 0))

# Posición inicial del jugador
player_pos = [SCREEN_WIDTH // 4, SCREEN_HEIGHT - 50]
player_vel = 0
player_on_ground = True

# Lista de obstáculos
obstacles = []

def add_obstacle():
    width = SCREEN_WIDTH - OBSTACLE_WIDTH
    x = width + random.randint(0, width // 2)
    obstacles.append(pygame.Rect(x, SCREEN_HEIGHT - OBSTACLE_HEIGHT, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

clock = pygame.time.Clock()

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and player_on_ground:
        player_vel = -JUMP_STRENGTH
        player_on_ground = False

    # Aplicar gravedad
    player_vel += GRAVITY
    player_pos[1] += player_vel

    # Chequear colisión con el suelo
    if player_pos[1] >= SCREEN_HEIGHT - 50:
        player_pos[1] = SCREEN_HEIGHT - 50
        player_vel = 0
        player_on_ground = True

    # Crear nuevos obstáculos
    if random.randint(1, 40) == 1:
        add_obstacle()

    # Mover obstáculos
    for obstacle in obstacles:
        obstacle.x -= OBSTACLE_SPEED
        if obstacle.x < -OBSTACLE_WIDTH:
            obstacles.remove(obstacle)

    # Chequear colisiones
    player_rect = pygame.Rect(player_pos[0], player_pos[1], 50, 50)
    for obstacle in obstacles:
        if player_rect.colliderect(obstacle):
            running = False

    # Dibujar todo
    screen.fill((0, 0, 0))
    screen.blit(player_image, player_pos)
    for obstacle in obstacles:
        screen.blit(obstacle_image, (obstacle.x, obstacle.y))
    
    pygame.display.flip()
    clock.tick(60)