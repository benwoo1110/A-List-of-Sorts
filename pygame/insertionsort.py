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

numOfSwaps = 0
runTime = 0

heightList_orginal = []
heightList = []
xList, y, w = [], 0, 0

def insertionsort(speed, length, replay):
    global heightList_orginal, heightList, xList, w, listLength, titleHeight, maxHeight, spacing, numOfSwaps, runTime, window_size, event
    
    # Initialization
    pygame.init()
    pygame.font.init()
    window = pygame.display.set_mode((window_size))

    # Change accordance to length and speed input
    listLength = length
    w = (window_size[0]-spacing*2)//listLength
    spacing = (window_size[0]-w*listLength)//2
    numOfSwaps = 0

    # colours
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)
    stats_colour = pygame.Color(67, 67, 67)
    background_colour = pygame.Color(245, 138, 7)

    # Font set
    stats_font = pygame.font.SysFont('Helvetica Neue Bold', 50)

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

    def draw():
        global xList, y, heightList, listLength, numOfSwaps
        
        # Draw UI
        insertionsortAlgo_image = pygame.image.load('insertionsortAlgo_image.png')
        window.blit(insertionsortAlgo_image,(0, 0))
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
        global event
        backBtn_x, backBtn_y, backBtn_w, backBtn_h = 48, 28, 42, 42

        for i in range(int(400/speed)):
            mousePos = pygame.mouse.get_pos()
        
            for event in pygame.event.get():
                # check if back btn clicked
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if backBtn_x+backBtn_w > mousePos[0] > backBtn_x and backBtn_y+backBtn_h > mousePos[1] > backBtn_y:
                        return True
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
        insertionsortAlgo_image = pygame.image.load('insertionsortAlgo_image.png').convert()

        window.blit(mainscreen_image,(0, 0))

        for i in range (160, 257, 32):
            insertionsortAlgo_image.set_alpha(i)
            window.blit(insertionsortAlgo_image,(0, 0))
            update_draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit()

    # Start timing
    runTime = time.time()
    # Load time cover 
    timeCover_image = pygame.image.load('timeCover_image.png')

    draw()
    update_draw()
    if backBtn_click(): return True

    # Algorithm
    for c in range(1, listLength): #Green
        for s in range(c, 0, -1):
            if heightList[s] < heightList[s-1]:
                # Before Swap
                draw()
                rect_draw(blue, xList[c], maxHeight+titleHeight-heightList[c], w, heightList[c])
                rect_draw(green, xList[s], maxHeight+titleHeight-heightList[s], w, heightList[s])
                rect_draw(red, xList[s-1], maxHeight+titleHeight-heightList[s-1], w, heightList[s-1])
                update_draw()
                heightList[s], heightList[s-1] = heightList[s-1], heightList[s]
                if backBtn_click(): return True
                
                # After swap
                draw()
                rect_draw(blue, xList[c], maxHeight+titleHeight-heightList[c], w, heightList[c])
                rect_draw(red, xList[s], maxHeight+titleHeight-heightList[s], w, heightList[s])
                rect_draw(green, xList[s-1], maxHeight+titleHeight-heightList[s-1], w, heightList[s-1])
                update_draw()
                numOfSwaps +=1
                if backBtn_click(): return True

            else: break
    draw()
    
    # Sort ended
    runTime = time.time() - runTime

    # Print sorted list to console
    print(heightList)
    print("Swaps: {}".format(numOfSwaps))
    print(runTime)

    # Save to history
    history("insertionsort", length, speed, runTime, numOfSwaps)

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
    replay_btn = pygame.image.load('replay_btn.png')
    window.blit(replay_btn,(791, 454))
    update_draw()

    while True:
        mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN: 
                # if cusor click in back_btn
                if backBtn_x+backBtn_w > mousePos[0] > backBtn_x and backBtn_y+backBtn_h > mousePos[1] > backBtn_y:
                    return True
                if replayBtn_x+replayBtn_w > mousePos[0] > replayBtn_x and replayBtn_y+replayBtn_h > mousePos[1] > replayBtn_y:
                    insertionsort(speed, length, True)
                    return True
            if event.type == pygame.QUIT: pygame.quit()
