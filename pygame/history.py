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
    
    historyFile_O.write(str(int(lines)+1) + '\n')
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

# Colour sets
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
background_colour = pygame.Color(245, 138, 7)
stats_colour = pygame.Color(67, 67, 67)
title_colour = pygame.Color(40, 40, 40)

# Font set
pygame.font.init()
stats_font = pygame.font.SysFont('Helvetica Neue Bold', 40)

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

# UI coordinates
historyTitle_x, historyTitle_y, historyTitle_w, historyTitle_h = 0, 0, 1000, 124
sortHistory_x, sortHistory_y, sortHistory_w, sortHistory_h = 0, 124, 1000, 89
backBtn_x, backBtn_y, backBtn_w, backBtn_h = 48, 28, 42, 42
timeTaken_x, timeTaken_y, timeTaken_w, timeTaken_h = 483, 32, 161, 37
numOfSwaps_x, numOfSwaps_y, numOfSwaps_w, numOfSwaps_h = 759, 32, 133, 37

# Initialization
screen_size = (1000, 700)
window_size = (1000, 124+lines*sortHistory_w)
screen = pygame.display.set_mode((screen_size))
window = pygame.surface.Surface((window_size))
pygame.display.set_caption("A list of Sort")
scroll_y = 0
backSelected_drawn = False
backBtn_click = False

window.blit(historyBackground_image, (historyTitle_x, historyTitle_y))

def scroll(event):
    global scroll_y, backBtn_click, backSelected_drawn, lines
    
    # Scrollbar
    isScrolling = False

    # When more history than window can display uses scrolling
    if historyTitle_h+sortHistory_h*lines > screen_size[1]:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4: scroll_y = min(scroll_y + 35, 0) # Scrolling up
            if event.button == 5: scroll_y = max(scroll_y - 35, screen_size[1]-(historyTitle_h+sortHistory_h*lines)) # Scrolling down
    
    screen.blit(historyBackground_image, (historyTitle_x, historyTitle_y))
    screen.blit(window, (0, scroll_y))
    screen.blit(historyTitle_image, (historyTitle_x, historyTitle_y))

    # Checking back button
    mousePos = pygame.mouse.get_pos()

    # If cursor over back_btn
    if backBtn_x+backBtn_w > mousePos[0] > backBtn_x and backBtn_y+backBtn_h > mousePos[1] > backBtn_y:
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

def drawBox(history_image, timeTaken, numOfSwaps, i):
    window.blit(history_image, (sortHistory_x, historyTitle_h+sortHistory_h*i))
    timeTaken_text = stats_font.render(timeTaken + ' sec', True, stats_colour)
    numOfSwaps_text = stats_font.render(numOfSwaps, True, stats_colour)
    window.blit(timeTaken_text, (timeTaken_x, (historyTitle_h+sortHistory_h*i) + timeTaken_y))
    window.blit(numOfSwaps_text, (numOfSwaps_x, (historyTitle_h+sortHistory_h*i) + numOfSwaps_y))

def history_run(sort_type):
    global backBtn_click, lines, data, scroll_y

    # Reset varibles
    backBtn_click = False
    lines = 0
    scroll_y = 0
    window.fill(background_colour)
    window.blit(historyBackground_image, (historyTitle_x, historyTitle_y))

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
                lines += 1
                
        # For all sort history
        else: 
            if sort[0] == 'bubblesort': drawBox(bubblesortHistory_image, sort[3], sort[4], lines)
            elif sort[0] == 'quicksort': drawBox(quicksortHistory_image, sort[3], sort[4], lines)
            elif sort[0] == 'mergesort': drawBox(mergesortHistory_image, sort[3], sort[4], lines)
            elif sort[0] == 'insertionsort': drawBox(insertionsortHistory_image, sort[3], sort[4], lines)
            elif sort[0] == 'bogosort': drawBox(bogosortHistory_image, sort[3], sort[4], lines)
            elif sort[0] == 'radixsort': drawBox(radixsortHistory_image, sort[3], sort[4], lines)
            lines += 1

    update_draw()

    while True:
        # If back button clicked
        buffer()
        if backBtn_click: return True # Go back