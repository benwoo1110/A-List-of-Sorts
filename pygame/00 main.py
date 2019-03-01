import pygame
import os
import time

from bubblesort import *
from quicksort import *
from mergesort import *
from insertionsort import *
from bogosort import *
from radixsort import *

# Initialization
pygame.init()
pygame.font.init()
window_size = (1000, 995)
screen = pygame.display.set_mode((1000, 700))
window = pygame.surface.Surface((window_size))
pygame.display.set_caption("A list of Sort")
scroll_y = 0

def scroll(event):
    global scroll_y, bubblesort_frame, quicksort_frame, mergesort_frame, insertionsort_frame, bogosort_frame, radixsort_frame
    
    # Scrollbar
    scrollbar_image = pygame.image.load('scrollbar_image.png').convert()
    isScrolling = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 4: scroll_y = min(scroll_y + 35, 0)
        if event.button == 5: scroll_y = max(scroll_y - 35, -295)

        if event.button == 4 or event.button == 5:
            scrollbar_image.set_alpha(170)

    screen.blit(window, (0, scroll_y))
    screen.blit(scrollbar_image, (window_size[0]-25, -int(scroll_y*(476/295))))
    update_draw()

    return scroll_y

def update_draw():
    pygame.display.flip()
    pygame.display.update()
    pygame.time.Clock().tick(1000000000)

def buffer():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        scroll(event)

# Colour sets
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
background_colour = pygame.Color(245, 138, 7)
config_colour = pygame.Color(67, 67, 67)
title_colour = pygame.Color(40, 40, 40)

# Font set
# title_font = pygame.font.SysFont('Helvetica Neue Bold', 85)
config_font = pygame.font.SysFont('Helvetica Neue Bold', 48)

# Title bar
title_height = 80
spacing = 30
mainscreen_image = pygame.image.load('mainscreen_image.png').convert()

# The 6 sorting boxes
sortingBoxes_size_w, sortingBoxes_size_h = (window_size[0]-(3*spacing))/2, (window_size[1]-title_height-(4*spacing))/3

bubblesort_frame = (spacing, title_height+spacing)
quicksort_frame = (window_size[0]-spacing-sortingBoxes_size_w, title_height+spacing)
mergesort_frame = (spacing, title_height+spacing*2+sortingBoxes_size_h)
insertionsort_frame = (window_size[0]-spacing-sortingBoxes_size_w, title_height+spacing*2+sortingBoxes_size_h)
bogosort_frame = (spacing, title_height+spacing*3+sortingBoxes_size_h*2)
radixsort_frame = (window_size[0]-spacing-sortingBoxes_size_w, title_height+spacing*3+sortingBoxes_size_h*2)

# Button setup
# Mainscreen button
bubblesort_btn = pygame.image.load('bubblesort_btn.png')
quicksort_btn = pygame.image.load('quicksort_btn.png')
mergesort_btn = pygame.image.load('mergesort_btn.png')
insertionsort_btn = pygame.image.load('insertionsort_btn.png')
bogosort_btn = pygame.image.load('bogosort_btn.png')
radixsort_btn = pygame.image.load('radixsort_btn.png')

# Config button
bubblesortConfig_btn = pygame.image.load('bubblesortConfig_btn.png')
quicksortConfig_btn = pygame.image.load('quicksortConfig_btn.png')
mergesortConfig_btn = pygame.image.load('mergesortConfig_btn.png')
insertionsortConfig_btn = pygame.image.load('insertionsortConfig_btn.png')
bogosortConfig_btn = pygame.image.load('bogosortConfig_btn.png')
radixsortConfig_btn = pygame.image.load('radixsortConfig_btn.png')

# More button
bubblesortMore_btn = pygame.image.load('bubblesortMore_btn.png')
quicksortMore_btn = pygame.image.load('quicksortMore_btn.png')
mergesortMore_btn = pygame.image.load('mergesortMore_btn.png')
insertionsortMore_btn = pygame.image.load('insertionsortMore_btn.png')
bogosortMore_btn = pygame.image.load('bogosortMore_btn.png')
radixsortMore_btn = pygame.image.load('radixsortMore_btn.png')

moreUnselected_btn = pygame.image.load('moreUnselected_btn.png')
moreSelected_btn = pygame.image.load('moreSelected_btn.png')

historySelected_btn = pygame.image.load('historySelected_btn.png')
infoSelected_btn = pygame.image.load('infoSelected_btn.png')

# Run button
runUnselected_btn = pygame.image.load('runUnselected_btn.png')
runSelected_btn = pygame.image.load('runSelected_btn.png')

# Fade in animation (NOT DONE)
def setup():
    window.blit(mainscreen_image, (0, 0))
    window.blit(bubblesort_btn, bubblesort_frame)
    window.blit(quicksort_btn, quicksort_frame)
    window.blit(mergesort_btn, mergesort_frame)
    window.blit(insertionsort_btn, insertionsort_frame)
    window.blit(bogosort_btn, bogosort_frame)
    window.blit(radixsort_btn, radixsort_frame)

    buffer()

setup()

# Sorting config
runBtn_x, runBtn_y, runBtn_w, runBtn_h = 305, 195, 150, 75
moreBtn_x, moreBtn_y, moreBtn_w, moreBtn_h = 373, 38, 47, 47
speedText_x, speedText_y, speedText_w, speedText_h = 146, 108, 145, 39 
listlengthText_x, listlengthText_y, listlengthText_w, listlengthText_h = 216, 152, 75, 39 
infoBtn_x, infoBtn_y, infoBtn_w, infoBtn_h = 90, 66, 275, 60
historyBtn_x, historyBtn_y, historyBtn_w, historyBtn_h = 90, 143, 275, 60
moreFrame_x, moreFrame_y, moreFrame_w, moreFrame_h = 73, 47, 310, 175
speed = float(1.0)
listlength = 10

def showConfig(frame, show_image):
    global scroll_y
    # frame = (frame[0], frame[1]-scroll_y)
    # Show image
    window.blit(show_image, frame)
    # Show config
    speedConfig_text = config_font.render(str(round(speed,1)) + ' x', True, config_colour)
    listlengthConfig_text = config_font.render(str(listlength), True, config_colour)
    window.blit(speedConfig_text,(frame[0]+speedText_x, frame[1]+speedText_y))
    window.blit(listlengthConfig_text,(frame[0]+listlengthText_x, frame[1]+listlengthText_y))

    # update_draw()
    # buffer()

def moreSelection(frame, show_image, more_image):
    global scroll_y
    mousePos = pygame.mouse.get_pos()

    infoSelected_drawn = False
    historySelected_drawn = False
    
    # Drawn the moreSelection page
    window.blit(more_image,frame)
    
    # While cursor in box
    while frame[0]+sortingBoxes_size_w > mousePos[0] > frame[0] and frame[1]+sortingBoxes_size_h+scroll_y > mousePos[1] > frame[1]+scroll_y:
        clicked = False

        for event in pygame.event.get():
            # Check for left click
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if event.button == 1: clicked = True
                else: clicked = False
            else: clicked = False
            
            # Cursor over info_btn
            if frame[0]+infoBtn_x+infoBtn_w > mousePos[0] > frame[0]+infoBtn_x and frame[1]+infoBtn_y+infoBtn_h+scroll_y > mousePos[1] > frame[1]+infoBtn_y+scroll_y:
                if not infoSelected_drawn:
                    window.blit(infoSelected_btn, (frame[0]+moreFrame_x, frame[1]+moreFrame_y))
                    infoSelected_drawn = True
            else: 
                if infoSelected_drawn:
                    window.blit(more_image,frame)
                    infoSelected_drawn = False

            # Cursor over history_btn 
            if frame[0]+historyBtn_x+historyBtn_w > mousePos[0] > frame[0]+historyBtn_x and frame[1]+historyBtn_y+historyBtn_h+scroll_y > mousePos[1] > frame[1]+historyBtn_y+scroll_y:
                if not historySelected_drawn:
                    window.blit(historySelected_btn, (frame[0]+moreFrame_x, frame[1]+moreFrame_y))
                    historySelected_drawn = True
            else: 
                if historySelected_drawn:
                    window.blit(more_image,frame)
                    historySelected_drawn = False
            
            # If click out of moreFrame
            if not(frame[0]+moreFrame_x+moreFrame_w > mousePos[0] > frame[0]+moreFrame_x and frame[1]+moreFrame_y+moreFrame_h+scroll_y > mousePos[1] > frame[1]+moreFrame_y+scroll_y) and clicked:
                # Show back config page
                showConfig(frame, show_image)
                return True
            scroll(event)
        
        mousePos = pygame.mouse.get_pos()

# Check if cursor in box
def cursor(frame, sort_image, show_image, more_image):
    global scroll_y, speed, listlength
    
    mousePos = pygame.mouse.get_pos()

    sortConfig_drawn = False
    clicked = False
    runSelected_drawn = False
    moreSelected_drawn = False

    # Cursor in frame of the box
    while frame[0]+sortingBoxes_size_w > mousePos[0] > frame[0] and frame[1]+sortingBoxes_size_h+scroll_y > mousePos[1] > frame[1]+scroll_y:
        # Change to sorConfig_btn
        if not sortConfig_drawn: 
            showConfig(frame, show_image)
            sortConfig_drawn = True
            # print(frame)
        
        # Mouse click in stepper
        clicked = False
        for event in pygame.event.get():
            # Check for left click
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if event.button == 1: clicked = True
                else: clicked = False
            else: clicked = False

            # Stepper for speed
            # click "-"
            if 0.3 < speed: # 0.2 is min number
                if frame[0]+speedText_x+speedText_w+50 > mousePos[0] > frame[0]+speedText_x+speedText_w and frame[1]+speedText_y+speedText_h+scroll_y > mousePos[1] > frame[1]+speedText_y+scroll_y:
                    if clicked:
                        speed -= 0.1
                        showConfig(frame, show_image)
            # click "+"
            if speed < 9.9: # 10.0 is max number
                if frame[0]+speedText_x+speedText_w+100 > mousePos[0] > frame[0]+speedText_x+speedText_w+50 and frame[1]+speedText_y+speedText_h+scroll_y > mousePos[1] > frame[1]+speedText_y+scroll_y:         
                    if clicked:
                        speed += 0.1
                        showConfig(frame, show_image)
                        
            # Stepper for listlength
            # click "-"
            if 1 < listlength: # 0 is min number
                if frame[0]+listlengthText_x+listlengthText_w+50 > mousePos[0] > frame[0]+listlengthText_x+listlengthText_w and frame[1]+listlengthText_y+speedText_h+scroll_y > mousePos[1] > frame[1]+listlengthText_y+scroll_y:
                    if clicked:
                        listlength -= 1
                        showConfig(frame, show_image)
            # click "+"
            if listlength < 100: # 100 is max number
                if frame[0]+listlengthText_x+listlengthText_w+100 > mousePos[0] > frame[0]+listlengthText_x+listlengthText_w+50 and frame[1]+listlengthText_y+speedText_h+scroll_y > mousePos[1] > frame[1]+listlengthText_y+scroll_y:
                    if clicked:
                        listlength += 1
                        showConfig(frame, show_image)

            scroll(event)

        # Cursor on more_btn
        while frame[0]+moreBtn_x+moreBtn_w > mousePos[0] > frame[0]+moreBtn_x and frame[1]+moreBtn_y+moreBtn_h+scroll_y > mousePos[1] > frame[1]+moreBtn_y+scroll_y:
            # Cursor on more_btn
            if not moreSelected_drawn:
                window.blit(moreSelected_btn, (frame[0]+moreBtn_x-10, frame[1]))
                moreSelected_drawn = True

            # Cursor click more_btn
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if event.button == 1: 
                        moreSelected_drawn = False
                        moreSelection(frame, show_image, more_image) # run sort algorithm
            
                scroll(event)
            
            mousePos = pygame.mouse.get_pos()

        # Cursor move out of more_btn
        if moreSelected_drawn:
            window.blit(moreUnselected_btn, (frame[0]+moreBtn_x-10, frame[1]))
            moreSelected_drawn = False

        # Cursor on run_btn
        while frame[0]+runBtn_x+runBtn_w > mousePos[0] > frame[0]+runBtn_x and frame[1]+runBtn_y+runBtn_h+scroll_y > mousePos[1] > frame[1]+runBtn_y+scroll_y:
            # if runSelected_btn not drawn 
            if not runSelected_drawn:
                window.blit(runSelected_btn, (frame[0]+runBtn_x, frame[1]+runBtn_y))
                runSelected_drawn = True

            # Cursor click run_btn
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if event.button == 1: return True # run sort algorithm
            
                scroll(event)
            
            mousePos = pygame.mouse.get_pos()


        # Cursor move out of run_btn
        if runSelected_drawn:
            window.blit(runUnselected_btn, (frame[0]+runBtn_x, frame[1]+runBtn_y))
            runSelected_drawn = False
            

        mousePos = pygame.mouse.get_pos()
    
    # Cursor is out of the box, change have to sort_btn
    if sortConfig_drawn: 
        buffer()
        window.blit(sort_image, frame)

# Main loop
while True:
    if cursor(bubblesort_frame, bubblesort_btn, bubblesortConfig_btn, bubblesortMore_btn):
        bubblesort(speed, listlength, False)
        setup()

    elif cursor(quicksort_frame, quicksort_btn, quicksortConfig_btn, quicksortMore_btn):
        quicksort(speed, listlength, False)
        setup()

    elif cursor(mergesort_frame, mergesort_btn, mergesortConfig_btn, mergesortMore_btn):
        mergesort(speed, listlength, False)
        setup()

    elif cursor(insertionsort_frame, insertionsort_btn, insertionsortConfig_btn, insertionsortMore_btn):
        insertionsort(speed, listlength, False)
        setup()

    elif cursor(bogosort_frame, bogosort_btn, bogosortConfig_btn, bogosortMore_btn):
        bogosort(speed, listlength, False)
        setup()

    elif cursor(radixsort_frame, radixsort_btn, radixsortConfig_btn, radixsortMore_btn):
        radixsort(speed, listlength, False)
        setup()

    buffer()










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
