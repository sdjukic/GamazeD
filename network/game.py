#!/usr/bin/env python

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640,480), 0, 32)
pygame.display.set_caption("GamazeD")


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
            
    pygame.draw.line(screen, (255,255,255), (100,100), (100, 350), 1)
    pygame.draw.line(screen, (255,255,255), (100,100), (350, 100), 1)
    pygame.draw.line(screen, (255,255,255), (350,100), (350, 350), 1)
    pygame.draw.line(screen, (255,255,255), (100,350), (350, 350), 1)
    
    pygame.draw.circle(screen, (255,255,255), (115,115), 13)
    
    pygame.display.update()