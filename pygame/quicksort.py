import pygame
from random import randint
import time

from history import addHistory

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
quicksortAlgo_image = pygame.image.load('quicksortAlgo_image.png')
replay_btn = pygame.image.load('replay_btn.png')
backSelected_btn = pygame.image.load('backSelected_btn.png')
backUnselected_btn = pygame.image.load('backUnselected_btn.png')
timeCover_image = pygame.image.load('timeCover_image.png')

def quicksort_run(speed, length, replay):
    global heightList_orginal, heightList, xList, w, listLength, titleHeight, maxHeight, spacing, runSpeed, numOfSwaps, runTime, swap, backSelected_drawn, backBtn_click, window_size, event

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


    #Displaying bars on the window
    def draw():
        global xList, y, heightList, listLength, numOfSwaps, backBtn_click
        if backBtn_click: return True
        
        # Top title bar
        window.blit(quicksortAlgo_image,(0, 0))
        # Show BackSelected_btn
        if backSelected_drawn: 
            window.blit(backSelected_btn,(0, 0))

        # Update stats
        timeStats_text = stats_font.render(str(round(time.time() - runTime, 3)) + " sec", True, stats_colour)
        swapStats_text = stats_font.render(str(numOfSwaps), True, stats_colour)
        speedStats_text = stats_font.render(str(round(speed, 1)) + " x", True, stats_colour)
        listlengthStats_text = stats_font.render(str(int(listLength)), True, stats_colour)
        
        window.blit(timeStats_text, (300, 570))
        window.blit(swapStats_text, (392, 617))
        window.blit(speedStats_text, (739, 570))
        window.blit(listlengthStats_text, (794, 617))
         
        # Update bars
        for i in range(listLength):
            rect_draw(white, xList[i], maxHeight+titleHeight-heightList[i], w, heightList[i])

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
        global runSpeed, backBtn_click, event
        if backBtn_click: return True

        pygame.display.flip()
        pygame.display.update()
        pygame.time.Clock().tick(10000000000)
    
    # Start sort
    def animate_fadein():
        # Fade in animation
        mainscreen_image = pygame.image.load('mainscreen_image.png').convert()
        quicksortAlgo_image = pygame.image.load('quicksortAlgo_image.png').convert()

        window.blit(mainscreen_image,(0, 0))

        for i in range (160, 257, 32):
            quicksortAlgo_image.set_alpha(i)
            window.blit(quicksortAlgo_image,(0, 0))
            update_draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit()
    
    # Start timing
    runTime = time.time()

    # Algorithm
    def quickSort(heightList):
        global backBtn_click
        if backBtn_click: return True

        quickSortHelper(heightList,0,len(heightList)-1)

    def quickSortHelper(heightList,first,last):
        global backBtn_click
        if backBtn_click: return True

        if first<last:
            #Its going to Partiition
            splitpoint = partition(heightList,first,last)

            #Basically, per iteration you are running it  split into 2. So it does it for the
            #beofre and after the Partition
            quickSortHelper(heightList,first,splitpoint-1)
            quickSortHelper(heightList,splitpoint+1,last)

    def partition(heightList,first,last):
        global backBtn_click, numOfSwaps, event
        if backBtn_click: return True

        #set a pivot value, in our case at the start
        pivotvalue = heightList[first]
        pivotindex = first

        #ensure that the border when swapping heightListound stuff, is right of the 
        border = first+1
        end = last
        isCompleted = False
        swap = False

        while not isCompleted:

            draw()
            rect_draw(blue, xList[pivotindex], maxHeight+titleHeight-heightList[pivotindex], w, heightList[pivotindex])
            if swap:
                rect_draw(green, xList[border], maxHeight+titleHeight-heightList[border], w, heightList[border])
                rect_draw(green, xList[end], maxHeight+titleHeight-heightList[end], w, heightList[end])
                swap = False

            update_draw()
            buffer()
            if backBtn_click: return True
    

            #Basically this is once everythin is sorted and checks if its more
            while border <= end and heightList[border] <= pivotvalue:
                border = border + 1

            #Same thing as above but opposite and in this cfase its less
            while heightList[end] >= pivotvalue and end >= border:
                end = end -1

            #this is bascially once everything after the border, which in the end gos to the end, is smaller 
            if end < border:
                isCompleted = True

            #if not it swaps 
            else:
                #Before swaps
                rect_draw(red, xList[border], maxHeight+titleHeight-heightList[border], w, heightList[border])
                rect_draw(red, xList[end], maxHeight+titleHeight-heightList[end], w, heightList[end])
                update_draw()
                buffer()
                if backBtn_click: return True
    

                heightList[border], heightList[end] = heightList[end], heightList[border]
                
                #After swaps
                draw()
                rect_draw(blue, xList[pivotindex], maxHeight+titleHeight-heightList[pivotindex], w, heightList[pivotindex])
                rect_draw(green, xList[border], maxHeight+titleHeight-heightList[border], w, heightList[border])
                rect_draw(green, xList[end], maxHeight+titleHeight-heightList[end], w, heightList[end])
                
                numOfSwaps += 1
                update_draw()
                buffer()
                if backBtn_click: return True
    


        #it swaps again
        rect_draw(red, xList[first], maxHeight+titleHeight-heightList[first], w, heightList[first])
        rect_draw(red, xList[end], maxHeight+titleHeight-heightList[end], w, heightList[end])
        
        update_draw() 
        buffer()
        if backBtn_click: return True
    

        heightList[first], heightList[end] = heightList[end], heightList[first]

        draw()
        rect_draw(blue, xList[pivotindex], maxHeight+titleHeight-heightList[pivotindex], w, heightList[pivotindex])
        rect_draw(green, xList[first], maxHeight+titleHeight-heightList[first], w, heightList[first])
        rect_draw(green, xList[end], maxHeight+titleHeight-heightList[end], w, heightList[end])
        
        numOfSwaps += 1
        update_draw()
        buffer()
        if backBtn_click: return True

        return end

    quickSort(heightList)

    #Sort Ended
    #Show results
    print(heightList)

    # Last animation
    draw()
    update_draw()
    buffer()
    if backBtn_click: return True

    runTime = time.time() - runTime

    # Save to history
    addHistory("quicksort", length, speed, runTime, numOfSwaps)
    
    # End animation
    #green going up
    for i in range(0, listLength):
        rect_draw(green, xList[i], maxHeight+titleHeight-heightList[i], w, heightList[i])
        update_draw()
        buffer()
        if backBtn_click: return True
    
    #green going down
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
                    quicksort(speed, length, True)
                    return True
            if event.type == pygame.QUIT: pygame.quit()