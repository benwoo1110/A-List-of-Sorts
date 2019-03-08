import pygame
from random import randint
import time
from dataclasses import dataclass

from history import addHistory
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
runSpeed = 1.0

numOfSwaps = 0
runTime = 0
backBtn_click = False
swap = False
backSelected_drawn = False
infoSelected_drawn = False
sort_done = False
isPause = False

heightList_orginal = []
heightList = []
xList, y, w = [], 0, 0

window = pygame.display.set_mode((window_size))

# Colour
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0, 0, 255)
stats_colour = pygame.Color(67, 67, 67)
background_colour = pygame.Color(245, 138, 7)

# Font set
pygame.font.init()
stats_font = pygame.font.SysFont('Helvetica Neue Bold', 50)

# Load images
mergesortAlgo_image = pygame.image.load('mergesortAlgo_image.png')
replay_btn = pygame.image.load('replay_btn.png')
backSelected_btn = pygame.image.load('backSelected_btn.png')
backUnselected_btn = pygame.image.load('backUnselected_btn.png')

sortInfoSelected_btn = pygame.image.load('sortInfoSelected_btn.png')
sortInfoUnselected_btn = pygame.image.load('sortInfoUnselected_btn.png')

# UI coordinates
backBtn_x, backBtn_y, backBtn_w, backBtn_h = 48, 28, 42, 42
replayBtn_x, replayBtn_y, replayBtn_w, replayBtn_h = 791, 454, 165, 54
info_btn = coordinates(x=905, y=17, w=65, h=65)

# Fade in animation
def animate_fadein():
    mainscreen_image = pygame.image.load('mainscreen_image.png').convert()
    mergesortAlgo_image = pygame.image.load('mergesortAlgo_image.png').convert()

    window.blit(mainscreen_image,(0, 0))

    for i in range (160, 257, 32):
        mergesortAlgo_image.set_alpha(i)
        window.blit(mergesortAlgo_image,(0, 0))
        update_draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()

def rect_draw(colour, x, y, w, h):
    pygame.draw.rect(window, colour, (x, y, w, h), 0)

def update_draw():
    pygame.display.update()
    pygame.time.Clock().tick(10000000000)

# Displaying bars on the window
def draw(arrList, start, end):
    global xList, y, heightList, listLength, numOfSwaps, backSelected_drawn, optionSelected_drawn, sort_done
    if backBtn_click: return True

    for i in range(start, end+1):
        # Top title bar
        window.blit(mergesortAlgo_image,(0, 0))
        
        # Draw UI
        window.blit(mergesortAlgo_image,(0, 0))
        if backSelected_drawn: # Show BackSelected_btn
            window.blit(backSelected_btn,(0, 0))

        if infoSelected_drawn: # Show optionSelected_btn
            window.blit(sortInfoSelected_btn, (info_btn.x-10, 0))
        
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

        # Update heightList
        heightList[i] = arrList[i-start]

        for j in range(len(heightList)):
            if j == i: 
                rect_draw(red, xList[j], maxHeight+titleHeight-heightList[j], w, heightList[j])
                Note(heightList[j]*5+400).play(1)
                numOfSwaps += 1
            else: rect_draw(white, xList[j], maxHeight+titleHeight-heightList[j], w, heightList[j])
        
        update_draw()
        btn_click()
        if backBtn_click: return True

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
                information_run('mergesort')
                pause()
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
                mergesort_run(runSpeed, listLength, True)
                return 'end'

        if event.type == pygame.QUIT: pygame.quit()

def btn_click():
    global runSpeed, backBtn_click
    if backBtn_click: return True
    
    for i in range(int(400/runSpeed)):
        mousePos = pygame.mouse.get_pos()

        if click_action(False) == 'back': backBtn_click = True

        time.sleep(0.001)

def mergesort_run(speed, length, replay):
    global heightList_orginal, heightList, xList, w, listLength, titleHeight, maxHeight, spacing, runSpeed, numOfSwaps, runTime, backBtn_click, swap, backSelected_drawn, window_size, event, sort_done

    # Change accordance to length and speed input
    listLength = length
    runSpeed = speed
    w = (window_size[0]-spacing*2)//listLength
    spacing = (window_size[0]-w*listLength)//2
    numOfSwaps = 0
    backBtn_click = False

    if replay: 
        # Get previous heightList
        heightList = heightList_orginal.copy()
        print(heightList_orginal)
    else: 
        # Reset variables
        xList = []
        heightList = []
        
        # Creating all the random numbers
        for i in range(listLength):
            heightList.append(randint(10, maxHeight))
            xList.append(spacing + w*i)
        heightList_orginal = heightList.copy()
        print(heightList_orginal)
    
    # Start sort
    # Start timing
    runTime = time.time()

    # Algorithm
    def mergesort_algo(arrList, start, end):
        global backBtn_click
        if backBtn_click: return True
            
        n = int(len(arrList))
        if (n <= 1):
            return arrList

        m = int(n//2)
        first = arrList[:m]
        second = arrList[m:]
        # print('---------')
        # print(first, second)

        mergesort_algo(first, start, m+start-1)
        mergesort_algo(second, m+start, end)

        heightList_before = heightList.copy()
        # print(heightList_before)

        i, j, k = 0, 0, 0

        while i < len(first) and j < len(second):
            if first[i] < second[j]:
                arrList[k] = first[i]
                i += 1
            else:
                arrList[k] = second[j]
                j += 1

            k += 1

        while i < len(first):
            arrList[k] = first[i]
            i += 1
            k += 1

        while j < len(second):
            arrList[k] = second[j]
            j += 1
            k += 1

        if heightList == arrList:
            return heightList_before

        draw(arrList, start, end)
        if backBtn_click: return True

    # Run sort
    heightList_before = mergesort_algo(heightList, 0, listLength-1)

    # Sort ended
    # Get total runTime
    runTime = time.time() - runTime
    sort_done = True

    # Completed List
    heightList, heightList_After = heightList_before.copy(), heightList.copy()
    draw(heightList_After, 0, listLength-1)
    if backBtn_click: return True

    # Show results
    print(heightList)
    
    # Save to history
    addHistory("mergesort", length, speed, runTime, numOfSwaps)

    # Ending animation
    runSpeed = 400.0
    # green going up
    for i in range(listLength):
        drawPage()
        rect_draw(green, xList[i], maxHeight + titleHeight-heightList[i], w, heightList[i])     
        # Play sound
        Note(heightList[i]*5+400).play(1)
        
        update_draw()
        if btn_click(): return True

    # green going down
    for i in range(listLength-1, -1, -1):
        drawPage()
        rect_draw(green, xList[i], maxHeight + titleHeight-heightList[i], w, heightList[i])     
        # Play sound
        Note(heightList[i]*5+400).play(1)
        
        update_draw()
        if btn_click(): return True

    # Drawn replay_btn
    drawPage()
    window.blit(replay_btn, (791, 454))
    update_draw()

    while True:
        action = click_action(True)
        if action == 'back' or action == 'end': return True
        if action == 'next': 
            drawPage()
            update_draw()


def drawPage():
    # Top title bar
    window.blit(mergesortAlgo_image,(0, 0))

    # Draw UI
    window.blit(mergesortAlgo_image,(0, 0))
    if backSelected_drawn: # Show BackSelected_btn
        window.blit(backSelected_btn,(0, 0))

    if infoSelected_drawn: # Show optionSelected_btn
        window.blit(sortInfoSelected_btn, (info_btn.x-10, 0))

    # show stats
    timeStats_text = stats_font.render(str(round(runTime, 3)) + " sec", True, stats_colour)
    swapStats_text = stats_font.render(str(numOfSwaps), True, stats_colour)
    speedStats_text = stats_font.render(str(round(runSpeed, 1)) + " x", True, stats_colour)
    listlengthStats_text = stats_font.render(str(int(listLength)), True, stats_colour)

    window.blit(timeStats_text, (300, 570))
    window.blit(swapStats_text, (392, 617))
    window.blit(speedStats_text, (739, 570))
    window.blit(listlengthStats_text, (794, 617))

    for j in range(len(heightList)):
        rect_draw(white, xList[j], maxHeight+titleHeight-heightList[j], w, heightList[j])

def pause():
    global runTime, isPause
    
    if isPause:
        isPause = False
        runTime = time.time() - runTime
    else:
        isPause = True
        runTime = time.time() - runTime