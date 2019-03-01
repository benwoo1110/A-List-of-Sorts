import pygame
from random import randint
import time

from history import *

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
timeCover_image = pygame.image.load('timeCover_image.png')

def mergesort(speed, length, replay):
    global heightList_orginal, heightList, xList, w, listLength, titleHeight, maxHeight, spacing, runSpeed, numOfSwaps, runTime, backBtn_click, swap, backSelected_drawn, window_size, event

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

    def rect_draw(colour, x, y, w, h):
        pygame.draw.rect(window, colour, (x, y, w, h), 0)

    # Displaying bars on the window
    def draw(arrList, start, end):
        global xList, y, heightList, listLength, backBtn_click, backSelected_drawn, numOfSwaps, event
        if backBtn_click: return True

        for i in range(start, end+1):
            # Top title bar
            window.blit(mergesortAlgo_image,(0, 0))
            # Show BackSelected_btn
            if backSelected_drawn: 
                window.blit(backSelected_btn,(0, 0))
            
            # show stats
            timeStats_text = stats_font.render(str(round(time.time() - runTime, 3)) + " sec", True, stats_colour)
            swapStats_text = stats_font.render(str(numOfSwaps), True, stats_colour)
            speedStats_text = stats_font.render(str(round(speed, 1)) + " x", True, stats_colour)
            listlengthStats_text = stats_font.render(str(int(listLength)), True, stats_colour)
            window.blit(timeStats_text,(321, 568))
            window.blit(swapStats_text,(321, 616))
            window.blit(speedStats_text,(729, 568))
            window.blit(listlengthStats_text,(729, 616))

            # Update heightList
            heightList[i] = arrList[i-start]

            for j in range(len(heightList)):
                if j == i: rect_draw(red, xList[j], maxHeight+titleHeight-heightList[j], w, heightList[j])
                else: rect_draw(white, xList[j], maxHeight+titleHeight-heightList[j], w, heightList[j])
            
            update_draw()
            buffer()
            if backBtn_click: return True

    def buffer():
        global runSpeed, backBtn_click, backSelected_drawn, event
        if backBtn_click: return True

        backBtn_x, backBtn_y, backBtn_w, backBtn_h = 48, 28, 42, 42
        
        for i in range(int(400/runSpeed)):
            mousePos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                # If cursor over back_btn
                if backBtn_x+backBtn_w > mousePos[0] > backBtn_x and backBtn_y+backBtn_h > mousePos[1] > backBtn_y:
                    if not backSelected_drawn: 
                        window.blit(backSelected_btn,(0, 0))
                        update_draw()
                        backSelected_drawn = True                    
                    if event.type == pygame.MOUSEBUTTONDOWN: 
                        if event.button == 1:
                            backBtn_click = True
                            return True # check if back_btn clicked
                else: 
                    if backSelected_drawn: 
                        window.blit(backUnselected_btn,(0, 0))
                        update_draw()
                        backSelected_drawn = False   
                
                if event.type == pygame.QUIT: pygame.quit()

            time.sleep(0.001)

    def update_draw():
        pygame.display.update()
        pygame.time.Clock().tick(10000000000)

    
    # Start sort
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
    # Completed List
    heightList, heightList_After = heightList_before.copy(), heightList.copy()
    draw(heightList_After, 0, listLength-1)
    if backBtn_click: return True

    # Show results
    print(heightList)

    # Total runtime
    runTime = time.time() - runTime
    
    # Save to history
    history("mergesort", length, speed, runTime, numOfSwaps)

    # green going up
    for i in range(listLength):
        rect_draw(green, xList[i], maxHeight+titleHeight-heightList[i], w, heightList[i])
        update_draw()
        buffer()
        if backBtn_click: return True

    # green going down
    for i in range(listLength-1, -1, -1):
        rect_draw(white, xList[i], maxHeight+titleHeight-heightList[i], w, heightList[i])
        update_draw()
        buffer()
        if backBtn_click: return True

    # Coordinates of back && replay btn
    backBtn_x, backBtn_y, backBtn_w, backBtn_h = 48, 28, 42, 42
    replayBtn_x, replayBtn_y, replayBtn_w, replayBtn_h = 791, 454, 165, 54

    # Drawn replay_btn
    window.blit(replay_btn,(791, 454))
    update_draw()

    while True:
        mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():

              # if cusor click in back_btn
            if backBtn_x+backBtn_w > mousePos[0] > backBtn_x and backBtn_y+backBtn_h > mousePos[1] > backBtn_y:
                if not backSelected_drawn: 
                    window.blit(backSelected_btn,(0, 0))
                    update_draw()
                    backSelected_drawn = True                    
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if event.button == 1:
                        backBtn_click = True
                        return True # check if back_btn clicked
            else: 
                if backSelected_drawn: 
                    window.blit(backUnselected_btn,(0, 0))
                    update_draw()
                    backSelected_drawn = False

            # Replay btn pressed
            if replayBtn_x+replayBtn_w > mousePos[0] > replayBtn_x and replayBtn_y+replayBtn_h > mousePos[1] > replayBtn_y:
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    mergesort(speed, length, True)
                    return True
            if event.type == pygame.QUIT: pygame.quit()