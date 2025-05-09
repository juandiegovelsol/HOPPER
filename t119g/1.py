import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuraciones básicas
WIDTH, HEIGHT = 800, 600
FPS = 60
BALL_SPEED_X, BALL_SPEED_Y = 5, 5
PADDLE_SPEED = 7
BALL_SIZE = 15
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()

# Posiciones iniciales
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
player1_y, player2_y = HEIGHT // 2 - PADDLE_HEIGHT // 2, HEIGHT // 2 - PADDLE_HEIGHT // 2

ball_dx, ball_dy = BALL_SPEED_X, BALL_SPEED_Y

player1_score, player2_score = 0, 0

font = pygame.font.Font(None, 74)

# Función para dibujar todo
def draw():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (0, player1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - PADDLE_WIDTH, player2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    
    score_text = font.render(f'{player1_score}   {player2_score}', True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= PADDLE_SPEED
    if keys[pygame.K_s] and player1_y < HEIGHT - PADDLE_HEIGHT:
        player1_y += PADDLE_SPEED
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player2_y < HEIGHT - PADDLE_HEIGHT:
        player2_y += PADDLE_SPEED

    ball_x += ball_dx
    ball_y += ball_dy

    # Lógica de rebote en los bordes superior e inferior
    if ball_y <= 0 or ball_y + BALL_SIZE >= HEIGHT:
        ball_dy *= -1

    # Lógica de rebote en las paletas
    if (player1_y < ball_y < player1_y + PADDLE_HEIGHT and ball_x <= PADDLE_WIDTH) or \
       (player2_y < ball_y < player2_y + PADDLE_HEIGHT and ball_x + BALL_SIZE >= WIDTH - PADDLE_WIDTH):
        ball_dx *= -1

    # Lógica de puntuación
    if ball_x < 0:
        player2_score += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_dx *= -1
    elif ball_x > WIDTH:
        player1_score += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_dx *= -1

    draw()
    pygame.display.flip()
    clock.tick(FPS)