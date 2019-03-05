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

def removeHistory():
    global data
    # Open for Write
    historyFile_O = open("history.txt", "w")
    # Add new data
    historyFile_O.write(str(len(data)) + '\n')
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
deleteAll_btn = coordinates(x=905, y=17, w=65, h=65)

historyDetail_Frame = coordinates(x=273, y=223, w=445, h=270)
timeTaken_historyDetail = coordinates(x=471, y=313, w=149, h=40)
swaps_historyDetail = coordinates(x=415, y=349, w=277, h=40)
speed_historyDetail = coordinates(x=412, y=386, w=280, h=40)
listlength_historyDetail = coordinates(x=473, y=425, w=203, h=40)
run_btn = coordinates(x=593, y=416, w=115, h=54)
delete_btn = coordinates(x=648, y=249, w=47, h=47)

historyDeleteConfirm_Frame = coordinates(x=338, y=251, w=325, h=198)
deleteConfirmYes_btn = coordinates(x=517, y=376, w=113, h=51)
deleteConfirmNo_btn = coordinates(x=369, y=376, w=113, h=51)

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

historyDeleteAllSelected_btn = pygame.image.load('historyDeleteAllSelected_btn.png')
historyDeleteAllUnselected_btn = pygame.image.load('historyDeleteAllUnselected_btn.png')

historyDeleteAllConfirm_btn = pygame.image.load('historyDeleteAllConfirm_btn.png')
historyDeleteAllNoSelected_btn = pygame.image.load('historyDeleteAllNoSelected_btn.png')
historyDeleteAllYesSelected_btn = pygame.image.load('historyDeleteAllYesSelected_btn.png')

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
historyDeleteSelected_btn = pygame.image.load('historyDeleteSelected_btn.png')
historyDeleteUnselected_btn = pygame.image.load('historyDeleteUnselected_btn.png')

scrollbar_image = pygame.image.load('scrollbar_image.png')

optionBackground_image = pygame.image.load('optionBackground_image.png').convert()
optionBackground_image.set_alpha(78)

# Set default bg image
window.blit(historyBackground_image, (historyTitle.x, historyTitle.y))

def scroll(event):
    global scroll_y, backBtn_click, backSelected_drawn, lines, totalSwaps, totalTime

    pageHeight = historyTitle.h+sortHistory.h*lines
    show_scrollbar = False

    # When more history than window can display uses scrolling
    if pageHeight > screen_size[1]:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4: scroll_y = min(scroll_y + 35, 0) # Scrolling up
            if event.button == 5: scroll_y = max(scroll_y - 35, screen_size[1] - pageHeight) # Scrolling down
        
        # Show scroll bar when scrolling required
        show_scrollbar = True
        

    screen.blit(historyBackground_image, (historyTitle.x, historyTitle.y))
    screen.blit(window, (0, scroll_y))
    screen.blit(historyTitle_image, (historyTitle.x, historyTitle.y))
    if show_scrollbar: screen.blit(scrollbar_image, (window_size[0]-25, -int(scroll_y*((screen_size[1]-224)/(pageHeight-screen_size[1])))))

    if lines != 0:
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

def drawhistoryDetail(sort):
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

def historyDetail(sort, sort_type):
    global backBtn_click, data

    # draw history detail page
    drawhistoryDetail(sort)

    clicked = False
    runSelected_drawn = False
    deleteSelected_drawn = False

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
                    
                    # update any new sort history after run
                    setupView(sort_type)
                    
                    # Re-drawn history & historyDetail page
                    scroll(event)
                    drawhistoryDetail(sort)
                    backBtn_click = False # Back button is clicked for sort page not history page
                    
            else:
                if runSelected_drawn:
                    screen.blit(runUnselected_btn, (run_btn.x-16, run_btn.y-6))
                    runSelected_drawn = False
                    update_draw()
            
            # When cursor on delete button
            if delete_btn.x+delete_btn.w > mousePos[0] > delete_btn.x and delete_btn.y+delete_btn.h > mousePos[1] > delete_btn.y:
                if not deleteSelected_drawn:
                    screen.blit(historyDeleteSelected_btn, (delete_btn.x-17, delete_btn.y-16))
                    deleteSelected_drawn = True
                    update_draw()
                if clicked: 
                    data.pop(data.index('{} {} {} {} {}\n'.format(sort[0],sort[1],sort[2],sort[3],sort[4])))
                    removeHistory()
                    # update any new sort history after run
                    setupView(sort_type)
                    return True
                    
            else:
                if deleteSelected_drawn:
                    screen.blit(historyDeleteUnselected_btn, (delete_btn.x-17, delete_btn.y-16))
                    deleteSelected_drawn = False
                    update_draw()

            # Closing the page by clicking outside of historyDetail frame
            if not(historyDetail_Frame.x+historyDetail_Frame.w > mousePos[0] > historyDetail_Frame.x and historyDetail_Frame.y+historyDetail_Frame.h > mousePos[1] > historyDetail_Frame.y) and clicked:
                return True

            if event.type == pygame.QUIT: pygame.quit()

def setupView(sort_type):
    global backBtn_click, lines, data, totalSwaps, totalTime, moreBtn_Ys, shownData

    # Reset varibles
    backBtn_click = False
    lines = 0
    totalSwaps = 0
    totalTime = 0
    moreBtn_Ys = []
    shownData = []

    # Setup view
    window.blit(historyBackground_image, (historyTitle.x, historyTitle.y))
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
                # print(historyTitle.h+sortHistory.h*lines + more_btn.y)
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

    # Set up view
    setupView(sort_type)

    clicked = False
    moreSelected_drawn = False
    deleteAllSelected_drawn = False
    moreSelectedDrawn_y = 0

    while True:
        for event in pygame.event.get():  
            # Check for left click
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if event.button == 1: clicked = True
                else: clicked = False
            else: clicked = False

            mousePos = pygame.mouse.get_pos()  
            
            # More Btn
            if more_btn.x+more_btn.w > mousePos[0] > more_btn.x:
                for y in moreBtn_Ys:
                    if y+more_btn.h > mousePos[1]-scroll_y > y:
                        # drawn historyMoreSelected_btn
                        if not moreSelected_drawn:
                            window.blit(historyMoreSelected_btn, (more_btn.x, y))
                            moreSelectedDrawn_y = y
                            moreSelected_drawn = True
                        # If more button clicked
                        if clicked: historyDetail(shownData[moreBtn_Ys.index(y)], sort_type)
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

            # deleteAll button
            while deleteAll_btn.x+deleteAll_btn.w > mousePos[0] > deleteAll_btn.x and deleteAll_btn.y+deleteAll_btn.h > mousePos[1] > deleteAll_btn.y:
                if not deleteAllSelected_drawn:
                    screen.blit(historyDeleteAllSelected_btn, (deleteAll_btn.x-10, 0))
                    update_draw()
                    deleteAllSelected_drawn = True
                
                for event in pygame.event.get():
                    # If deleteAll button clicked
                    if event.type == pygame.MOUSEBUTTONDOWN: 
                        if event.button == 1: 
                            if historyDeleteConfirm(): 
                                data = []
                                removeHistory()
                                return True

                    if event.type == pygame.QUIT: pygame.quit()
                
                mousePos = pygame.mouse.get_pos()

            # return back to unselected image when cursor not in x axis of more_btns
            deleteAllSelected_drawn = False
            
            # Buffer stuff
            if event.type == pygame.QUIT: pygame.quit()
            scroll(event)
            if backBtn_click: return True # Go back

def historyDeleteConfirm():
    screen.blit(optionBackground_image, (0,0))
    screen.blit(historyDeleteAllConfirm_btn, (0,0))
    update_draw()

    clicked = False
    deleteConfirmNoSelected_drawn = False
    deleteConfirmYesSelected_drawn = False

    while True:
        for event in pygame.event.get():
            # Check for left click
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if event.button == 1: clicked = True
                else: clicked = False
            else: clicked = False

            mousePos = pygame.mouse.get_pos()  

            # Cursor on No btn
            if deleteConfirmNo_btn.x+deleteConfirmNo_btn.w > mousePos[0] > deleteConfirmNo_btn.x and deleteConfirmNo_btn.y+deleteConfirmNo_btn.h > mousePos[1] > deleteConfirmNo_btn.y:
                if not deleteConfirmNoSelected_drawn:
                    screen.blit(historyDeleteAllNoSelected_btn, (0,0))
                    update_draw()
                    deleteConfirmNoSelected_drawn = True
                if clicked: return False # DO NOT REMOVE HISTORY
            else:
                if deleteConfirmNoSelected_drawn:
                    screen.blit(historyDeleteAllConfirm_btn, (0,0))
                    update_draw()
                    deleteConfirmNoSelected_drawn = False

            # Cursor on Yes btn
            if deleteConfirmYes_btn.x+deleteConfirmYes_btn.w > mousePos[0] > deleteConfirmYes_btn.x and deleteConfirmYes_btn.y+deleteConfirmYes_btn.h > mousePos[1] > deleteConfirmYes_btn.y:
                if not deleteConfirmYesSelected_drawn:
                    screen.blit(historyDeleteAllYesSelected_btn, (0,0))
                    update_draw()
                    deleteConfirmYesSelected_drawn = True
                if clicked: return True # removes all history
            else:
                if deleteConfirmYesSelected_drawn:
                    screen.blit(historyDeleteAllConfirm_btn, (0,0))
                    update_draw()
                    deleteConfirmYesSelected_drawn = False

            # Cursor Click outside of historyDeleteConfirm Frame
            if not(historyDeleteConfirm_Frame.x+historyDeleteConfirm_Frame.w > mousePos[0] > historyDeleteConfirm_Frame.x and historyDeleteConfirm_Frame.y+historyDeleteConfirm_Frame.h > mousePos[1] > historyDeleteConfirm_Frame.y) and clicked:
                return False # DO NOT REMOVE HISTORY
                
            if event.type == pygame.QUIT: pygame.quit()

