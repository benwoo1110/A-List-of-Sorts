import pygame
from random import randint
import time
from dataclasses import dataclass

from history import addHistory
from history import history_run
from sound import Note
from information import information_run 

@dataclass
class coordinates(object):
    x : int
    y : int
    w : int
    h : int

# Declaring Variables
window_size = (1000, 700)

listLength = 0
titleHeight = 128
maxHeight = 390
spacing = 75

numOfSwaps = 0
runTime = 0
runSpeed = 0
swap = False
backSelected_drawn = False
infoSelected_drawn = False
sort_done = False
isPause = False

heightList_orginal = []
heightList = []
xList, y, w = [], 0, 0

window = pygame.display.set_mode((window_size))
pygame.init()

# colours
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
stats_colour = pygame.Color(67, 67, 67)
background_colour = pygame.Color(245, 138, 7)

# Font set
pygame.font.init()
stats_font = pygame.font.SysFont('Helvetica Neue Bold', 50)

# Load images
bubblesortAlgo_image = pygame.image.load('bubblesortAlgo_image.png')
backSelected_btn = pygame.image.load('backSelected_btn.png')
backUnselected_btn = pygame.image.load('backUnselected_btn.png')
replay_btn = pygame.image.load('replay_btn.png')

sortInfoSelected_btn = pygame.image.load('sortInfoSelected_btn.png')
sortInfoUnselected_btn = pygame.image.load('sortInfoUnselected_btn.png')

# UI Coordinates
backBtn_x, backBtn_y, backBtn_w, backBtn_h = 48, 28, 42, 42
optionsBtn_x, optionsBtn_y, optionsBtn_w, optionsBtn_h = 905, 17, 65, 65
replayBtn_x, replayBtn_y, replayBtn_w, replayBtn_h=791, 454, 165, 54

option_Frame = coordinates(x=661, y=96, w=310, h=175)
info_btn = coordinates(x=905, y=17, w=65, h=65)
infomation_btn = coordinates(x=678, y=114, w=275, h=60)
history_btn = coordinates(x=678, y=192, w=275, h=60)

# Fade in animation
def animate_fadein():
    for i in range(160, 257, 32):
        bubblesortAlgo_image.set_alpha(i)
        window.blit(bubblesortAlgo_image, (0, 0))
        update_draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()

def rect_draw(colour, x, y, w, h):
    global window
    pygame.draw.rect(window, colour, (x, y, w, h), 0)

def update_draw():
    pygame.display.flip()
    pygame.display.update()
    pygame.time.Clock().tick(1000000000)

def draw():
    global xList, y, heightList, listLength, numOfSwaps, backSelected_drawn, optionSelected_drawn, sort_done

    # Draw UI
    window.blit(bubblesortAlgo_image,(0, 0))
    if backSelected_drawn: # Show BackSelected_btn
        window.blit(backSelected_btn,(0, 0))

    if infoSelected_drawn: # Show optionSelected_btn
        window.blit(sortInfoSelected_btn, (info_btn.x-10, 0))

    update_draw()

    time_current = runTime
    if not sort_done:
        time_current = time.time() - runTime

    # show stats
    timeStats_text = stats_font.render(str(round(time_current, 3)) + " sec", True, stats_colour)
    swapStats_text = stats_font.render(str(numOfSwaps), True, stats_colour)
    speedStats_text = stats_font.render(str(round(runSpeed, 1)) + " x", True, stats_colour)
    listlengthStats_text = stats_font.render(str(int(listLength)), True, stats_colour)

    window.blit(timeStats_text, (300, 570))
    window.blit(swapStats_text, (392, 617))
    window.blit(speedStats_text, (739, 570))
    window.blit(listlengthStats_text, (794, 617))

    for i in range(listLength):
        rect_draw(white, xList[i], maxHeight+titleHeight-heightList[i], w, heightList[i])

def click_action(replay):
    global backSelected_drawn, infoSelected_drawn

    clicked = False

    for event in pygame.event.get():
        # Check for left click
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if event.button == 1: clicked = True
            else: clicked = False
        else: clicked = False

        mousePos = pygame.mouse.get_pos()

        # If cursor over back_btn
        if backBtn_x+backBtn_w > mousePos[0] > backBtn_x and backBtn_y+backBtn_h > mousePos[1] > backBtn_y:
            if not backSelected_drawn: 
                window.blit(backSelected_btn, (0, 0))
                update_draw()
                backSelected_drawn = True                    
            if clicked: return 'back' # check if back_btn clicked
        else: 
            if backSelected_drawn: 
                window.blit(backUnselected_btn, (0, 0))
                update_draw()
                backSelected_drawn = False

        # Info button
        if info_btn.x+info_btn.w > mousePos[0] > info_btn.x and info_btn.y+info_btn.h > mousePos[1] > info_btn.y:
            if not infoSelected_drawn: 
                window.blit(sortInfoSelected_btn, (info_btn.x-10, 0))
                update_draw()
                infoSelected_drawn = True                    
            if clicked: 
                pause()
                information_run('bubblesort')
                pause()
                draw()
                update_draw()
                return 'next'
        else: 
            if infoSelected_drawn: 
                window.blit(sortInfoUnselected_btn, (info_btn.x-10, 0))
                update_draw()
                infoSelected_drawn = False

        # Replay button
        if replayBtn_x+replayBtn_w > mousePos[0] > replayBtn_x and replayBtn_y+replayBtn_h > mousePos[1] > replayBtn_y and replay:
            if clicked:
                sort_done = False
                bubblesort_run(runSpeed, listLength, True)
                return 'end'

        if event.type == pygame.QUIT: pygame.quit()

def btn_click():
    global runSpeed

    for i in range(int(400/runSpeed)):
        mousePos = pygame.mouse.get_pos()
        action = click_action(False)
        if action == 'next': break
        if action == 'end' or action == 'back': return True

        time.sleep(0.001)  

def bubblesort_run(speed, length, replay):
    global heightList_orginal, heightList, xList, w, listLength, titleHeight, maxHeight, spacing, numOfSwaps, runTime, swap, runSpeed, sort_done

    # Change accordance to length and speed input
    listLength = length
    w = (window_size[0]-spacing*2)//listLength
    spacing = (window_size[0]-w*listLength)//2
    numOfSwaps = 0
    runSpeed = speed
    
    if replay: 
        # Get previous heightList
        heightList = heightList_orginal.copy()
    else:
        # Reset variables
        xList = []
        heightList = []

        # Creating all the random numbers
        for i in range(listLength):
            heightList.append(randint(10, maxHeight))
            xList.append(spacing + w*i)
        heightList_orginal = heightList.copy()

    # Start sort
    # animate_fadein()

    # Start timing
    runTime = time.time()

    # Algorithm
    for i in range(listLength-1, -1, -1):
        for j in range(i):
            draw()  # Draw fundamental bars first
         
            if swap:
                rect_draw(green, xList[j], maxHeight + titleHeight-heightList[j], w, heightList[j])
                swap = False
            else: rect_draw(red, xList[j], maxHeight + titleHeight-heightList[j], w, heightList[j])
             
            update_draw()

            if heightList[j] > heightList[j+1]:
                heightList[j], heightList[j+1]=heightList[j+1], heightList[j]
                swap = True

                numOfSwaps += 1

            # Play sound
            Note(heightList[j]*5+400).play(1)

            if btn_click(): return True

    # Sort ended
    # Get total runTime
    runTime = time.time() - runTime
    sort_done = True
   
    draw()
    update_draw()
     
    if btn_click(): return True

    # Print sorted list to console
    print(heightList)
    print("Swaps: {}".format(numOfSwaps))
    print(runTime)

    # Save to history
    addHistory("bubblesort", length, speed, runTime, numOfSwaps)

    # Ending animation
    # green going up
    for i in range(listLength):
        draw()
        rect_draw(green, xList[i], maxHeight + titleHeight-heightList[i], w, heightList[i])     
        # Play sound
        Note(heightList[i]*5+400).play(1)
        
        update_draw()
        if btn_click(): return True

    # green going down
    for i in range(listLength-1, -1, -1):
        draw()
        rect_draw(green, xList[i], maxHeight + titleHeight-heightList[i], w, heightList[i])     
        # Play sound
        Note(heightList[i]*5+400).play(1)
        
        update_draw()
        if btn_click(): return True

    # Drawn replay_btn
    draw()
    window.blit(replay_btn, (791, 454))
    update_draw()

    while True:
        action = click_action(True)
        if action == 'back' or action == 'end': return True

def pause():
    global runTime, isPause
    
    if isPause:
        isPause = False
        runTime = time.time() - runTime
    else:
        isPause = True
        runTime = time.time() - runTime