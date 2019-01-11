import pygame
from random import randint

#Initializing the window
pygame.init()
size = (1000,500)
window = pygame.display.set_mode((size))
pygame.display.set_caption("Bubble-Sort Visualization")
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
 
#Declaring Variables
heightList = []
listLength = 10

#coordinate for drawing
xList,y,w = [],0,size[0]/listLength

#Creating all the random numbers
for i in range(listLength):
    heightList.append(randint(0,500))
    xList.append(w*i)

#Displaying bars on the window
def draw():
    global xList,y,heightList
    for i in range(listLength):
        pygame.draw.rect(window, white, (xList[i],500-heightList[i],w,heightList[i]), 0)
 
#Algorithm
for i in range(listLength-1, 0, -1):         
    for j in range(i):
        window.fill(black)

        if heightList[j] > heightList[j+1]:
            heightList[j], heightList[j+1] = heightList[j+1], heightList[j]

        draw()
        pygame.display.update()
        pygame.time.Clock().tick(10000000000000000)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

#Sort ended
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()