import pygame
from random import randint

#Initializing the window
pygame.init()
size = (1500,500)
window = pygame.display.set_mode((size))
pygame.display.set_caption("Bubble-Sort Visualization")
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
 
#Declaring Variables
heightList = []
listLength = 10
swap = False

#coordinate for drawing
xList,y,w = [],0,size[0]/listLength

#Creating all the random numbers
for i in range(listLength):
    heightList.append(randint(0,500))
    xList.append(w*i)

#Displaying bars on the window
def draw():
    global xList,y,heightList
    window.fill(black)
    for i in range(listLength):
        pygame.draw.rect(window, white, (xList[i],500-heightList[i],w,heightList[i]), 0)
    
def buffer():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

def update_draw(): 
    pygame.display.update()
    pygame.time.Clock().tick(10)
 
#Algorithm
for i in range(listLength-1, 0, -1):         
    for j in range(i):
        draw()
        update_draw()
        
        if swap:
            pygame.draw.rect(window, green, (xList[j],500-heightList[j],w,heightList[j]), 0)
            swap = False
        else: 
            pygame.draw.rect(window, red, (xList[j],500-heightList[j],w,heightList[j]), 0)
        
        update_draw()

        if heightList[j] > heightList[j+1]:
            heightList[j], heightList[j+1] = heightList[j+1], heightList[j] 
            swap = True
        
        buffer()

#Sort ended

#Ending animation
#green going up
for i in range(listLength):
    pygame.draw.rect(window, green, (xList[i],500-heightList[i],w,heightList[i]), 0)
    update_draw()

    buffer()
#green going down
for i in range(listLength-1, -1, -1):
    pygame.draw.rect(window, white, (xList[i],500-heightList[i],w,heightList[i]), 0)
    update_draw()

    buffer()

#Print sorted list to console
print(heightList)

#Ended
while True:
    buffer()