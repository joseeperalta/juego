import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Constantes
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Cargar imágenes
nave_img = pygame.image.load("Nave.png")
nave_img = pygame.transform.scale(nave_img, (50, 50))

asteroide_img = pygame.image.load("aste.jpg")
asteroide_img = pygame.transform.scale(asteroide_img, (40, 40))

bala_img = pygame.Surface((5, 10))
bala_img.fill((255, 255, 0))

# Fuente para texto
fuente = pygame.font.SysFont(None, 30)

# Clase Nave
class Nave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = nave_img
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 60))
        self.velocidad = 5
        self.vidas = 3

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocidad
        if teclas[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.velocidad

# Clase Bala
class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bala_img
        self.rect = self.image.get_rect(center=(x, y))
        self.velocidad = -7

    def update(self):
        self.rect.y += self.velocidad
        if self.rect.bottom < 0:
            self.kill()

# Clase Asteroide
class Asteroide(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = asteroide_img
        self.rect = self.image.get_rect(center=(random.randint(0, WIDTH), -40))
        self.velocidad = random.randint(2, 5)

    def update(self):
        self.rect.y += self.velocidad
        if self.rect.top > HEIGHT:
            self.kill()

# Clase Juego principal
class Juego:
    def __init__(self):
        self.pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Asteroides con Clases y Sprites")
        self.clock = pygame.time.Clock()
        self.nave = Nave()
        self.grupo_nave = pygame.sprite.GroupSingle(self.nave)
        self.grupo_balas = pygame.sprite.Group()
        self.grupo_asteroides = pygame.sprite.Group()
        self.puntaje = 0
        self.tiempo_asteroide = 0
        self.ejecutando = True

    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.ejecutando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    bala = Bala(self.nave.rect.centerx, self.nave.rect.top)
                    self.grupo_balas.add(bala)

    def actualizar(self):
        # Generar asteroides cada cierto tiempo
        self.tiempo_asteroide += 1
        if self.tiempo_asteroide >= 30:
            self.grupo_asteroides.add(Asteroide())
            self.tiempo_asteroide = 0

        self.grupo_nave.update()
        self.grupo_balas.update()
        self.grupo_asteroides.update()

        # Colisiones: balas vs asteroides
        colisiones = pygame.sprite.groupcollide(self.grupo_balas, self.grupo_asteroides, True, True)
        self.puntaje += len(colisiones)

        # Colisiones: nave vs asteroides
        if pygame.sprite.spritecollide(self.nave, self.grupo_asteroides, True):
            self.nave.vidas -= 1
            if self.nave.vidas <= 0:
                self.ejecutando = False

    def dibujar(self):
        self.pantalla.fill(BLACK)
        self.grupo_nave.draw(self.pantalla)
        self.grupo_balas.draw(self.pantalla)
        self.grupo_asteroides.draw(self.pantalla)

        # Mostrar puntaje y vidas
        texto_puntaje = fuente.render(f"Puntaje: {self.puntaje}", True, WHITE)
        texto_vidas = fuente.render(f"Vidas: {self.nave.vidas}", True, WHITE)
        self.pantalla.blit(texto_puntaje, (10, 10))
        self.pantalla.blit(texto_vidas, (10, 40))

        pygame.display.flip()

    def ejecutar(self):
        while self.ejecutando:
            self.clock.tick(FPS)
            self.manejar_eventos()
            self.actualizar()
            self.dibujar() 

        # Fin del juego
        print("¡Juego terminado!")
        pygame.quit()
        sys.exit()

# Iniciar el juego
if __name__ == "__main__":
    juego = Juego()
    juego.ejecutar() 