__author__ = 'sanand'

#Merge sort is a perfectly elegant example of a Divide and Conquer algorithm. It simple uses the 2 main steps of such an algorithm:
#(1) Continuously divide the unsorted list until you have N sublists,
# where each sublist has 1 element that is “unsorted” and N is the number of elements in the original array.
#(2) Repeatedly merge i.e conquer the sublists together 2 at a time to produce new sorted sublists until all elements have been
# fully merged into a single sorted array.


#array to be sorted
Array = [99,21,19,22,28,11,14,18,0,10,12,22]

#function for merging two sub-arrays
def merge(left, right, Array):
    i = 0
    j = 0
    k = 0

    while (i<len(left) and j<len(right)):
        if(left[i]<right[j]):
            Array[k] = left[i]
            i = i+1
        else:
            Array[k] = right[j]
            j = j+1

        k = k+1

    while(i<len(left)):
        Array[k] = left[i]
        i = i+1
        k = k+1

    while(j<len(right)):
        Array[k] = right[j]
        j = j+1
        k = k+1

#function for dividing and calling merge function
def mergesort(Array):
    n = len(Array)
    if(n<2):
        return

    mid = n/2
    left = []
    right = []

    for i in range(int(mid)):
        number = Array[i]
        left.append(number)

    for i in range(int(mid),int(n)):
        number = Array[i]
        right.append(number)

    mergesort(left)
    mergesort(right)

    merge(left,right,Array)

#calling mergesort
mergesort(Array)
for i in Array:
    print(i)






