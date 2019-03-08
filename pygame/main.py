import pygame
import os
import time
from dataclasses import dataclass

from bubblesort import bubblesort_run
from quicksort import quicksort_run
from mergesort import mergesort_run
from insertionsort import insertionsort_run
from bogosort import bogosort_run
from radixsort import radixsort_run

from history import getLastRun
from history import history_run

from information import information_run

# Initialization
pygame.init()
pygame.font.init()
window_size = (1000, 995)
screen = pygame.display.set_mode((1000, 700))
window = pygame.surface.Surface((window_size))
pygame.display.set_caption("A list of Sort")
scroll_y = 0
helpPage_drawn = False

# Colour sets
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
background_colour = pygame.Color(245, 138, 7)
config_colour = pygame.Color(67, 67, 67)
title_colour = pygame.Color(40, 40, 40)

# Font set
# title_font = pygame.font.SysFont('Helvetica Neue Bold', 85)
config_font = pygame.font.SysFont('Helvetica Neue Bold', 46)


@dataclass
class sort(object):
    name: str
    frame: tuple
    sort_btn: pygame.Surface
    config_btn: pygame.Surface
    more_btn: pygame.Surface
    last_run: str
    speed: str


def scroll(event):
    global scroll_y, helpPage_drawn

    # No scrolling in help page
    if helpPage_drawn:
        screen.blit(window, (0, scroll_y))
        update_draw()

    else:
        # Scrollbar
        scrollbar_image = pygame.image.load('scrollbar_image.png').convert()
        isScrolling = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                scroll_y = min(scroll_y + 35, 0)
            if event.button == 5:
                scroll_y = max(scroll_y - 35, -295)

            if event.button == 4 or event.button == 5:
                scrollbar_image.set_alpha(170)

        screen.blit(window, (0, scroll_y))
        screen.blit(scrollbar_image,
                    (window_size[0]-25, -int(scroll_y*(476/295))))
        update_draw()

        return scroll_y


def update_draw():
    pygame.display.flip()
    pygame.display.update()
    pygame.time.Clock().tick(1000000000)


def buffer():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        scroll(event)


# Title bar
title_height = 80
spacing = 30
mainscreen_image = pygame.image.load('mainscreen_image.png').convert()

# The 6 sorting boxes
sortingBoxes_size_w, sortingBoxes_size_h = (
    window_size[0]-(3*spacing))/2, (window_size[1]-title_height-(4*spacing))/3

bubblesort = sort(
    name='bubblesort',
    frame=(spacing, title_height+spacing),
    sort_btn=pygame.image.load('bubblesort_btn.png'),
    config_btn=pygame.image.load('bubblesortConfig_btn.png'),
    more_btn=pygame.image.load('bubblesortMore_btn.png'),
    last_run='--',
    speed='Slow')

quicksort = sort(
    name='quicksort',
    frame=(window_size[0]-spacing-sortingBoxes_size_w, title_height+spacing),
    sort_btn=pygame.image.load('quicksort_btn.png'),
    config_btn=pygame.image.load('quicksortConfig_btn.png'),
    more_btn=pygame.image.load('quicksortMore_btn.png'),
    last_run='--',
    speed='Fast')

mergesort = sort(
    name='mergesort',
    frame=(spacing, title_height+spacing*2+sortingBoxes_size_h),
    sort_btn=pygame.image.load('mergesort_btn.png'),
    config_btn=pygame.image.load('mergesortConfig_btn.png'),
    more_btn=pygame.image.load('mergesortMore_btn.png'),
    last_run='--',
    speed='Fast')

insertionsort = sort(
    name='insertionsort',
    frame=(window_size[0]-spacing-sortingBoxes_size_w,
           title_height+spacing*2+sortingBoxes_size_h),
    sort_btn=pygame.image.load('insertionsort_btn.png'),
    config_btn=pygame.image.load('insertionsortConfig_btn.png'),
    more_btn=pygame.image.load('insertionsortMore_btn.png'),
    last_run='--',
    speed='Moderate')

bogosort = sort(
    name='bogosort',
    frame=(spacing, title_height+spacing*3+sortingBoxes_size_h*2),
    sort_btn=pygame.image.load('bogosort_btn.png'),
    config_btn=pygame.image.load('bogosortConfig_btn.png'),
    more_btn=pygame.image.load('bogosortMore_btn.png'),
    last_run='--',
    speed='Very Slow')

radixsort = sort(
    name='radixsort',
    frame=(window_size[0]-spacing-sortingBoxes_size_w,
           title_height+spacing*3+sortingBoxes_size_h*2),
    sort_btn=pygame.image.load('radixsort_btn.png'),
    config_btn=pygame.image.load('radixsortConfig_btn.png'),
    more_btn=pygame.image.load('radixsortMore_btn.png'),
    last_run='--',
    speed='Moderate')

helpsort = sort(
    name='mergesort',
    frame=(spacing, 405),
    sort_btn=pygame.image.load('helpmergesort_btn.png'),
    config_btn=pygame.image.load('helpmergesortConfig_btn.png'),
    more_btn=pygame.image.load('helpmergesortMore_btn.png'),
    last_run='--',
    speed='Fast')

# options button
optionUnselected_btn = pygame.image.load('optionUnselected_btn.png')
optionSelected_btn = pygame.image.load('optionSelected_btn.png')
optionShown_btn = pygame.image.load('optionShown_btn.png')
optionBackground_image = pygame.image.load(
    'optionBackground_image.png').convert()
optionBackground_image.set_alpha(78)

allhistorySelected_btn = pygame.image.load('allhistorySelected_btn.png')
helpSelected_btn = pygame.image.load('helpSelected_btn.png')
creditsSelected_btn = pygame.image.load('creditsSelected_btn.png')

# more button
moreUnselected_btn = pygame.image.load('moreUnselected_btn.png')
moreSelected_btn = pygame.image.load('moreSelected_btn.png')

historySelected_btn = pygame.image.load('historySelected_btn.png')
infoSelected_btn = pygame.image.load('infoSelected_btn.png')

# Run button
runUnselected_btn = pygame.image.load('runUnselected_btn.png')
runSelected_btn = pygame.image.load('runSelected_btn.png')

# Help page
helpscreen_image = pygame.image.load('helpscreen_image.png')
helpmergesort_btn = pygame.image.load('helpmergesort_btn.png')

# Credits page
credits_image = pygame.image.load('credits_image.png')
backSelected_btn = pygame.image.load('backSelected_btn.png')
backUnselected_btn = pygame.image.load('backUnselected_btn.png')

# Sorting config
runBtn_x, runBtn_y, runBtn_w, runBtn_h = 305, 195, 150, 75
moreBtn_x, moreBtn_y, moreBtn_w, moreBtn_h = 373, 38, 47, 47

optionBtn_x, optionBtn_y, optionBtn_w, optionBtn_h = 905, 17, 65, 65
optionFrame_x, optionFrame_y, optionFrame_w, optionFrame_h = 660, 96, 310, 252
allhistoryBtn_x, allhistoryBtn_y, allhistoryBtn_w, allhistoryBtn_h = 676, 114, 275, 60
helpBtn_x, helpBtn_y, helpBtn_w, helpBtn_h = 678, 192, 275, 60
creditsBtn_x, creditsBtn_y, creditsBtn_w, creditsBtn_h = 676, 267, 275, 60

speedText_x, speedText_y, speedText_w, speedText_h = 142, 109, 145, 39
listlengthText_x, listlengthText_y, listlengthText_w, listlengthText_h = 213, 153, 75, 39

moreFrame_x, moreFrame_y, moreFrame_w, moreFrame_h = 73, 47, 310, 175
infoBtn_x, infoBtn_y, infoBtn_w, infoBtn_h = 90, 66, 275, 60
historyBtn_x, historyBtn_y, historyBtn_w, historyBtn_h = 90, 143, 275, 60

lastRun_x, lastRun_y, lastRun_w, lastRun_h = 181, 134, 183, 39
sortSpeed_x, sortSpeed_y, sortSpeed_w, sortSpeed_h = 145, 171, 216, 39

backBtn_x, backBtn_y, backBtn_w, backBtn_h = 48, 28, 42, 42

speed = float(1.0)
listlength = 10


def showSort(sort):
    frame = sort.frame
    # Draw box
    window.blit(sort.sort_btn, frame)
    # Draw last run
    lastRun_text = config_font.render(sort.last_run, True, config_colour)
    window.blit(lastRun_text, (frame[0]+lastRun_x, frame[1]+lastRun_y))


def showOption():
    global scroll_y

    optionSelected_drawn = False
    mousePos = pygame.mouse.get_pos()

    # If in frame
    while optionBtn_x+optionBtn_w > mousePos[0] > optionBtn_x and optionBtn_y+optionBtn_h+scroll_y > mousePos[1] > optionBtn_y+scroll_y:
        if not optionSelected_drawn:
            window.blit(optionSelected_btn, (optionBtn_x-10, 0))
            optionSelected_drawn = True

        for event in pygame.event.get():
            # Check for left click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    optionSelected_drawn = False
                    optionSelection()
                    setup()

            scroll(event)

        mousePos = pygame.mouse.get_pos()

    if optionSelected_drawn:
        window.blit(optionUnselected_btn, (optionBtn_x-10, 0))
        optionSelected_drawn = False


def optionSelection():
    # Show options
    screen.blit(optionBackground_image, (0, 0))
    screen.blit(optionShown_btn, (0, scroll_y))
    update_draw()

    allhistorySelected_drawn = False
    helpSelected_drawn = False
    creditsSelected_drawn = False

    mousePos = pygame.mouse.get_pos()

    while True:
        clicked = False

        for event in pygame.event.get():

            # Check for mouse button click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
                else:
                    clicked = False
            else:
                clicked = False

            # Cursor on All History
            if allhistoryBtn_x+allhistoryBtn_w > mousePos[0] > allhistoryBtn_x and allhistoryBtn_y+allhistoryBtn_h+scroll_y > mousePos[1] > allhistoryBtn_y+scroll_y:
                if not allhistorySelected_drawn:
                    screen.blit(allhistorySelected_btn,
                                (optionFrame_x, optionFrame_y+scroll_y))
                    update_draw()
                    allhistorySelected_drawn = True
                # Open history page
                if clicked:
                    history_run('everything')
                    scroll(event)
                    screen.blit(optionBackground_image, (0, 0))
                    screen.blit(optionShown_btn, (0, scroll_y))
                    update_draw()
            else:
                if allhistorySelected_drawn:
                    screen.blit(optionShown_btn, (0, scroll_y))
                    update_draw()
                    allhistorySelected_drawn = False

            # Cursor on Help
            if helpBtn_x+helpBtn_w > mousePos[0] > helpBtn_x and helpBtn_y+helpBtn_h+scroll_y > mousePos[1] > helpBtn_y+scroll_y:
                if not helpSelected_drawn:
                    screen.blit(helpSelected_btn,
                                (optionFrame_x, optionFrame_y+scroll_y))
                    update_draw()
                    helpSelected_drawn = True
                # Open help page
                if clicked:
                    help_run()  # Add help page here
                    return True
            else:
                if helpSelected_drawn:
                    screen.blit(optionShown_btn, (0, scroll_y))
                    update_draw()
                    helpSelected_drawn = False

            # Cursor on Credit
            if creditsBtn_x+creditsBtn_w > mousePos[0] > creditsBtn_x and creditsBtn_y+creditsBtn_h+scroll_y > mousePos[1] > creditsBtn_y+scroll_y:
                if not creditsSelected_drawn:
                    screen.blit(creditsSelected_btn,
                                (optionFrame_x, optionFrame_y+scroll_y))
                    update_draw()
                    creditsSelected_drawn = True
                # Open credits page
                if clicked:
                    credits_run()
                    scroll(event)
                    screen.blit(optionBackground_image, (0, 0))
                    screen.blit(optionShown_btn, (0, scroll_y))
                    update_draw()
            else:
                if creditsSelected_drawn:
                    screen.blit(optionShown_btn, (0, scroll_y))
                    update_draw()
                    creditsSelected_drawn = False

            if not(optionFrame_x+optionFrame_w > mousePos[0] > optionFrame_x and optionFrame_y+optionFrame_h+scroll_y > mousePos[1] > optionFrame_y+scroll_y):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return True

            mousePos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()

                


def showConfig(sort):
    global scroll_y
    frame = sort.frame
    # Show image
    window.blit(sort.config_btn, frame)
    # Show config
    speedConfig_text = config_font.render(
        str(round(speed, 1)) + ' x', True, config_colour)
    listlengthConfig_text = config_font.render(
        str(listlength), True, config_colour)
    window.blit(speedConfig_text, (frame[0]+speedText_x, frame[1]+speedText_y))
    window.blit(listlengthConfig_text,
                (frame[0]+listlengthText_x, frame[1]+listlengthText_y))


def moreSelection(sort):
    global scroll_y, helpPage_drawn
    frame = sort.frame
    mousePos = pygame.mouse.get_pos()

    infoSelected_drawn = False
    historySelected_drawn = False

    # Drawn the moreSelection page
    if helpPage_drawn:
        setup()
        window.blit(optionBackground_image, (0, 0))
    window.blit(sort.more_btn, frame)

    # While cursor in box
    while frame[0]+sortingBoxes_size_w > mousePos[0] > frame[0] and frame[1]+sortingBoxes_size_h+scroll_y > mousePos[1] > frame[1]+scroll_y:
        clicked = False

        for event in pygame.event.get():
            # Check for left click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
                else:
                    clicked = False
            else:
                clicked = False

            # Cursor over info_btn
            if frame[0]+infoBtn_x+infoBtn_w > mousePos[0] > frame[0]+infoBtn_x and frame[1]+infoBtn_y+infoBtn_h+scroll_y > mousePos[1] > frame[1]+infoBtn_y+scroll_y:
                if not infoSelected_drawn:
                    window.blit(infoSelected_btn,
                                (frame[0]+moreFrame_x, frame[1]+moreFrame_y))
                    infoSelected_drawn = True
                # Open infomation page
                if clicked:
                    information_run(sort.name)
            else:
                if infoSelected_drawn:
                    window.blit(sort.more_btn, frame)
                    infoSelected_drawn = False

            # Cursor over history_btn
            if frame[0]+historyBtn_x+historyBtn_w > mousePos[0] > frame[0]+historyBtn_x and frame[1]+historyBtn_y+historyBtn_h+scroll_y > mousePos[1] > frame[1]+historyBtn_y+scroll_y:
                if not historySelected_drawn:
                    window.blit(historySelected_btn,
                                (frame[0]+moreFrame_x, frame[1]+moreFrame_y))
                    historySelected_drawn = True
                # Open history page
                if clicked:
                    history_run(sort.name)
            else:
                if historySelected_drawn:
                    window.blit(sort.more_btn, frame)
                    historySelected_drawn = False

            # If click out of moreFrame
            if not(frame[0]+moreFrame_x+moreFrame_w > mousePos[0] > frame[0]+moreFrame_x and frame[1]+moreFrame_y+moreFrame_h+scroll_y > mousePos[1] > frame[1]+moreFrame_y+scroll_y) and clicked:
                # Show back config page
                if helpPage_drawn:
                    setup()
                    window.blit(optionBackground_image, (0, 0))
                showConfig(sort)
                return True
            scroll(event)

        mousePos = pygame.mouse.get_pos()

def sortSelection(sort):
    global scroll_y, speed, listlength, helpPage_drawn

    frame = sort.frame
    mousePos = pygame.mouse.get_pos()

    sortConfig_drawn = False
    clicked = False
    runSelected_drawn = False
    moreSelected_drawn = False

    # Cursor in frame of the box
    while frame[0]+sortingBoxes_size_w > mousePos[0] > frame[0] and frame[1]+sortingBoxes_size_h+scroll_y > mousePos[1] > frame[1]+scroll_y:
        # Change to sorConfig_btn
        if not sortConfig_drawn:
            if helpPage_drawn:
                setup()
                window.blit(optionBackground_image, (0, 0))
            showConfig(sort)
            sortConfig_drawn = True

        # Mouse click in stepper
        clicked = False
        for event in pygame.event.get():
            # Check for left click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
                else:
                    clicked = False
            else:
                clicked = False

            # Stepper for speed
            # click "-"
            if 0.3 < speed:  # 0.2 is min number
                if frame[0]+speedText_x+speedText_w+50 > mousePos[0] > frame[0]+speedText_x+speedText_w and frame[1]+speedText_y+speedText_h+scroll_y > mousePos[1] > frame[1]+speedText_y+scroll_y:
                    if clicked:
                        speed -= 0.1
                        showConfig(sort)
            # click "+"
            if speed < 9.9:  # 10.0 is max number
                if frame[0]+speedText_x+speedText_w+100 > mousePos[0] > frame[0]+speedText_x+speedText_w+50 and frame[1]+speedText_y+speedText_h+scroll_y > mousePos[1] > frame[1]+speedText_y+scroll_y:
                    if clicked:
                        speed += 0.1
                        showConfig(sort)

            # Stepper for listlength
            # click "-"
            if 1 < listlength:  # 0 is min number
                if frame[0]+listlengthText_x+listlengthText_w+50 > mousePos[0] > frame[0]+listlengthText_x+listlengthText_w and frame[1]+listlengthText_y+speedText_h+scroll_y > mousePos[1] > frame[1]+listlengthText_y+scroll_y:
                    if clicked:
                        listlength -= 1
                        showConfig(sort)
            # click "+"
            if listlength < 100:  # 100 is max number
                if frame[0]+listlengthText_x+listlengthText_w+100 > mousePos[0] > frame[0]+listlengthText_x+listlengthText_w+50 and frame[1]+listlengthText_y+speedText_h+scroll_y > mousePos[1] > frame[1]+listlengthText_y+scroll_y:
                    if clicked:
                        listlength += 1
                        showConfig(sort)

            scroll(event)

        # Cursor on more_btn
        while frame[0]+moreBtn_x+moreBtn_w > mousePos[0] > frame[0]+moreBtn_x and frame[1]+moreBtn_y+moreBtn_h+scroll_y > mousePos[1] > frame[1]+moreBtn_y+scroll_y:
            # Cursor on more_btn
            if not moreSelected_drawn:
                window.blit(moreSelected_btn,
                            (frame[0]+moreBtn_x-10, frame[1]))
                moreSelected_drawn = True

            # Cursor click more_btn
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        moreSelected_drawn = False
                        moreSelection(sort)  # run sort algorithm

                scroll(event)

            mousePos = pygame.mouse.get_pos()

        # Cursor move out of more_btn
        if moreSelected_drawn:
            window.blit(moreUnselected_btn, (frame[0]+moreBtn_x-10, frame[1]))
            moreSelected_drawn = False

        # Cursor on run_btn
        while frame[0]+runBtn_x+runBtn_w > mousePos[0] > frame[0]+runBtn_x and frame[1]+runBtn_y+runBtn_h+scroll_y > mousePos[1] > frame[1]+runBtn_y+scroll_y:
            # if runSelected_btn not drawn
            if not runSelected_drawn:
                window.blit(runSelected_btn,
                            (frame[0]+runBtn_x, frame[1]+runBtn_y))
                runSelected_drawn = True

            # Cursor click run_btn
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        return True  # run sort algorithm

                scroll(event)

            mousePos = pygame.mouse.get_pos()

        # Cursor move out of run_btn
        if runSelected_drawn:
            window.blit(runUnselected_btn,
                        (frame[0]+runBtn_x, frame[1]+runBtn_y))
            runSelected_drawn = False

        mousePos = pygame.mouse.get_pos()

    # Cursor is out of the box, change have to sort_btn
    if sortConfig_drawn:
        if helpPage_drawn:
            setup()
            window.blit(optionBackground_image, (0, 0))
        showSort(sort)


def help_run():
    global helpPage_drawn

    helpPage_drawn = True
    window.blit(optionBackground_image, (0, 0))
    showSort(helpsort)

    while True:
        setup()
        window.blit(optionBackground_image, (0, 0))
        showSort(helpsort)

        if sortSelection(helpsort):
            mergesort_run(speed, listlength, False)
            setup()
            helpPage_drawn = False
            return True

        mousePos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if not(helpsort.frame[0]+sortingBoxes_size_w > mousePos[0] > helpsort.frame[0] and helpsort.frame[1]+sortingBoxes_size_h > mousePos[1] > helpsort.frame[1]):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        setup()
                        helpPage_drawn = False
                        return True  # exit help

            screen.blit(window, (0, scroll_y))
            update_draw()

            if event.type == pygame.QUIT:
                pygame.quit()


def credits_run():
    screen.blit(credits_image, (0,0))
    update_draw()

    backSelected_drawn = False

    while True:
            for event in pygame.event.get():
                mousePos = pygame.mouse.get_pos()

                # If cursor over back_btn
                if backBtn_x+backBtn_w > mousePos[0] > backBtn_x and backBtn_y+backBtn_h > mousePos[1] > backBtn_y:
                    if not backSelected_drawn:
                        screen.blit(backSelected_btn, (0, 0))
                        update_draw()
                        backSelected_drawn = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            return True
                else:
                    if backSelected_drawn:
                        screen.blit(backUnselected_btn, (0, 0))
                        update_draw()
                        backSelected_drawn = False

# Fade in animation (NOT DONE)


def setup():
    global bubblesort, quicksort, mergesort, insertionsort, bogosort, radixsort

    bubblesort.last_run = getLastRun('bubblesort')
    quicksort.last_run = getLastRun('quicksort')
    mergesort.last_run = getLastRun('mergesort')
    insertionsort.last_run = getLastRun('insertionsort')
    bogosort.last_run = getLastRun('bogosort')
    radixsort.last_run = getLastRun('radixsort')
    helpsort.last_run = getLastRun('mergesort')

    # Show mainscreen
    window.blit(mainscreen_image, (0, 0))

    showSort(bubblesort)
    showSort(quicksort)
    showSort(mergesort)
    showSort(insertionsort)
    showSort(bogosort)
    showSort(radixsort)


setup()

# Main loop
while True:
    if sortSelection(bubblesort):
        bubblesort_run(speed, listlength, False)
        setup()

    elif sortSelection(quicksort):
        quicksort_run(speed, listlength, False)
        setup()

    elif sortSelection(mergesort):
        mergesort_run(speed, listlength, False)
        setup()

    elif sortSelection(insertionsort):
        insertionsort_run(speed, listlength, False)
        setup()

    elif sortSelection(bogosort):
        bogosort_run(speed, listlength, False)
        setup()

    elif sortSelection(radixsort):
        radixsort_run(speed, listlength, False)
        setup()

    showOption()

    buffer()
