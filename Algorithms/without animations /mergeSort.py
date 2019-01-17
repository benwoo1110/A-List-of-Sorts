from random import random, sample
third = []
def mergesort(Arr): 
    n = len(Arr)
    n = int(n)
    if (n <= 1) :
        return Arr
    m = int(n//2)
    first = Arr[:m]
    second = Arr[m:]

    mergesort(first)
    mergesort(second)

    # print(first, second)
    merge(first, second)


def merge(first, second):
    
    while len(first) and len(second):
        if first[0] > second[0]:
            third.append(second.pop(0))
        else:
            third.append(first.pop(0))

    while (len(first)):
        third.append(first.pop(0))

    while (len(second)):
        third.append(second.pop(0))

    return third
Arr = sample(range(100), 16)
print(Arr)
print(mergesort(Arr))
