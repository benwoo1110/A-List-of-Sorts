import pygame
from random import randint

#Initializing the window
pygame.init()
size = (1000,700)
window = pygame.display.set_mode((size))
pygame.display.set_caption("Quick-Sort Visualization")
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0, 0, 255)
 
#Declaring Variables
heightList = []
listLength = 100

#coordinate for drawing
xList,y,w = [],0,size[0]/listLength

#Creating all the random numbers
for i in range(listLength):
    heightList.append(randint(0,400))
    xList.append(w*i)

#Displaying bars on the window
def draw():
    global xList,y,heightList
    window.fill(black)
    for i in range(listLength):
        pygame.draw.rect(window, white, (xList[i],400-heightList[i],w,heightList[i]), 0)
    
def buffer():
        for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

def update_draw(): 
    pygame.display.update()
    pygame.time.Clock().tick(20)
 
#Algorithm
def quickSort(heightList):
   quickSortHelper(heightList,0,len(heightList)-1)

def quickSortHelper(heightList,first,last):
   if first<last:

       #Its going to Partiition
       splitpoint = partition(heightList,first,last)

       #Basically, per iteration you are running it  split into 2. So it does it for the
       #beofre and after the Partition
       quickSortHelper(heightList,first,splitpoint-1)
       quickSortHelper(heightList,splitpoint+1,last)

def partition(heightList,first,last):
   #set a pivot value, in our case at the start
   pivotvalue = heightList[first]
   pivotindex = first

   #ensure that the border when swapping heightListound stuff, is right of the 
   border = first+1
   end = last
   isCompleted = False
   swap = False

   while not isCompleted:

       draw()
       pygame.draw.rect(window, blue, (xList[pivotindex],400-heightList[pivotindex],w,heightList[pivotindex]), 0)
       if swap:
           pygame.draw.rect(window, green, (xList[border],400-heightList[border],w,heightList[border]), 0)
           pygame.draw.rect(window, green, (xList[end],400-heightList[end],w,heightList[end]), 0)
           swap = False
       update_draw()
       buffer()

       #Basically this is once everythin is sorted and checks if its more
       while border <= end and heightList[border] <= pivotvalue:
           border = border + 1

       #Same thing as above but opposite and in this cfase its less
       while heightList[end] >= pivotvalue and end >= border:
           end = end -1

       #this is bascially once everything after the border, which in the end gos to the end, is smaller 
       if end < border:
           isCompleted = True

       #if not it swaps 
       else:
           #Before swaps
           pygame.draw.rect(window, red, (xList[border],400-heightList[border],w,heightList[border]), 0)
           pygame.draw.rect(window, red, (xList[end],400-heightList[end],w,heightList[end]), 0)
           update_draw()
           buffer()

           heightList[border], heightList[end] = heightList[end], heightList[border]
           
           #After swaps
           draw()
           pygame.draw.rect(window, blue, (xList[pivotindex],400-heightList[pivotindex],w,heightList[pivotindex]), 0)
           pygame.draw.rect(window, green, (xList[border],400-heightList[border],w,heightList[border]), 0)
           pygame.draw.rect(window, green, (xList[end],400-heightList[end],w,heightList[end]), 0)
           update_draw()
           buffer()


   #it swaps again
   pygame.draw.rect(window, red, (xList[first],400-heightList[first],w,heightList[first]), 0)
   pygame.draw.rect(window, red, (xList[end],400-heightList[end],w,heightList[end]), 0)
   update_draw()
   buffer()

   heightList[first], heightList[end] = heightList[end], heightList[first]

   draw()
   pygame.draw.rect(window, blue, (xList[pivotindex],400-heightList[pivotindex],w,heightList[pivotindex]), 0)
   pygame.draw.rect(window, green, (xList[first],400-heightList[first],w,heightList[first]), 0)
   pygame.draw.rect(window, green, (xList[end],400-heightList[end],w,heightList[end]), 0)
   update_draw()
   buffer()

   return end

quickSort(heightList)

#Sort Ended

#End animation
draw()
update_draw()
buffer()
#green going up
for i in range(0, listLength-1, 2):
    pygame.draw.rect(window, green, (xList[i],400-heightList[i],w,heightList[i]), 0)
    pygame.draw.rect(window, green, (xList[i+1],400-heightList[i+1],w,heightList[i+1]), 0)
    update_draw()
    buffer()
#green going down
for i in range(listLength-1, 0, -2):
    pygame.draw.rect(window, white, (xList[i],400-heightList[i],w,heightList[i]), 0)
    pygame.draw.rect(window, white, (xList[i-1],400-heightList[i-1],w,heightList[i-1]), 0)
    update_draw()
    buffer()

#Show results
print(heightList)

#Ended
while True:
    buffer()