import pygame
from random import randint
import time

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

heightList = []
xList, y, w = [], 0, 0

def mergesort(speed, length):
    global heightList, xList, w, listLength, titleHeight, maxHeight, spacing, runSpeed, numOfSwaps, runTime, backBtn_click, swap, window_size, event
    
    # Initialization
    pygame.init()
    pygame.font.init()
    window = pygame.display.set_mode((window_size))

    # Reset variables
    heightList = []
    xList = []
    numOfSelections = 0
    numOfSwaps = 0
    backBtn_click = False
    swap = False

    # Change accordance to length and speed input
    listLength = length
    runSpeed = speed
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

    # Displaying bars on the window
    def draw(arrList, start, end):
        global xList, y, heightList, listLength, backBtn_click, numOfSwaps, event
        if backBtn_click: return True

        for i in range(start, end+1):
            # Top title bar
            mergesortAlgo_image = pygame.image.load('mergesortAlgo_image.png')
            window.blit(mergesortAlgo_image,(0, 0))
            
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
        global runSpeed, backBtn_click, event
        if backBtn_click: return True

        backBtn_x, backBtn_y, backBtn_w, backBtn_h = 48, 28, 42, 42
        mousePos = pygame.mouse.get_pos()
        
        for i in range(int(400/runSpeed)):
            for event in pygame.event.get():
                # if cusor click in back_btn
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if backBtn_x+backBtn_w > mousePos[0] > backBtn_x and backBtn_y+backBtn_h > mousePos[1] > backBtn_y:
                        backBtn_click = True
                        return True
                if event.type == pygame.QUIT: pygame.quit()
                    
            time.sleep(0.001)
        print(backBtn_click)

    def update_draw():
        pygame.display.update()
        pygame.time.Clock().tick(10000000000)

    # Algorithm
    # Start sort
    runTime = time.time()
    # Load time cover 
    timeCover_image = pygame.image.load('timeCover_image.png')

    def mergesort(arrList, start, end):
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

        mergesort(second, m+start, end)

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
    heightList_before = mergesort(heightList, 0, listLength-1)

    # Sort ended
    if backBtn_click: return True
    # Show results
    print(heightList)

    # Completed Animation
    heightList, heightList_After = heightList_before.copy(), heightList.copy()
    draw(heightList_After, 0, listLength-1)
    if backBtn_click: return True

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


    while True:
       buffer()
       if backBtn_click: return True