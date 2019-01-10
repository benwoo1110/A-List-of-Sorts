Arr = [166, 226, 238, 328, 392, 465, 68, 59, 273, 123]

def bubbleSort():
    for i in range(len(Arr)-1, 0, -1):
        for j in range(i):
            if Arr[j]>Arr[j+1]:
                temp = Arr[j]
                Arr[j] = Arr[j+1]
                Arr[j+1] = temp

bubbleSort(); print(Arr)
