#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Importamos las siguientes librerias
import sys, pygame
from pygame.locals import *
#Tamaño de la ventana 
WIDTH = 820
HEIGHT = 700
#Movimiento de imagen .png vertical y horizontalmente  
class Bola(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("imagenes/foto7.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speed = [0.5, -0.5]
 

    def actualizar(self, time, persona1):
        self.rect.centerx += self.speed[0] * time
        self.rect.centery += self.speed[1] * time
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1] * time
 
        if pygame.sprite.collide_rect(self, persona1):
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
            self.rect.centery += self.speed[0] * time
        if pygame.sprite.collide_rect(self, persona1):
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
            self.rect.centery += self.speed[0] * time
 
class Persona(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("imagenes/foto6.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = 0.5
 #Movimiento de la imagen hacia arriba abajo derecha y izquierda 
    def mover(self, time, keys):
        if self.rect.top >= 0:
            if keys[K_UP]:
                self.rect.centery -= self.speed * time 
        if self.rect.bottom <= HEIGHT:
            if keys[K_DOWN]:
                self.rect.centery += self.speed * time

        if self.rect.left >= 0:
            if keys[K_LEFT]:
                self.rect.centerx -= self.speed * time
        if self.rect.right <= WIDTH:
            if keys[K_RIGHT]:
                self.rect.centerx += self.speed * time
# Cargamos la imagen y le decimos que imprima por pantalla si no la encuentra o es incorrecto
def load_image(filename, transparent=False):  
    try:
        image = pygame.image.load(filename)    
    except pygame.error as message:   
        print("No carga la imagen " + filename)
        raise SystemExit(message)    
    return image.convert_alpha()

# Ahora empezaremos con el main definiendo el fondo de pantalla 
 
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("juego")
    background_image = load_image('imagenes/foto1.jpg')
    bola = Bola()
    persona1 = Persona(630,630)
    clock = pygame.time.Clock()
 #y dandole valor a la imagenes y el tiempo que tarda en realizar esos movimeinto segun lo rapido que vaya
    while True:
        time = clock.tick(60)
        keys = pygame.key.get_pressed()
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        bola.actualizar(time, persona1)
        persona1.mover(time, keys)
        screen.blit(background_image, (0, 0))
        screen.blit(persona1.image, persona1.rect)
        screen.blit(bola.image, bola.rect)
        pygame.display.flip()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()