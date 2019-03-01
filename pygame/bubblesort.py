import pygame
from random import randint
import time
from time import sleep
import pyaudio
import math
import sys
import os
import pyaudio
from pygame.mixer import Sound, get_init, pre_init
from array import array

# Declaring Variables
window_size = (1000, 700)

listLength = 0
titleHeight = 128
maxHeight = 390
spacing = 75

numOfSwaps = 0
runTime = 0
swap = False
backSelected_drawn = False

heightList_orginal = []
heightList = []
xList, y, w = [], 0, 0

class Note(Sound):
    def __init__(self, frequency, volume=.1):
        self.frequency = frequency
        Sound.__init__(self, self.build_samples())
        self.set_volume(volume)
    def build_samples(self):
        period = int(round(get_init()[0] / self.frequency))
        samples = array("h", [0] * period)
        amplitude = 2 ** (abs(get_init()[1]) - 1) - 1
        for time in range(period):
            if time < period / 2:
                samples[time] = amplitude
            else:
                samples[time] = -amplitude
        return samples



window = pygame.display.set_mode((window_size))
pre_init(44100, -16, 1, 1024)
pygame.init()

def bubblesort(speed, length, replay):
    global window, heightList_orginal, heightList, xList, w, listLength, titleHeight, maxHeight, spacing, numOfSwaps, runTime, swap, backSelected_drawn, window_size, event

    # Change accordance to length and speed input
    listLength = length
    w = (window_size[0]-spacing*2)//listLength
    spacing = (window_size[0]-w*listLength)//2
    numOfSwaps = 0

    # colours
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    stats_colour = pygame.Color(67, 67, 67)
    background_colour = pygame.Color(245, 138, 7)

    # Font set
    stats_font = pygame.font.SysFont('Helvetica Neue Bold', 50)

    if replay:
        # Get previous heightList
        heightList = heightList_orginal.copy()
    else:
        # Reset variables
        xList = []
        heightList = []

        # Creating all the random numbers
        for i in range(listLength):
            heightList.append(randint(10, maxHeight))
            xList.append(spacing + w*i)
        heightList_orginal = heightList.copy()

    def rect_draw(colour, x, y, w, h):
        global window
        pygame.draw.rect(window, colour, (x, y, w, h), 0)

    def draw():
        global window, xList, y, heightList, listLength, numOfSwaps, backSelected_drawn

        # Draw UI
        bubblesortAlgo_image = pygame.image.load('bubblesortAlgo_image.png')
        window.blit(bubblesortAlgo_image, (0, 0))
        if backSelected_drawn:  # Show BackSelected_btn
            backSelected_btn = pygame.image.load('backSelected_btn.png')
            window.blit(backSelected_btn, (0, 0))

        update_draw()

        # show stats
        timeStats_text = stats_font.render(
            str(round(time.time() - runTime, 3)) + " sec", True, stats_colour)
        swapStats_text = stats_font.render(str(numOfSwaps), True, stats_colour)
        speedStats_text = stats_font.render(
            str(round(speed, 1)) + " x", True, stats_colour)
        listlengthStats_text = stats_font.render(
            str(int(listLength)), True, stats_colour)
        window.blit(timeStats_text, (321, 568))
        window.blit(swapStats_text, (321, 616))
        window.blit(speedStats_text, (729, 568))
        window.blit(listlengthStats_text, (729, 616))

        for i in range(listLength):
            rect_draw(white, xList[i], maxHeight +
                      titleHeight-heightList[i], w, heightList[i])

    def backBtn_click():
        global window, backSelected_drawn, event
        backBtn_x, backBtn_y, backBtn_w, backBtn_h = 48, 28, 42, 42

        for i in range(int(400/speed)):
            mousePos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                # If cursor over back_btn
                if backBtn_x+backBtn_w > mousePos[0] > backBtn_x and backBtn_y+backBtn_h > mousePos[1] > backBtn_y:
                    if not backSelected_drawn:
                        backSelected_btn = pygame.image.load(
                            'backSelected_btn.png')
                        window.blit(backSelected_btn, (0, 0))
                        update_draw()
                        backSelected_drawn = True
                    if event.type == pygame.MOUSEBUTTONDOWN: return True  # check if back_btn clicked
                else:
                    if backSelected_drawn:
                        backUnselected_btn = pygame.image.load(
                            'backUnselected_btn.png')
                        window.blit(backUnselected_btn, (0, 0))
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
        global window

        bubblesortAlgo_image = pygame.image.load(
            'bubblesortAlgo_image.png').convert()

        for i in range(160, 257, 32):
            bubblesortAlgo_image.set_alpha(i)
            window.blit(bubblesortAlgo_image, (0, 0))
            update_draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit()

    # animate_fadein()

    # Start timing
    runTime = time.time()
    # Load time cover
    timeCover_image = pygame.image.load('timeCover_image.png')

    # Algorithm
    for i in range(listLength-1, -1, -1):
        for j in range(i):
            draw()  # Draw fundamental bars first
         
            if swap:
                rect_draw(green, xList[j], maxHeight + \
                          titleHeight-heightList[j], w, heightList[j])
                swap=False
            else:
                rect_draw(red, xList[j], maxHeight + \
                          titleHeight-heightList[j], w, heightList[j])
             
            update_draw()

            if heightList[j] > heightList[j+1]:
                heightList[j], heightList[j+1]=heightList[j+1], heightList[j]
                swap=True

                numOfSwaps += 1
            Note(heightList[j-1]*2+390).play(1) 
            print(heightList[j])
            if backBtn_click(): return True

    # Sort ended
    time_end=time.time()
   
    draw()

    update_draw()
     
    if backBtn_click(): return True

    # Print sorted list to console
    print(heightList)
    print("Swaps: {}".format(numOfSwaps))
    print(time_end - runTime)

    # Ending animation
    # green going up
    for i in range(listLength):
        rect_draw(green, xList[i], maxHeight + \
                  titleHeight-heightList[i], w, heightList[i])
        update_draw()
        if backBtn_click(): return True

    # green going down
    for i in range(listLength-1, -1, -1):
        rect_draw(white, xList[i], maxHeight + \
                  titleHeight-heightList[i], w, heightList[i])
        update_draw()
        if backBtn_click(): return True

    # Coordinates of back && replay btn
    backBtn_x, backBtn_y, backBtn_w, backBtn_h=48, 28, 42, 42
    replayBtn_x, replayBtn_y, replayBtn_w, replayBtn_h=791, 454, 165, 54

    # Drawn replay_btn
    replay_btn=pygame.image.load('replay_btn.png')
    window.blit(replay_btn, (791, 454))
    update_draw()

    while True:
        mousePos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            # If cursor over back_btn
            if backBtn_x+backBtn_w > mousePos[0] > backBtn_x and backBtn_y+backBtn_h > mousePos[1] > backBtn_y:
                if not backSelected_drawn:
                    backSelected_btn=pygame.image.load('backSelected_btn.png')
                    window.blit(backSelected_btn, (0, 0))
                    update_draw()
                    backSelected_drawn=True
                if event.type == pygame.MOUSEBUTTONDOWN: return True  # check if back_btn clicked
            else:
                if backSelected_drawn:
                    backUnselected_btn=pygame.image.load(
                        'backUnselected_btn.png')
                    window.blit(backUnselected_btn, (0, 0))
                    update_draw()
                    backSelected_drawn=False

            if replayBtn_x+replayBtn_w > mousePos[0] > replayBtn_x and replayBtn_y+replayBtn_h > mousePos[1] > replayBtn_y:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    bubblesort(speed, length, True)
                    return True

            if event.type == pygame.QUIT: pygame.quit()
