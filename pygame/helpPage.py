import pygame
import os
import time
from dataclasses import dataclass

import main

@dataclass
class sort(object):
    name : str
    frame : tuple
    sort_btn : pygame.Surface
    config_btn : pygame.Surface
    more_btn : pygame.Surface
    last_run : str
    speed : str

helpsort = sort(
    name='mergesort', 
    frame=(spacing, 405), 
    sort_btn=pygame.image.load('helpmergesort_btn.png'), 
    config_btn=pygame.image.load('helpmergesortConfig_btn.png'), 
    more_btn=pygame.image.load('helpmergesortMore_btn.png'),
    last_run='--',
    speed='Fast')


# Colour sets
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
background_colour = pygame.Color(245, 138, 7)
config_colour = pygame.Color(67, 67, 67)
title_colour = pygame.Color(40, 40, 40)

# Font set
config_font = pygame.font.SysFont('Helvetica Neue Bold', 46)

# Image
helpscreen_image = pygame.image.load('helpscreen_image.png')

def update_draw():
    pygame.display.flip()
    pygame.display.update()
    pygame.time.Clock().tick(1000000000)

def buffer():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit()
        scroll(event)


def help_run():
    window.blit(helpscreen_image, (0,0))
    update_draw()
    main.sortSelection(mergesort)

