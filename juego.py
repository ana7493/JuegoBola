#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import sys, pygame
from pygame.locals import *
 
# Constantes
WIDTH = 235
HEIGHT = 350
 

 
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
 
    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
 
        screen.blit(background_image, (0, 0))
        pygame.display.flip()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()