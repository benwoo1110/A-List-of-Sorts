'''
This is easy to understand
But hard to implement so imma just comment
'''


def quickSort(Arr):
   quickSortHelper(Arr,0,len(Arr)-1)

def quickSortHelper(Arr,first,last):
   if first<last:

       #Its going to Partiition
       splitpoint = partition(Arr,first,last)

       #Basically, per iteration you are running it  split into 2. So it does it for the
       #beofre and after the Partition
       quickSortHelper(Arr,first,splitpoint-1)
       quickSortHelper(Arr,splitpoint+1,last)

def partition(Arr,first,last):
   #set a pivot value, in our case at the start
   pivotvalue = Arr[first]

   #ensure that the border when swapping arround stuff, is right of the 
   border = first+1
   end = last
   isCompleted = False

   while not isCompleted:

       #Basically this is once everythin is sorted and checks if its more
       while border <= end and Arr[border] <= pivotvalue:
           border = border + 1

       #Same thing as above but opposite and in this cfase its less
       while Arr[end] >= pivotvalue and end >= border:
           end = end -1

       #this is bascially once everything after the border, which in the end gos to the end, is smaller 
       if end < border:
           isCompleted = True

       #if not it swaps 
       else:
           temp = Arr[border]
           Arr[border] = Arr[end]
           Arr[end] = temp


   #it swaps again
   Arr[first] = Arr[end]
   Arr[end] = temp

   return end

Arr = [54,26,93,17,77,31,44,55,20]
quickSort(Arr)
print(Arr)

