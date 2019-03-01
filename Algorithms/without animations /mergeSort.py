from random import random, sample

def mergesort(Arr): 
    n = len(Arr)
    n = int(n)
    if (n <= 1) :
        return Arr
    m = int(n//2)
    first = Arr[:m]
    second = Arr[m:]
    # print('---------')
    # print(first, second)
    mergesort(first)
    mergesort(second)

    i, j, k = 0, 0, 0

    while i< len(first) and j < len(second):
        if first[i] < second[j]:
            Arr[k] = first[i]
            i+=1
        else: 
            Arr[k] = second[j]
            j+=1

        k+=1
    while i < len(first): 
        Arr[k] = first[i]
        i+=1
        k+=1

    while j < len(second):
        Arr[k] = second[j]
        j+=1
        k+=1


Arr = [54,26,93,17,77,31,44,55,20]
mergesort(Arr)
print(Arr)
