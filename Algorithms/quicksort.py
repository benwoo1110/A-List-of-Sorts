import pygame
from random import randint

#Initializing the window
pygame.init()
size = (500,500)
window = pygame.display.set_mode((size))
pygame.display.set_caption("Pygame Quick-Sort Visualization")
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
 
#Declaring Variables
heightList = []
listLength = 100
isSorted = False
sortedCount = 0
trackInt = 0

#coordinate for drawing
xList,y,w = [],0,5
tmpX = 0

#Creating all the random numbers
for i in range(listLength):
    heightList.append(randint(0,500))
    xList.append(tmpX)
    tmpX += w

#Actually Displaying the window
def draw(color):
    global xList,y,heightList
    for i in range(listLength):
        pygame.draw.rect(window,color,(xList[i],max(heightList) - heightList[i],w,heightList[i]),0)
 

# Algorithm
# While true is needed for the screen to stay there
while True:
    window.fill(black)

    #the point needs to reset, hence:
    if trackInt == listLength-1:
        trackInt = 0

    # #Condition once everything is done
    # if sortedCount > listLength and isSorted == False:
    #     #sorted count will go to or listlength 
    #     print("Sorted!")
    #     print(heightList)
    #     isSorted = True
    
    # if heightList[trackInt] > heightList[trackInt+1] and isSorted == False:
    #     tmp = heightList[trackInt+1]
    #     heightList[trackInt+1],heightList[trackInt] = heightList[trackInt],tmp
    #     sortedCount = 0
    #     trackInt += 1

    # else:
    #     sortedCount += 1
    #     trackInt += 1


	# choose pivot_
	# 2-way partition_
	


        draw(white)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
