# insertionsort()

from random import randint

listLength = int(input("List Length: "))
heightList = list(range(listLength))
for i in range(listLength):
    heightList[i] = randint(0, 100)
print(heightList)
numOfSwaps = 0

'''
for c in range(1, listLength): #Green
    if heightList[c] < heightList[c-1]:
        lessList = [] #Red
        lessNum = 0
        change = False
        for s in range(c-1, -1, -1):
            if heightList[c] < heightList[s]:
                lessList += [heightList[s]]
            elif heightList[c] >= heightList[c]:
                lessNum = s
                change = True
                break
        lessList = lessList[::-1]
        if change == False:
            heightList = heightList[0:lessNum] + [heightList[c]] + lessList + heightList[c+1::]
            numOfSwaps += 1
        elif change == True:
            heightList = heightList[0:lessNum+1] + [listSort[c]] + lessList + heightList[c+1::]
            numOfSwaps += 1
'''
for c in range(1, listLength):
    for s in range(c, 0, -1):
        if heightList[s] < heightList[s-1]:
            heightList[s], heightList[s-1] = heightList[s-1], heightList[s]
            numOfSwaps +=1
        else: break

print(heightList)
print('numOfSwaps:', numOfSwaps)
