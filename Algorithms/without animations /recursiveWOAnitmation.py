from random import randint

#Adding Stuff Now
Arr = []
# for i in range(10):
#     Arr.append(randint(0, 500))
# print(Arr) 
Arr = [166, 226, 238, 328, 392, 465, 68, 59, 273, 123]


#Function
def quickSort(Arr, border=0, pivotIndex=0, end=len(Arr), isAllDone=False):
    pivotValue = Arr[0]
    operations(Arr, pivotValue, border, pivotIndex, end, start=pivotIndex, isSolved=False)
    return(Arr)

#Operations when finding out stuff?
def operations(Arr, pivotValue, border, pivotIndex, end, start, isSolved):
    for i in range(start+1, end):
        if Arr[i] < pivotValue:
            Arr.insert(border+1, Arr.pop(i))
            border+=1
    print(Arr)
    Arr.insert(border, Arr.pop(pivotIndex))
    end = border
    







#Output Statement
print(quickSort(Arr))
