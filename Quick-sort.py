__author__ = 'sanand'
#Quick sort is also a divide and conquer algorithm like merge sort. Although it’s a bit more complicated,
# in most standard implementations it performs significantly faster than merge sort and rarely reaches
# its worst case complexity of O(n²). It has 3 main steps:


#(1) We first select an element which we will call the pivot from the array.
#(2) Move all elements that are smaller than the pivot to the left of the pivot; move all elements that are larger than the pivot to the right of the pivot. This is called the partition operation.
#(3) Recursively apply the above 2 steps separately to each of the sub-arrays of elements with smaller and bigger values than the last pivot.

Array = [48,44,19,59,72,80,42,65,82,8,95,68]


def quicksort(Array, low, high):
    if high - low > 0:
        p = partition(Array, low, high)
        #position of index to be sorted, p is index of the partion, p-1 is the position to be sorted from low.
        quicksort(Array, low, p-1)
        #p+1 is the position of index to be sorted to high.
        quicksort(Array, p+1, high)


def partition(Array, low, high):
    divider = low
    pivot = high
    #pivot is the last element, now take all the i elements and compare with pivot, use divider to keep swap for the element.
    for i in range(low, high):
        if Array[i] < Array[pivot]:
            Array[i], Array[divider] = Array[divider], Array[i]
            divider +=1
    Array[pivot], Array[divider] = Array[divider], Array[pivot]

    return divider

list1 = [48,44,19,59,72,80,42,65,45]
quicksort(list1, 0, 8)

print(list1)




