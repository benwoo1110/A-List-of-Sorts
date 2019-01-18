import pygame
from random import randint

# Initializing the window
pygame.init()
size = (1000, 500)
window = pygame.display.set_mode((size))
pygame.display.set_caption("Bubble-Sort Visualization")
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Declaring Variables
heightList = []
listLength = 50
swap = False

# coordinate for drawing
xList, y, w = [], 0, size[0]/listLength

# Creating all the random numbers
for i in range(listLength):
    heightList.append(randint(0, 500))
    xList.append(w*i)

# Displaying bars on the window


def draw():
    global xList, y, heightList
    window.fill(black)
    for i in range(listLength):
        pygame.draw.rect(
            window, white, (xList[i], 500-heightList[i], w, heightList[i]), 0)


def buffer():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


def update_draw():
    pygame.display.update()
    pygame.time.Clock().tick(100000)

# Algorithm


def mergesort(heightList):
    n = len(heightList)
    n = int(n)
    if (n <= 1):
        return heightList
    m = int(n//2)
    first = heightList[:m]
    second = heightList[m:]
    # print('---------')
    # print(first, second)
    mergesort(first)
    mergesort(second)

    i, j, k = 0, 0, 0

    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            heightList[k] = first[i]
            i += 1
        else:
            heightList[k] = second[j]
            j += 1

        k += 1

        draw()
        update_draw()
        buffer()
        # print('1')

    while i < len(first):
        heightList[k] = first[i]
        i += 1
        k += 1

        draw()
        update_draw()
        buffer()
        # print('2')

    while j < len(second):
        heightList[k] = second[j]
        j += 1
        k += 1

        draw()
        update_draw()
        buffer()
        # print('3')


mergesort(heightList)

# Sort ended

# Show results
print(heightList)

# Ended
while True:
    buffer()
