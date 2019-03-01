import pygame
from random import shuffle
import time

from history import *

# Declaring Variables
window_size = (1000, 700)

listLength = 0
titleHeight = 128
maxHeight = 390
spacing = 75

numOfSwaps = 0
runTime = 0
backSelected_drawn = False

heightList_orginal = []
heightList = []
xList, y, w = [], 0, 0

window = pygame.display.set_mode((window_size))

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
radixsortAlgo_image = pygame.image.load('radixsortAlgo_image.png')
backSelected_btn = pygame.image.load('backSelected_btn.png')
backUnselected_btn = pygame.image.load('backUnselected_btn.png')
timeCover_image = pygame.image.load('timeCover_image.png')
replay_btn = pygame.image.load('replay_btn.png')

def radixsort(speed, length, replay):
    global heightList_orginal, heightList, xList, w, listLength, titleHeight, maxHeight, spacing, numOfSwaps, runTime, backSelected_drawn, window_size, event

    # Change accordance to length and speed input
    listLength = length
    w = (window_size[0]-spacing*2)//listLength
    spacing = (window_size[0]-w*listLength)//2
    numOfSwaps = 0

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
            heightList.append((i+1) * maxHeight // length)
            xList.append(spacing + w*i)
        shuffle(heightList)
        heightList_orginal = heightList.copy()
        print(heightList_orginal)

    def rect_draw(colour, x, y, w, h):
        pygame.draw.rect(window, colour, (x, y, w, h), 0)

    def draw():
        global xList, y, heightList, listLength, numOfSwaps
        
        # Draw UI
        window.blit(radixsortAlgo_image,(0, 0))
        if backSelected_drawn: # Show BackSelected_btn
            window.blit(backSelected_btn,(0, 0))

        update_draw()

        # show stats
        timeStats_text = stats_font.render(str(round(time.time() - runTime, 3)) + " sec", True, stats_colour)
        swapStats_text = stats_font.render(str(numOfSwaps), True, stats_colour)
        speedStats_text = stats_font.render(str(round(speed, 1)) + " x", True, stats_colour)
        listlengthStats_text = stats_font.render(str(int(listLength)), True, stats_colour)
        window.blit(timeStats_text,(321, 568))
        window.blit(swapStats_text,(321, 616))
        window.blit(speedStats_text,(729, 568))
        window.blit(listlengthStats_text,(729, 616))
         

        for i in range(listLength):
            rect_draw(white, xList[i], maxHeight+titleHeight-heightList[i], w, heightList[i])

    def backBtn_click():
        global window, backSelected_drawn, event
        backBtn_x, backBtn_y, backBtn_w, backBtn_h = 48, 28, 42, 42

        for i in range(int(400/speed)):
            mousePos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                # If cursor over back_btn
                if backBtn_x+backBtn_w > mousePos[0] > backBtn_x and backBtn_y+backBtn_h > mousePos[1] > backBtn_y:
                    if not backSelected_drawn: 
                        window.blit(backSelected_btn,(0, 0))
                        update_draw()
                        backSelected_drawn = True                    
                    if event.type == pygame.MOUSEBUTTONDOWN: 
                        if event.button == 1: return True # check if back_btn clicked
                else: 
                    if backSelected_drawn: 
                        window.blit(backUnselected_btn,(0, 0))
                        update_draw()
                        backSelected_drawn = False   
                
                if event.type == pygame.QUIT: pygame.quit()

            time.sleep(0.001)

    def update_draw():
        pygame.display.flip()
        pygame.display.update()
        pygame.time.Clock().tick(10000000000)
        
    # Start sort
    # Fade in animation
    def animate_fadein():
        mainscreen_image = pygame.image.load('mainscreen_image.png').convert()
        radixsortAlgo_image = pygame.image.load('radixsortAlgo_image.png').convert()

        window.blit(mainscreen_image,(0, 0))

        for i in range (128, 257, 32):
            radixsortAlgo_image.set_alpha(i)
            window.blit(radixsortAlgo_image,(0, 0))
            update_draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit()

    # Start timing
    runTime = time.time()

    draw()
    update_draw()
    if backBtn_click(): return True

    # Algorithm
    radixList = [[int(heightList[x]/100), int(heightList[x]%100/10), heightList[x]%10] for x in range(length)]
    for m in range(-1, -4, -1):
        hSort = [[] for x in range(10)]
        rSort = [[] for x in range(10)]
        for c in range(length):
            draw()
            rect_draw(green, xList[c], maxHeight+titleHeight-heightList[c], w, heightList[c])
            update_draw()
            if backBtn_click(): return True
            for i in range(10):
                if radixList[c][m] == i:
                    hSort[i] += [heightList[c]]
                    rSort[i] += [radixList[c]]
        for i in range(9, -1, -1):
            for j in range(len(hSort[i])):
                if hSort[i] != []:
                    numOfSwaps += 1
                    draw()
                    for y in [d for d,x in enumerate(heightList) if x == hSort[i][-1]]:
                        rect_draw(red, xList[y], maxHeight+titleHeight-heightList[y], w, heightList[y])
                    update_draw()
                    if backBtn_click(): return True
                    for t in range(int(400/speed)): time.sleep(0.0005)
                    print(i)
                    print(hSort)
                    heightList.remove(hSort[i][-1])
                    heightList =  [hSort[i][-1]] + heightList
                    hSort[i].remove(hSort[i][-1])
                    radixList.remove(rSort[i][-1])
                    radixList =  [rSort[i][-1]] + radixList
                    rSort[i].remove(rSort[i][-1])
                    draw()
                    rect_draw(red, xList[0], maxHeight+titleHeight-heightList[0], w, heightList[0])
                    update_draw()
                    if backBtn_click(): return True
                    for t in range(int(400/speed)): time.sleep(0.0005)
    draw()
    
    # Sort ended
    runTime = time.time() - runTime

    # Print sorted list to console
    print(heightList)
    print("Swaps: {}".format(numOfSwaps))
    print(runTime)

    # Save to history
    history("radixsort", length, speed, runTime, numOfSwaps)

    # Ending animation
    # green going up
    for i in range(listLength):
        rect_draw(green, xList[i], maxHeight+titleHeight-heightList[i], w, heightList[i])
        update_draw()
        if backBtn_click(): return True

    # green going down
    for i in range(listLength-1, -1, -1):
        rect_draw(white, xList[i], maxHeight+titleHeight-heightList[i], w, heightList[i])
        update_draw()
        if backBtn_click(): return True

    # Coordinates of back && replay btn
    backBtn_x, backBtn_y, backBtn_w, backBtn_h = 48, 28, 42, 42
    replayBtn_x, replayBtn_y, replayBtn_w, replayBtn_h = 791, 454, 165, 54

    # Drawn replay_btn
    window.blit(replay_btn,(791, 454))
    update_draw()

    while True:
        mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            # If cursor over back_btn
            if backBtn_x+backBtn_w > mousePos[0] > backBtn_x and backBtn_y+backBtn_h > mousePos[1] > backBtn_y:
                if not backSelected_drawn: 
                    window.blit(backSelected_btn,(0, 0))
                    update_draw()
                    backSelected_drawn = True                    
                if event.type == pygame.MOUSEBUTTONDOWN: return True # check if back_btn clicked
            else: 
                if backSelected_drawn: 
                    window.blit(backUnselected_btn,(0, 0))
                    update_draw()
                    backSelected_drawn = False   

            if replayBtn_x+replayBtn_w > mousePos[0] > replayBtn_x and replayBtn_y+replayBtn_h > mousePos[1] > replayBtn_y:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    radixsort(speed, length, True)
                    return True

            if event.type == pygame.QUIT: pygame.quit()
