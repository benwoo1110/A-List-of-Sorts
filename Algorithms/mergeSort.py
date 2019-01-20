import pygame
from random import randint

# Initializing the window
pygame.init()
size = (1500, 500)
window = pygame.display.set_mode((size))
pygame.display.set_caption("Merge sort Visualization")
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Declaring Variables
heightList = []
listLength = 300
swap = False

# coordinate for drawing
xList, y, w = [], 0, size[0]/listLength

# Creating all the random numbers
for i in range(listLength):
    heightList.append(randint(0, 500))
    xList.append(w*i)

# Displaying bars on the window


def draw(arrList, start, end):
    global xList, y, heightList
	
    for i in range(start, end+1):
        # background
        window.fill(black)

        # Update heightList
        heightList[i] = arrList[i-start]
        # print(heightList)

        for i in range(len(heightList)):
            pygame.draw.rect(
                window, white, (xList[i], 500-heightList[i], w, heightList[i]), 0)
        update_draw()
        buffer()


def buffer():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


def update_draw():
    pygame.display.update()
    pygame.time.Clock().tick(100000000)

# Algorithm


def mergesort(arrList, start, end):
    n = int(len(arrList))
    if (n <= 1):
        return arrList

    m = int(n//2)
    first = arrList[:m]
    second = arrList[m:]
    # print('---------')
    # print(first, second)

    mergesort(first, start, m+start-1)
    mergesort(second, m+start, end)

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

    draw(arrList, start, end)

    print(arrList)
    print(heightList)
    print(start, end)


mergesort(heightList, 0, listLength-1)

# Sort ended

# Show results
print(heightList)

# Ended
while True:
    buffer()
