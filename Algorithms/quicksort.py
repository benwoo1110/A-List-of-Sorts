import pygame
from random import randint

#Initializing the window
pygame.init()
size = (1500,500)
window = pygame.display.set_mode((size))
pygame.display.set_caption("Quick-Sort Visualization")
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
# Algorithm
# While true is needed for the screen to stay there
while True:
	# choose pivot_
	# 2-way partition_
	


        draw(white)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
