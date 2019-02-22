import pygame
from random import randint
import time

# Declaring Variables
window_size = (1000, 700)

listLength = 0
titleHeight = 128
maxHeight = 390
spacing = 75

numOfSwaps = 0
runTime = 0
swap = False

heightList = []
xList, y, w = [], 0, 0

def bubblesort(speed, length):
    global heightList, xList, w, listLength, titleHeight, maxHeight, spacing, numOfSwaps, runTime, swap, window_size
    
    # Initialization
    pygame.init()
    pygame.font.init()
    window = pygame.display.set_mode((window_size))

    # Reset variables
    heightList = []
    xList = []
    numOfSelections = 0
    numOfSwaps = 0
    swap = False

    # Change accordance to length and speed input
    listLength = length
    w = (window_size[0]-spacing*2)//listLength
    spacing = (window_size[0]-w*listLength)//2

    # colours
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    stats_colour = pygame.Color(67, 67, 67)

    # Font set
    stats_font = pygame.font.SysFont('Helvetica Neue Bold', 50)

    # Creating all the random numbers
    for i in range(listLength):
        heightList.append(randint(10, maxHeight))
        xList.append(spacing + w*i)

    def rect_draw(colour, x, y, w, h):
        pygame.draw.rect(window, colour, (x, y, w, h), 0)

    def draw():
        global xList, y, heightList, listLength, numOfSwaps
        
        # Top title bar
        bubblesortAlgo_image = pygame.image.load('bubblesortAlgo_image.png')
        window.blit(bubblesortAlgo_image,(0, 0))

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
        backBtn_x, backBtn_y, backBtn_w, backBtn_h = 48, 28, 42, 42
        mousePos = pygame.mouse.get_pos()
        
        # if cusor click in 
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if backBtn_x+backBtn_w > mousePos[0] > backBtn_x and backBtn_y+backBtn_h > mousePos[1] > backBtn_y:
                return True

    def update_draw():
        pygame.display.flip()
        pygame.display.update()
        pygame.time.Clock().tick(10000000000)

    # Start sort
    runTime = time.time()
    # Load time cover 
    timeCover_image = pygame.image.load('timeCover_image.png')

    # Algorithm
    for i in range(listLength-1, -1, -1):
        for j in range(i):
            draw() # Draw fundamental bars first

            if swap:
                rect_draw(green, xList[j], maxHeight+titleHeight-heightList[j], w, heightList[j])
                swap = False
            else: 
                rect_draw(red, xList[j], maxHeight+titleHeight-heightList[j], w, heightList[j])
            
            update_draw()

            if heightList[j] > heightList[j+1]:
                heightList[j], heightList[j+1] = heightList[j+1], heightList[j]
                swap = True

                numOfSwaps += 1

            for i in range(int(400/speed)):
                # check if back btn clicked
                for event in pygame.event.get():
                    if backBtn_click(): return None # End program
                    if event.type == pygame.QUIT: pygame.quit()
    
                time.sleep(0.001)
    
    # Sort ended
    time_end = time.time()

    # Print sorted list to console
    print(heightList)
    print("Swaps: {}".format(numOfSwaps))
    print(time_end - runTime)

    # Ending animation
    # green going up
    for i in range(listLength):
        rect_draw(green, xList[i], maxHeight+titleHeight-heightList[i], w, heightList[i])
        update_draw()
        
        for event in pygame.event.get():
            if backBtn_click(): return None # End program
            if event.type == pygame.QUIT: pygame.quit()

    # green going down
    for i in range(listLength-1, -1, -1):
        rect_draw(white, xList[i], maxHeight+titleHeight-heightList[i], w, heightList[i])
        update_draw()
        
        for event in pygame.event.get():
            if backBtn_click(): return None # End program
            if event.type == pygame.QUIT: pygame.quit()

    while True:
        for event in pygame.event.get():
            if backBtn_click(): return None # End program
            if event.type == pygame.QUIT: pygame.quit()