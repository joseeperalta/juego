rosa= (208, 171, 227, 1)
blanco=(238,238,228)
import pygame
#importo librerias
import sys
import random

#Constanes
WIDTH = 1000#ancho
HEIGHT = 900#alto

class Asteroide:
    def __init__(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = 0 #comienza desde arriba
        self.velocidad=random.randint(2,5)
        self.radio=20

    def mover(self):
        self.y += self.velocidad

    def dibujar(self, superficie):
        pygame.draw.circle(superficie, rosa, (self.x, self.y), self.radio)
             
def main():#Funcion principal del juego
    pygame.init()#iniciar pygame
#creamos la screen = pygame.display.set_mode((width,height)) y le indicamos un titulo:
    ventana=pygame.display.set_mode((WIDTH , HEIGHT))
    pygame.display.set_caption("CAE")
    aste=Asteroide()
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        aste.mover()
        
        ventana.fill((blanco))
        
        aste.dibujar(ventana)
        
        pygame.display.flip()
        pygame.display.update()
        pygame.time.Clock(). tick(60)
    
if __name__ == "__main__":#si no hay un error en principal, funcion a main
    main()
    