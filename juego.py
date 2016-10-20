#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, pygame
from pygame.locals import *
 
WIDTH = 820
HEIGHT = 700
 
class Persona(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("imagenes/foto6.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = 0.5
 
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
 
def load_image(filename, transparent=False):  
    try:
        image = pygame.image.load(filename)    
    except pygame.error as message:   
        print("No carga la imagen " + filename)
        raise SystemExit(message)    
    return image.convert_alpha()
# ---------------------------------------------------------------------
 
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("juego")
    background_image = load_image('imagenes/foto1.jpg')
    persona = Persona(630,630)
    clock = pygame.time.Clock()
 
    while True:
        time = clock.tick(60)
        keys = pygame.key.get_pressed()
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        persona.mover(time, keys)
        screen.blit(background_image, (0, 0))
        screen.blit(persona.image, persona.rect)
        pygame.display.flip()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()