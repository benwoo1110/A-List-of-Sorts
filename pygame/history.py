data = []
lines = 0

# Open for Read
historyFile_I = open("history.txt", "r")

# Number of data
lines = int(historyFile_I.readline().strip(' '))
data = [''] * (lines)

for i in range(0, lines):
    data[i] = str(historyFile_I.readline())

# Close
historyFile_I.close()

def addHistory(sortType, listLength, runSpeed, runTime, numOfSwaps):
    global data, lines
    # Open for Write
    historyFile_O = open("history.txt", "w")

    # Add new data
    lines += 1
    data.insert(0, str(sortType) + ' ' + str(listLength) + ' ' +  str(round(runSpeed, 1)) + ' ' +  str(round(runTime, 3)) + ' ' +  str(numOfSwaps) + '\n')
    
    historyFile_O.write(str(lines) + '\n')
    historyFile_O.writelines(data)

    # Close
    historyFile_O.close()

def getLastRun(sort_type):
    global data
    for run in data:
        sort = run.rstrip().split(' ')
        if sort[0] == sort_type: return str(sort[3]) + " sec"
    return "--"



# Pygame history page
import pygame
from dataclasses import dataclass

import bubblesort
import quicksort
import mergesort
import insertionsort
import bogosort
import radixsort

@dataclass
class coordinates(object):
    x : int
    y : int
    w : int
    h : int

# UI coordinates
historyTitle = coordinates(x=0, y=0, w=1000, h=124)
sortHistory = coordinates(x=0, y=124, w=1000, h=89)
backBtn = coordinates(x=48, y=28, w=42, h=42)
timeTaken = coordinates(x=483, y=32, w=161, h=37)
numOfSwaps = coordinates(x=759, y=32, w=133, h=37)

totalHistory = coordinates(x=99, y=99, w=50, h=32)
averageSwaps = coordinates(x=917, y=99, w=133, h=32)
averageTime = coordinates(x=614, y=99, w=109, h=32)
mostRan = coordinates(x=284, y=99, w=138, h=32)

more_btn = coordinates(x=905, y=18, w=50, h=50)

historyDetail_Frame = coordinates(x=273, y=223, w=445, h=270)
timeTaken_historyDetail = coordinates(x=471, y=313, w=149, h=40)
swaps_historyDetail = coordinates(x=415, y=349, w=277, h=40)
speed_historyDetail = coordinates(x=412, y=386, w=280, h=40)
listlength_historyDetail = coordinates(x=473, y=425, w=203, h=40)
run_btn = coordinates(x=593, y=416, w=115, h=54)

# Initialization
screen_size = (1000, 700)
window_size = (1000, historyTitle.h+lines*sortHistory.w)
screen = pygame.display.set_mode((screen_size))
window = pygame.surface.Surface((window_size))
pygame.display.set_caption("A list of Sort")
scroll_y = 0
totalSwaps = 0
totalTime = 0
backSelected_drawn = False
backBtn_click = False
moreBtn_Ys = []
shownData = []

# Colour sets
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
background_colour = pygame.Color(245, 138, 7)
overallStats_colour = pygame.Color(51, 51, 51)
historyStats_colour = pygame.Color(67, 67, 67)
title_colour = pygame.Color(40, 40, 40)

# Font set
pygame.init()
pygame.font.init()
overallStats_font = pygame.font.SysFont('Helvetica Neue Bold', 32)
historyStats_font = pygame.font.SysFont('Helvetica Neue Bold', 40)
historyDetailStats_font = pygame.font.SysFont('Helvetica Neue Bold', 43)

# UI elements
historyTitle_image = pygame.image.load('historyTitle_image.png')
historyBackground_image = pygame.image.load('historyBackground_image.png')

bubblesortHistory_image = pygame.image.load('bubblesortHistory_image.png')
quicksortHistory_image = pygame.image.load('quicksortHistory_image.png')
mergesortHistory_image = pygame.image.load('mergesortHistory_image.png')
insertionsortHistory_image = pygame.image.load('insertionsortHistory_image.png')
bogosortHistory_image = pygame.image.load('bogosortHistory_image.png')
radixsortHistory_image = pygame.image.load('radixsortHistory_image.png')

backSelected_btn = pygame.image.load('backSelected_btn.png')
backUnselected_btn = pygame.image.load('backUnselected_btn.png')
scrollbar_image = pygame.image.load('scrollbar_image.png')

historyMoreSelected_btn = pygame.image.load('historyMoreSelected_btn.png')
historyMoreUnselected_btn = pygame.image.load('historyMoreUnselected_btn.png')

bubblesortHistoryDetail_image = pygame.image.load('bubblesortHistoryDetail_image.png')
quicksortHistoryDetail_image = pygame.image.load('quicksortHistoryDetail_image.png')
mergesortHistoryDetail_image = pygame.image.load('mergesortHistoryDetail_image.png')
insertionsortHistoryDetail_image = pygame.image.load('insertionsortHistoryDetail_image.png')
bogosortHistoryDetail_image = pygame.image.load('bogosortHistoryDetail_image.png')
radixsortHistoryDetail_image = pygame.image.load('radixsortHistoryDetail_image.png')

runUnselected_btn = pygame.image.load('runUnselected_btn.png')
runSelected_btn = pygame.image.load('runSelected_btn.png')

optionBackground_image = pygame.image.load('optionBackground_image.png').convert()
optionBackground_image.set_alpha(78)

# Set default bg image
window.blit(historyBackground_image, (historyTitle.x, historyTitle.y))

def scroll(event):
    global scroll_y, backBtn_click, backSelected_drawn, lines, totalSwaps, totalTime
    
    # Scrollbar
    isScrolling = False

    # When more history than window can display uses scrolling
    if historyTitle.h+sortHistory.h*lines > screen_size[1]:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4: scroll_y = min(scroll_y + 35, 0) # Scrolling up
            if event.button == 5: scroll_y = max(scroll_y - 35, screen_size[1] - (historyTitle.h+sortHistory.h*lines) ) # Scrolling down
    
    screen.blit(historyBackground_image, (historyTitle.x, historyTitle.y))
    screen.blit(window, (0, scroll_y))
    screen.blit(historyTitle_image, (historyTitle.x, historyTitle.y))

    totalHistory_text = overallStats_font.render(str(lines), True, overallStats_colour)
    mostRan_text = overallStats_font.render('Bubble sort', True, overallStats_colour)
    averageTime_text = overallStats_font.render(str(round(totalTime/lines, 3)) + ' sec', True, overallStats_colour)
    averageSwaps_text = overallStats_font.render(str(int(totalSwaps/lines)), True, overallStats_colour)

    screen.blit(totalHistory_text, (totalHistory.x, totalHistory.y))
    screen.blit(mostRan_text, (mostRan.x, mostRan.y))
    screen.blit(averageTime_text, (averageTime.x, averageTime.y))
    screen.blit(averageSwaps_text, (averageSwaps.x, averageSwaps.y))
    
    # Checking back button
    mousePos = pygame.mouse.get_pos()

    # If cursor over back_btn
    if backBtn.x+backBtn.w > mousePos[0] > backBtn.x and backBtn.y+backBtn.h > mousePos[1] > backBtn.y:
        screen.blit(backSelected_btn,(0, 0))
        # check if back_btn clicked
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if event.button == 1:
                backBtn_click = True
                return True

    update_draw()

    return scroll_y

def update_draw():
    pygame.display.flip()
    pygame.display.update()
    pygame.time.Clock().tick(1000000000)

def buffer():
    for event in pygame.event.get():        
        if event.type == pygame.QUIT: pygame.quit()
        scroll(event)

def drawBox(history_image, time, swaps, i):
    window.blit(history_image, (sortHistory.x, historyTitle.h+sortHistory.h*i))
    timeTaken_text = historyStats_font.render(time + ' sec', True, historyStats_colour)
    numOfSwaps_text = historyStats_font.render(swaps, True, historyStats_colour)
    window.blit(timeTaken_text, (timeTaken.x, (historyTitle.h+sortHistory.h*i) + timeTaken.y))
    window.blit(numOfSwaps_text, (numOfSwaps.x, (historyTitle.h+sortHistory.h*i) + numOfSwaps.y))

def historyDetail(sort):
     # darken background
    screen.blit(optionBackground_image, (historyTitle.x, historyTitle.y))

    # History Detail image
    if sort[0] == 'bubblesort': screen.blit(bubblesortHistoryDetail_image, (historyTitle.x, historyTitle.y))
    elif sort[0] == 'quicksort': screen.blit(quicksortHistoryDetail_image, (historyTitle.x, historyTitle.y))
    elif sort[0] == 'mergesort': screen.blit(mergesortHistoryDetail_image, (historyTitle.x, historyTitle.y))
    elif sort[0] == 'insertionsort': screen.blit(insertionsortHistoryDetail_image, (historyTitle.x, historyTitle.y))
    elif sort[0] == 'bogosort': screen.blit(bogosortHistoryDetail_image, (historyTitle.x, historyTitle.y))
    elif sort[0] == 'radixsort': screen.blit(radixsortHistoryDetail_image, (historyTitle.x, historyTitle.y))

    # Detailed stats for sort
    timeTaken_text = historyDetailStats_font.render(sort[3] + ' sec', True, historyStats_colour)
    numOfSwaps_text = historyDetailStats_font.render(sort[4], True, historyStats_colour)
    speed_text = historyDetailStats_font.render(sort[2] + ' x', True, historyStats_colour)
    listLength_text = historyDetailStats_font.render(sort[1], True, historyStats_colour)

    screen.blit(timeTaken_text, (timeTaken_historyDetail.x, timeTaken_historyDetail.y))
    screen.blit(numOfSwaps_text, (swaps_historyDetail.x, swaps_historyDetail.y))
    screen.blit(speed_text, (speed_historyDetail.x, speed_historyDetail.y))
    screen.blit(listLength_text, (listlength_historyDetail.x, listlength_historyDetail.y))

    update_draw()

    clicked = False
    runSelected_drawn = False
    while True:
        for event in pygame.event.get():  
            mousePos = pygame.mouse.get_pos() 

            # Check for left click
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if event.button == 1: clicked = True
                else: clicked = False
            else: clicked = False
            
            # When cursor on run button
            if run_btn.x+run_btn.w > mousePos[0] > run_btn.x and run_btn.y+run_btn.h > mousePos[1] > run_btn.y:
                if not runSelected_drawn:
                    screen.blit(runSelected_btn, (run_btn.x-16, run_btn.y-6))
                    runSelected_drawn = True
                    update_draw()
                if clicked:
                    if sort[0] == 'bubblesort': bubblesort.bubblesort_run(float(sort[2]), int(sort[1]), False)
                    elif sort[0] == 'quicksort': quicksort.quicksort_run(float(sort[2]), int(sort[1]), False)
                    elif sort[0] == 'mergesort': mergesort.mergesort_run(float(sort[2]), int(sort[1]), False)
                    elif sort[0] == 'insertionsort': insertionsort.insertionsort_run(float(sort[2]), int(sort[1]), False)
                    elif sort[0] == 'bogosort': bogosort.bogosort_run(float(sort[2]), int(sort[1]), False)
                    elif sort[0] == 'radixsort': radixsort.radixsort_run(float(sort[2]), int(sort[1]), False)
                    return True
                    
            else:
                if runSelected_drawn:
                    screen.blit(runUnselected_btn, (run_btn.x-16, run_btn.y-6))
                    runSelected_drawn = False
                    update_draw()

            # Closing the page by clicking outside of historyDetail frame
            if not(historyDetail_Frame.x+historyDetail_Frame.w > mousePos[0] > historyDetail_Frame.x and historyDetail_Frame.y+historyDetail_Frame.h > mousePos[1] > historyDetail_Frame.y) and clicked:
                return True

            if event.type == pygame.QUIT: pygame.quit()

def history_run(sort_type):
    global backBtn_click, lines, data, scroll_y, totalSwaps, totalTime, moreBtn_Ys, shownData

    # Reset varibles
    backBtn_click = False
    lines = 0
    totalSwaps = 0
    totalTime = 0
    scroll_y = 0
    moreBtn_Ys = []
    shownData = []
    window.fill(background_colour)
    window.blit(historyBackground_image, (historyTitle.x, historyTitle.y))

    # Setup view
    for run in data:
        sort = run.rstrip().split(' ')
        # For specific sort type
        if sort_type != 'everything':
            if sort[0] == sort_type: 
                if sort_type == 'bubblesort': drawBox(bubblesortHistory_image, sort[3], sort[4], lines)
                elif sort_type == 'quicksort': drawBox(quicksortHistory_image, sort[3], sort[4], lines)
                elif sort_type == 'mergesort': drawBox(mergesortHistory_image, sort[3], sort[4], lines)
                elif sort_type == 'insertionsort': drawBox(insertionsortHistory_image, sort[3], sort[4], lines)
                elif sort_type == 'bogosort': drawBox(bogosortHistory_image, sort[3], sort[4], lines)
                elif sort_type == 'radixsort': drawBox(radixsortHistory_image, sort[3], sort[4], lines)
                # Update stats
                shownData.append(sort)
                print(historyTitle.h+sortHistory.h*lines + more_btn.y)
                moreBtn_Ys.append(historyTitle.h+sortHistory.h*lines + more_btn.y)
                totalSwaps += int(sort[4])
                totalTime += float(sort[3])
                lines += 1
                
        # For all sort history
        else: 
            if sort[0] == 'bubblesort': drawBox(bubblesortHistory_image, sort[3], sort[4], lines)
            elif sort[0] == 'quicksort': drawBox(quicksortHistory_image, sort[3], sort[4], lines)
            elif sort[0] == 'mergesort': drawBox(mergesortHistory_image, sort[3], sort[4], lines)
            elif sort[0] == 'insertionsort': drawBox(insertionsortHistory_image, sort[3], sort[4], lines)
            elif sort[0] == 'bogosort': drawBox(bogosortHistory_image, sort[3], sort[4], lines)
            elif sort[0] == 'radixsort': drawBox(radixsortHistory_image, sort[3], sort[4], lines)
            # Update stats
            shownData.append(sort)
            moreBtn_Ys.append(historyTitle.h+sortHistory.h*lines + more_btn.y)
            totalSwaps += int(sort[4])
            totalTime += float(sort[3])
            lines += 1

    update_draw()

    moreSelected_drawn = False
    moreSelectedDrawn_y = 0
    while True:
        for event in pygame.event.get():  
            mousePos = pygame.mouse.get_pos()  

            if more_btn.x+more_btn.w > mousePos[0] > more_btn.x:
                for y in moreBtn_Ys:
                    if y+more_btn.h > mousePos[1]-scroll_y > y:
                        # drawn historyMoreSelected_btn
                        if not moreSelected_drawn:
                            window.blit(historyMoreSelected_btn, (more_btn.x, y))
                            moreSelectedDrawn_y = y
                            moreSelected_drawn = True
                        # If more button clicked
                        if event.type == pygame.MOUSEBUTTONDOWN: 
                            if event.button == 1: historyDetail(shownData[moreBtn_Ys.index(y)])
                        break
                    # return back to unselected image when cursor not in y axis of more_btns
                    else: 
                        if moreSelected_drawn: 
                            window.blit(historyMoreUnselected_btn, (more_btn.x, moreSelectedDrawn_y))
                            moreSelected_drawn = False
    
            # return back to unselected image when cursor not in x axis of more_btns
            else: 
                if moreSelected_drawn: 
                    window.blit(historyMoreUnselected_btn, (more_btn.x, moreSelectedDrawn_y))
                    moreSelected_drawn = False
            
            if event.type == pygame.QUIT: pygame.quit()
            scroll(event)
            if backBtn_click: return True # Go back