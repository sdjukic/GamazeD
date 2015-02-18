#!/usr/bin/env python

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640,480), 0, 32)
pygame.display.set_caption("GamazeD")


DISPLAY_COLOR = (255, 255, 255)
WALLS = [((0,0), (250,0)), ((0,0), (0,250)), ((0,250), (250,250)), ((250,0), (250,250))]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
    for wall in WALLS:
        pygame.draw.line(screen, DISPLAY_COLOR, wall[0], wall[1], 1)
    
    pygame.draw.circle(screen, (255,255,255), (115,115), 13)
    
    pygame.display.update()