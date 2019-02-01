import pygame
from random import randint

# Initializing the window
pygame.init()
size = (1000, 700)
window = pygame.display.set_mode((size))
pygame.display.set_caption("Quick-Sort Visualization")
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Declaring Variables
heightList = []
listLength = 500
numOfSelections = 0
numOfSwaps = 0

# coordinate for drawing
xList, y, w = [], 0, size[0]/listLength

# Creating all the random numbers
for i in range(listLength):
    heightList.append(randint(0, 400))
    xList.append(w*i)

# Displaying bars on the window



    global xList, y, heightList
def draw():
    global xList, y, heightList
    pygame.draw.rect( window, white, (xList[i], 400-heightList[i], w, heightList[i]), 0)


    pygame.draw.rect( window, white, (xList[i], 400-heightList[i], w, heightList[i]), 0)


def buffer():

def update_draw():
    if event.type == pygame.QUIT:
        pygame.quit()
pygame.time.Clock().tick(100000)
# Algorithm

            heightList[border], heightList[end] = heightList[end], heightList[border]
def quickSort(heightList, first, last):
    if first < last:
                window, green, (xList[border], 400-heightList[border], w, heightList[border]), 0)
        # Its going to Partiition
        splitpoint = partition(heightList, first, last)
                window, green, (xList[end], 400-heightList[end], w, heightList[end]), 0)
        # Basically, per iteration you are running it  split into 2. So it does it for the
        # beofre and after the Partition
        quickSort(heightList, first, splitpoint-1)
        quickSort(heightList, splitpoint+1, last)
    # Show before selection
    pygame.draw.rect(
def partition(heightList, first, last):
    global numOfSelections, numOfSwaps
    update_draw()
    # set a pivot value, in our case at the start
    pivotvalue = heightList[first]
    pivotindex = first

    numOfSelections += 1

    # ensure that the border when swapping heightListound stuff, is right of the
    border = first+1
    end = last
    isCompleted = False
    swap = False

    while not isCompleted:

        draw()
        pygame.draw.rect(
            window, blue, (xList[pivotindex], 400-heightList[pivotindex], w, heightList[pivotindex]), 0)
        if swap:
            pygame.draw.rect(
                window, green, (xList[border], 400-heightList[border], w, heightList[border]), 0)
            pygame.draw.rect(
                window, green, (xList[end], 400-heightList[end], w, heightList[end]), 0)
            swap = False
        update_draw()
        buffer()

        # Basically this is once everythin is sorted and checks if its more
        while border <= end and heightList[border] <= pivotvalue:
            border = border + 1

        # Same thing as above but opposite and in this cfase its less
        while heightList[end] >= pivotvalue and end >= border:
            end = end - 1

        # this is bascially once everything after the border, which in the end gos to the end, is smaller
        if end < border:
            isCompleted = True

        # if not it swaps
        else:
            # Before swaps
            pygame.draw.rect(
                window, red, (xList[border], 400-heightList[border], w, heightList[border]), 0)
            pygame.draw.rect(
                window, red, (xList[end], 400-heightList[end], w, heightList[end]), 0)
            update_draw()
            buffer()

            heightList[border], heightList[end] = heightList[end], heightList[border]

            # After swaps
            draw()
            pygame.draw.rect(
                window, blue, (xList[pivotindex], 400-heightList[pivotindex], w, heightList[pivotindex]), 0)
            pygame.draw.rect(
                window, green, (xList[border], 400-heightList[border], w, heightList[border]), 0)
            pygame.draw.rect(
                window, green, (xList[end], 400-heightList[end], w, heightList[end]), 0)
            update_draw()
            buffer()

            numOfSelections += 2
            numOfSwaps += 1

    # it swaps again
    # Show before selection
    pygame.draw.rect(
        window, red, (xList[first], 400-heightList[first], w, heightList[first]), 0)
    pygame.draw.rect(
        window, red, (xList[end], 400-heightList[end], w, heightList[end]), 0)
    update_draw()
    buffer()

    heightList[first], heightList[end] = heightList[end], heightList[first]

    # Show after change
    draw()
    pygame.draw.rect(
        window, blue, (xList[pivotindex], 400-heightList[pivotindex], w, heightList[pivotindex]), 0)
    pygame.draw.rect(
        window, green, (xList[first], 400-heightList[first], w, heightList[first]), 0)
    pygame.draw.rect(
        window, green, (xList[end], 400-heightList[end], w, heightList[end]), 0)
    update_draw()
    buffer()

    numOfSelections += 2
    numOfSwaps += 1

    return end


quickSort(heightList, 0, listLength-1)

# Sort Ended

# Show results
    draw()
    pygame.draw.rect(
        window, blue, (xList[pivotindex], 400-heightList[pivotindex], w, heightList[pivotindex]), 0)
# End animation
        window, green, (xList[first], 400-heightList[first], w, heightList[first]), 0)
    pygame.draw.rect(
        window, green, (xList[end], 400-heightList[end], w, heightList[end]), 0)
# green going up
    buffer()
    pygame.draw.rect(
        window, green, (xList[i], 400-heightList[i], w, heightList[i]), 0)
    numOfSelections += 2
    numOfSwaps += 1
# green going down
    return end
    pygame.draw.rect(
        window, white, (xList[i], 400-heightList[i], w, heightList[i]), 0)

quickSort(heightList, 0, listLength-1)

# Ended

# Show results
print(heightList)
print("Selections: {}\nSwaps: {}".format(numOfSelections, numOfSwaps))

# End animation
draw()
update_draw()
buffer()
# green going up
for i in range(listLength):
    pygame.draw.rect(
        window, green, (xList[i], 400-heightList[i], w, heightList[i]), 0)
    update_draw()
    buffer()
# green going down
for i in range(listLength-1, -1, -1):
    pygame.draw.rect(
        window, white, (xList[i], 400-heightList[i], w, heightList[i]), 0)
    update_draw()
    buffer()

# Ended
while True:
    buffer()
