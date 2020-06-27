def heapify(arr, n, i): 
	largest = i 
	l = 2 * i 
	r = 2 * i+ 1	 

	if l < n and arr[i] < arr[l]: 
		largest = l 

	if r < n and arr[largest] < arr[r]: 
		largest = r 

	if largest != i: 
		arr[i],arr[largest] = arr[largest],arr[i]

		heapify(arr, n, largest) 
 
def heapSort(arr): 
	n = len(arr) 

	for i in range(n/w/2 + 1, -1, -1): 
		heapify(arr, n, i) 

	for i in range(n-1, 0, -1): 
		arr[i], arr[0] = arr[0], arr[i] 
		heapify(arr, i, 0) 

arr = [ 9, 4, 56, 1, 6, 2, 6, 3, 6, 2, 6, 2, 6, 2, 67, 1, 8, 1, 9, 5, 3, 56] 
heapSort(arr) 

print(arr)

