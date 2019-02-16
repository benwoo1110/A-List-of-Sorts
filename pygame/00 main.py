import pygame
import os
import time

from bubblesort import *
from quicksort import *
from mergesort import *

# Initialization
pygame.init()
pygame.font.init()
window_size = (1000, 700)
window = pygame.display.set_mode((window_size))
pygame.display.set_caption("A list of Sort")

def update_draw():
    pygame.display.flip()
    pygame.display.update()
    pygame.time.Clock().tick(1000000000)

def buffer():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

# Colour sets
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
yellow_bg = pygame.Color(245, 138, 7)

# Font set
title_font = pygame.font.SysFont('Arial', 50)

# Top title bar
title_height = 70
spacing = 30

def setTitle():
    window.fill(yellow_bg)
    title_text = title_font.render('Sorting', True, (0, 0, 0))
    window.blit(title_text,(spacing,5))
    pygame.draw.rect(window, black, (spacing, title_height, window_size[0]-(2*spacing), 1), 0)
    update_draw()

# The 4 sorting boxes
sortingBoxes_size_w, sortingBoxes_size_h = (window_size[0]-(3*spacing))/2, (window_size[1]-title_height-(3*spacing))/2

bubblesort_frame = (spacing, title_height+spacing)
quicksort_frame = (window_size[0]-spacing-sortingBoxes_size_w, title_height+spacing)
mergesort_frame = (spacing, window_size[1]-spacing-sortingBoxes_size_h)
insertionsort_frame = (window_size[0]-spacing-sortingBoxes_size_w, window_size[1]-spacing-sortingBoxes_size_h)

bubblesort_btn = pygame.image.load('bubblesort_btn.png').convert()
quicksort_btn = pygame.image.load('quicksort_btn.png').convert()
mergesort_btn = pygame.image.load('mergesort_btn.png').convert()
insertionsort_btn = pygame.image.load('insertionsort_btn.png').convert()

def setBoxes():
    window.blit(bubblesort_btn, bubblesort_frame)
    window.blit(quicksort_btn, quicksort_frame)
    window.blit(mergesort_btn, mergesort_frame)
    window.blit(insertionsort_btn, insertionsort_frame)

    update_draw()

setTitle()
setBoxes()

# Clicking action
run_btn = pygame.image.load('run_btn.png').convert()

# Check if cursor in box
def cursor(frame, sort_image):
    mouse_pos = pygame.mouse.get_pos()
    if frame[0]+sortingBoxes_size_w > mouse_pos[0] > frame[0] and frame[1]+sortingBoxes_size_h > mouse_pos[1] > frame[1]:
        window.blit(run_btn, frame)
        update_draw()
        # Mouse click in box
        if event.type == pygame.MOUSEBUTTONDOWN:
            return True
    else:
        window.blit(sort_image, frame)
        update_draw()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if cursor(bubblesort_frame, bubblesort_btn):
            bubblesort()
            setTitle() # Reset
            setBoxes()
        elif cursor(quicksort_frame, quicksort_btn):
            quicksort()
            setTitle() # Reset
            setBoxes()
        elif cursor(mergesort_frame, mergesort_btn):
            mergesort()
            setTitle() # Reset
            setBoxes()
        elif cursor(insertionsort_frame, insertionsort_btn): # Algorithm not done
            # insertionsort()
            setTitle() # Reset
            setBoxes()










'''
        # Cursor in bubblesort
        bubblesortChange = False
        if bubblesort_frame[0]+sortingBoxes_size_w > mouse_pos[0] > bubblesort_frame[0] and bubblesort_frame[1]+sortingBoxes_size_h > mouse_pos[1] > bubblesort_frame[1]:
            bubblesortChange= True
            for i in range(100, 256, 15):
                mouse_pos = pygame.mouse.get_pos()
                if bubblesort_frame[0]+sortingBoxes_size_w > mouse_pos[0] > bubblesort_frame[0] and bubblesort_frame[1]+sortingBoxes_size_h > mouse_pos[1] > bubblesort_frame[1]:
                    run_btn.set_alpha(i)
                    window.blit(run_btn, bubblesort_frame)
                    update_draw()
                    buffer()
                else: break
        if bubblesortChange:
            bubblesortChange = False
            for i in range(100, 256, 15):
                mouse_pos = pygame.mouse.get_pos()
                if bubblesort_frame[0]+sortingBoxes_size_w > mouse_pos[0] > bubblesort_frame[0] and bubblesort_frame[1]+sortingBoxes_size_h > mouse_pos[1] > bubblesort_frame[1]:
                    break
                else:
                    bubblesort_btn.set_alpha(i)
                    window.blit(bubblesort_btn, bubblesort_frame)
                    update_draw()
                    buffer()

        # Cursor in quicksort
        if quicksort_frame[0]+sortingBoxes_size_w > mouse_pos[0] > quicksort_frame[0] and quicksort_frame[1]+sortingBoxes_size_h > mouse_pos[1] > quicksort_frame[1]:
            for i in range(100, 256, 15):
                mouse_pos = pygame.mouse.get_pos()
                if quicksort_frame[0]+sortingBoxes_size_w > mouse_pos[0] > quicksort_frame[0] and quicksort_frame[1]+sortingBoxes_size_h > mouse_pos[1] > quicksort_frame[1]:
                    run_btn.set_alpha(i)
                    window.blit(run_btn, quicksort_frame)
                    update_draw()
                    buffer()
                else: break
        else:
            for i in range(100, 256, 15):
                mouse_pos = pygame.mouse.get_pos()
                if quicksort_frame[0]+sortingBoxes_size_w > mouse_pos[0] > quicksort_frame[0] and quicksort_frame[1]+sortingBoxes_size_h > mouse_pos[1] > quicksort_frame[1]:
                    break
                else:
                    quicksort_btn.set_alpha(i)
                    window.blit(quicksort_btn, quicksort_frame)
                    update_draw()
                    buffer()
'''
