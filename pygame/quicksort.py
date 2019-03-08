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
quicksortAlgo_image = pygame.image.load('quicksortAlgo_image.png')
replay_btn = pygame.image.load('replay_btn.png')
backSelected_btn = pygame.image.load('backSelected_btn.png')
backUnselected_btn = pygame.image.load('backUnselected_btn.png')

sortInfoSelected_btn = pygame.image.load('sortInfoSelected_btn.png')
sortInfoUnselected_btn = pygame.image.load('sortInfoUnselected_btn.png')

# UI coordinates
backBtn_x, backBtn_y, backBtn_w, backBtn_h = 48, 28, 42, 42
replayBtn_x, replayBtn_y, replayBtn_w, replayBtn_h = 791, 454, 165, 54
info_btn = coordinates(x=905, y=17, w=65, h=65)

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

def rect_draw(colour, x, y, w, h):
    pygame.draw.rect(window, colour, (x, y, w, h), 0)

def update_draw(): 
    global runSpeed, backBtn_click, event
    if backBtn_click: return True

    pygame.display.flip()
    pygame.display.update()
    pygame.time.Clock().tick(10000000000)

#Displaying bars on the window
def draw():
    global xList, y, heightList, listLength, numOfSwaps, backSelected_drawn, optionSelected_drawn, sort_done
    if backBtn_click: return True
    
    # Top title bar
    window.blit(quicksortAlgo_image,(0, 0))
    # Show BackSelected_btn
    if backSelected_drawn: 
        window.blit(backSelected_btn,(0, 0))

    time_current = runTime
    if not sort_done:
        time_current = time.time() - runTime

    # Update stats
    timeStats_text = stats_font.render(str(round(time_current, 3)) + " sec", True, stats_colour)
    swapStats_text = stats_font.render(str(numOfSwaps), True, stats_colour)
    speedStats_text = stats_font.render(str(round(runSpeed, 1)) + " x", True, stats_colour)
    listlengthStats_text = stats_font.render(str(int(listLength)), True, stats_colour)
    
    window.blit(timeStats_text, (300, 570))
    window.blit(swapStats_text, (392, 617))
    window.blit(speedStats_text, (739, 570))
    window.blit(listlengthStats_text, (794, 617))
        
    # Update bars
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
                information_run('quicksort')
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
                quicksort_run(runSpeed, listLength, True)
                return 'end'

        if event.type == pygame.QUIT: pygame.quit()

def btn_click():
    global runSpeed, backBtn_click, backSelected_drawn, event
    if backBtn_click: return True
    
    for i in range(int(400/runSpeed)):
        mousePos = pygame.mouse.get_pos()

        if click_action(False) == 'back': backBtn_click = True

        time.sleep(0.001)

def quicksort_run(speed, length, replay):
    global heightList_orginal, heightList, xList, w, listLength, titleHeight, maxHeight, spacing, runSpeed, numOfSwaps, runTime, swap, backSelected_drawn, backBtn_click, window_size, event, sort_done

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

                # Play sound
                Note(heightList[border]*5+400).play(1)

            update_draw()
            btn_click()
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
                # Play sound
                Note(heightList[border]*5+400).play(1)

                btn_click()
                if backBtn_click: return True
                

                heightList[border], heightList[end] = heightList[end], heightList[border]
                
                #After swaps
                draw()
                rect_draw(blue, xList[pivotindex], maxHeight+titleHeight-heightList[pivotindex], w, heightList[pivotindex])
                rect_draw(green, xList[border], maxHeight+titleHeight-heightList[border], w, heightList[border])
                rect_draw(green, xList[end], maxHeight+titleHeight-heightList[end], w, heightList[end])
                update_draw()
                # Play sound
                Note(heightList[border]*5+400).play(1)

                btn_click()
                if backBtn_click: return True

                numOfSwaps += 1



        #it swaps again
        rect_draw(red, xList[first], maxHeight+titleHeight-heightList[first], w, heightList[first])
        rect_draw(red, xList[end], maxHeight+titleHeight-heightList[end], w, heightList[end])
        update_draw() 
        # Play sound
        Note(heightList[first]*5+400).play(1)
        
        btn_click()
        if backBtn_click: return True
    

        heightList[first], heightList[end] = heightList[end], heightList[first]

        draw()
        rect_draw(blue, xList[pivotindex], maxHeight+titleHeight-heightList[pivotindex], w, heightList[pivotindex])
        rect_draw(green, xList[first], maxHeight+titleHeight-heightList[first], w, heightList[first])
        rect_draw(green, xList[end], maxHeight+titleHeight-heightList[end], w, heightList[end])
        update_draw()
        # Play sound
        Note(heightList[first]*5+400).play(1)

        btn_click()
        if backBtn_click: return True

        numOfSwaps += 1

        return end

    quickSort(heightList)

    #Sort Ended
    # Get total runTime
    runTime = time.time() - runTime
    sort_done = True

    #Show results
    print(heightList)

    # Last animation
    draw()
    update_draw()
    btn_click()
    if backBtn_click: return True

    # Save to history
    addHistory("quicksort", length, speed, runTime, numOfSwaps)
    
    # Ending animation
    runSpeed = 400.0
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