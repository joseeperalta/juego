import pygame
import random
import sys

# Inicializar pygame
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Asteroids con POO")
clock = pygame.time.Clock()

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Tamaños
SHIP_SIZE = (50, 50)
ASTEROID_SIZE = (40, 40)
BULLET_SIZE = (5, 10)

class Nave:
    def __init__(self):
        self.image = pygame.Surface(SHIP_SIZE)
        self.image.fill((0, 100, 255))
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 60))
        self.velocidad = 5

    def mover(self, teclas):
        if teclas[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocidad
        if teclas[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.velocidad

    def dibujar(self, superficie):
        superficie.blit(self.image, self.rect)

class Bala:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, *BULLET_SIZE)
        self.velocidad = -7

    def mover(self):
        self.rect.y += self.velocidad

    def dibujar(self, superficie):
        pygame.draw.rect(superficie, (255, 255, 0), self.rect)

class Asteroide:
    def __init__(self):
        x = random.randint(0, WIDTH - ASTEROID_SIZE[0])
        self.rect = pygame.Rect(x, -40, *ASTEROID_SIZE)
        self.velocidad = random.randint(2, 5)

    def mover(self):
        self.rect.y += self.velocidad

    def dibujar(self, superficie):
        pygame.draw.rect(superficie, (200, 50, 50), self.rect)

class Juego:
    def __init__(self):
        self.nave = Nave()
        self.balas = []
        self.asteroides = []
        self.puntaje = 0
        self.spawn_timer = 0
        self.running = True

    def generar_asteroides(self):
        self.spawn_timer += 1
        if self.spawn_timer >= 30:
            self.asteroides.append(Asteroide())
            self.spawn_timer = 0

    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.running = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    x = self.nave.rect.centerx - BULLET_SIZE[0] // 2
                    y = self.nave.rect.top
                    self.balas.append(Bala(x, y))

    def actualizar(self):
        teclas = pygame.key.get_pressed()
        self.nave.mover(teclas)

        for bala in self.balas[:]:
            bala.mover()
            if bala.rect.bottom < 0:
                self.balas.remove(bala)

        for asteroide in self.asteroides[:]:
            asteroide.mover()
            if asteroide.rect.top > HEIGHT:
                self.asteroides.remove(asteroide)

        # Detectar colisiones
        for bala in self.balas[:]:
            for asteroide in self.asteroides[:]:
                if bala.rect.colliderect(asteroide.rect):
                    self.balas.remove(bala)
                    self.asteroides.remove(asteroide)
                    self.puntaje += 1
                    break

        self.generar_asteroides()

    def dibujar(self):
        screen.fill(BLACK)
        self.nave.dibujar(screen)

        for bala in self.balas:
            bala.dibujar(screen)

        for asteroide in self.asteroides:
            asteroide.dibujar(screen)

        # Mostrar puntaje
        fuente = pygame.font.SysFont(None, 30)
        texto = fuente.render(f"Puntaje: {self.puntaje}", True, WHITE)
        screen.blit(texto, (10, 10))

        pygame.display.flip()

    def bucle_principal(self):
        while self.running:
            self.manejar_eventos()
            self.actualizar()
            self.dibujar()
            clock.tick(60)

# Ejecutar el juego
if __name__ == "__main__":
    juego = Juego()
    juego.bucle_principal()
    pygame.quit()
    sys.exit()