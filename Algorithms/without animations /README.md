1. Bubble Sort

  A version in English
2. Quick Sort 

  The main oprandi of quicksort is divide and conquer. Quicksort tends to sort things based on whether they are larger or smaller than a specific pivot value. In our case. The pivot value is alway at the front. (For simplicities sake.
  
  It divides and conquers leftmost.
  We begin by incrementing leftmark until we locate a value that is greater than the pivot value. We then decrement rightmark until we find a value that is less than the pivot value. At this point we have discovered two items that are out of place with respect to the eventual split point. Then, we can exchange these two items and then repeat the process again.

  Ensure the the Lefrmost value that has crossed before it start the whole thing above again. But ensure the right index vgalue to the last iteration before the leftmost value

  Then ensure that once it goes all the way left, it goes one right and then does the two pargraphs against by diving at the split point. The quick sort can be invoked recursively on the two halves.

3. Merge Sort

    Merge sort is a recursive algorithm that continually splits a list in half. If the list is empty or has one item, it is sorted by definition (the base case). If the list has more than one item, we split the list and recursively invoke a merge sort on both halves. Once the two halves are sorted, the fundamental operation, called a merge, is performed. Merging is the process of taking two smaller sorted lists and combining them together into a single, sorted, new list. The mergeSort function shown in ActiveCode 1 begins by asking the base case question. If the length of the list is less than or equal to one, then we already have a sorted list and no more processing is necessary. If, on the other hand, the length is greater than one, then we use the Python slice operation to extract the left and right halves. It is important to note that the list may not have an even number of items. That does not matter, as the lengths will differ by at most one.

