import pygame
import random
import sys

# Inicialización
pygame.init()
ANCHO, ALTO = 600, 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mini Frogger")

# Colores
VERDE = (34, 177, 76) 
NEGRO = (0, 0, 0)
ROJO = (200, 0, 0)
BLANCO = (255, 255, 255)

# Jugador
jugador = pygame.Rect(275, 550, 50, 50)
velocidad_jugador = 50

# Enemigos (autos)
enemigos = []
for i in range(5):
    y = 100 + i * 80
    x = random.randint(0, ANCHO - 200)
    velocidad = random.randint(3, 6)
    enemigos.append({"rect": pygame.Rect(x, y, 100, 40), "vel": velocidad})

# Fuente
fuente = pygame.font.SysFont(None, 48)

# Relojimport pygame
import random
import sys

# Inicialización
pygame.init()
ANCHO, ALTO = 600, 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("CROCKI")

# Colores
VERDE = (34, 177, 76)
NEGRO = (0, 0, 0)
ROJO = (200, 0, 0)
BLANCO = (255, 255, 255)

# Jugador
jugador = pygame.Rect(275, 550, 50, 50)
velocidad_jugador = 10

# Enemigos (autos)
enemigos = []
for i in range(5):
    y = 100 + i * 80
    x = random.randint(0, ANCHO - 100)
    velocidad = random.randint(3, 6)
    enemigos.append({"rect": pygame.Rect(x, y, 100, 40), "vel": velocidad})

# Fuente
fuente = pygame.font.SysFont(None, 48)

# Reloj
clock = pygame.time.Clock()

# Función para mostrar texto
def mostrar_texto(texto, color, y_offset=0):
    texto_render = fuente.render(texto, True, color)
    rect = texto_render.get_rect(center=(ANCHO // 2, ALTO // 2 + y_offset))
    VENTANA.blit(texto_render, rect)

# Bucle principal
ejecutando = True
ganaste = False

while ejecutando:
    clock.tick(30)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento del jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP] and jugador.top > 0:
        jugador.y -= velocidad_jugador
    if teclas[pygame.K_DOWN] and jugador.bottom < ALTO:
        jugador.y += velocidad_jugador
    if teclas[pygame.K_LEFT] and jugador.left > 0:
        jugador.x -= velocidad_jugador
    if teclas[pygame.K_RIGHT] and jugador.right < ANCHO:
        jugador.x += velocidad_jugador

    # Mover enemigos
    for enemigo in enemigos:
        enemigo["rect"].x += enemigo["vel"]
        if enemigo["rect"].left > ANCHO:
            enemigo["rect"].right = 0
            enemigo["vel"] = random.randint(3, 6)

    # Colisiones
    for enemigo in enemigos:
        if jugador.colliderect(enemigo["rect"]):
            jugador.y = 550  # Reinicia posición

    # Ver si gana
    if jugador.top <= 0:
        ganaste = True
        ejecutando = False

    # Dibujar
    VENTANA.fill(VERDE)
    pygame.draw.rect(VENTANA, NEGRO, jugador)
    for enemigo in enemigos:
        pygame.draw.rect(VENTANA, ROJO, enemigo["rect"])

    pygame.display.flip()

# Pantalla de victoria
VENTANA.fill(VERDE)
mostrar_texto("¡Ganaste!", BLANCO)
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()
clock = pygame.time.Clock()

# Función para mostrar texto
def mostrar_texto(texto, color, y_offset=0):
    texto_render = fuente.render(texto, True, color)
    rect = texto_render.get_rect(center=(ANCHO // 2, ALTO // 2 + y_offset))
    VENTANA.blit(texto_render, rect)

# Bucle principal
ejecutando = True
ganaste = False

while ejecutando:
    clock.tick(30)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento del jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP] and jugador.top > 0:
        jugador.y -= velocidad_jugador
    if teclas[pygame.K_DOWN] and jugador.bottom < ALTO:
        jugador.y += velocidad_jugador
    if teclas[pygame.K_LEFT] and jugador.left > 0:
        jugador.x -= velocidad_jugador
    if teclas[pygame.K_RIGHT] and jugador.right < ANCHO:
        jugador.x += velocidad_jugador

    # Mover enemigos
    for enemigo in enemigos:
        enemigo["rect"].x += enemigo["vel"]
        if enemigo["rect"].left > ANCHO:
            enemigo["rect"].right = 0
            enemigo["vel"] = random.randint(3, 6)

    # Colisiones
    for enemigo in enemigos:
        if jugador.colliderect(enemigo["rect"]):
            jugador.y = 550  # Reinicia posición

    # Ver si gana
    if jugador.top <= 0:
        ganaste = True
        ejecutando = False

    # Dibujar
    VENTANA.fill(VERDE)
    pygame.draw.rect(VENTANA, NEGRO, jugador)
    for enemigo in enemigos:
        pygame.draw.rect(VENTANA, ROJO, enemigo["rect"])

    pygame.display.flip()

# Pantalla de victoria
VENTANA.fill(VERDE)
mostrar_texto("¡Ganaste!", BLANCO)
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()