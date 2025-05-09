import pygame
import sys

pygame.init()

# Configuraciones básicas
ANCHO, ALTO = 800, 600
FPS = 60
COLOR_FONDO = (0, 0, 0)
COLOR_BARRA = (255, 255, 255)
COLOR_BOLA = (255, 0, 0)
VEL_BOLA = [5, 5]

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pong")
reloj = pygame.time.Clock()

# Barras
barra1 = pygame.Rect(50, ALTO // 2 - 50, 10, 100)
barra2 = pygame.Rect(ANCHO - 60, ALTO // 2 - 50, 10, 100)

# Bola
bola = pygame.Rect(ANCHO // 2, ALTO // 2, 10, 10)

# Puntuaciones
puntuacion1 = 0
puntuacion2 = 0
fuente = pygame.font.Font(None, 74)

def actualizar_bola():
    global VEL_BOLA, puntuacion1, puntuacion2
    
    bola.x += VEL_BOLA[0]
    bola.y += VEL_BOLA[1]

    # Rebotar en las barras
    if bola.colliderect(barra1) or bola.colliderect(barra2):
        VEL_BOLA[0] = -VEL_BOLA[0]

    # Rebotar en los bordes superior e inferior
    if bola.top <= 0 or bola.bottom >= ALTO:
        VEL_BOLA[1] = -VEL_BOLA[1]

    # Punto para jugador 1
    if bola.left <= 0:
        puntuacion2 += 1
        bola.center = (ANCHO // 2, ALTO // 2)
        VEL_BOLA = [5, 5]

    # Punto para jugador 2
    if bola.right >= ANCHO:
        puntuacion1 += 1
        bola.center = (ANCHO // 2, ALTO // 2)
        VEL_BOLA = [5, 5]

def mover_barras():
    keys = pygame.key.get_pressed()
    
    # Mover barra izquierda
    if keys[pygame.K_w] and barra1.top > 0:
        barra1.y -= 7
    if keys[pygame.K_s] and barra1.bottom < ALTO:
        barra1.y += 7
        
    # Mover barra derecha
    if keys[pygame.K_UP] and barra2.top > 0:
        barra2.y -= 7
    if keys[pygame.K_DOWN] and barra2.bottom < ALTO:
        barra2.y += 7

def dibujar():
    pantalla.fill(COLOR_FONDO)
    pygame.draw.rect(pantalla, COLOR_BARRA, barra1)
    pygame.draw.rect(pantalla, COLOR_BARRA, barra2)
    pygame.draw.ellipse(pantalla, COLOR_BOLA, bola)
    
    texto1 = fuente.render(str(puntuacion1), True, COLOR_BARRA)
    pantalla.blit(texto1, (ANCHO // 4, 20))
    
    texto2 = fuente.render(str(puntuacion2), True, COLOR_BARRA)
    pantalla.blit(texto2, (3 * ANCHO // 4, 20))
    
    pygame.display.flip()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    actualizar_bola()
    mover_barras()
    dibujar()
    reloj.tick(FPS)