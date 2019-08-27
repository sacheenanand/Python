__author__ = 'sanand'

'''
A = [99,21,19,22,28,11,14,18]
def merge_sort(A):
    merge_sort2(A, 0, len(A)-1)

def merge_sort2(A, first, last):
    if first < last:
        middle = (first + last)//2
        merge_sort2(A, first, middle)
        merge_sort2(A, middle+1, last)
        merge(A, first,middle, last)

def merge(A, first, last, middle):
    L = A[first:middle]
    print(L)
    R = A[middle+1:last]
    L.append(999)
    R.append(999)
    i=j=0
    for k in range(first, last+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i +=1
        else:
            A[k] = R[j]
            j +=1
    k = k + 1
merge_sort(A)
for sacheen in A:
    print(sacheen)
'''


Array = [8,2,9,10,9,1,3,4,5,6,7,8,9]


def merge(left, right, Array):
    i = j = k =0
    while i < len(left) and j < len(left):
        if left[i]< right[j]:
            Array[k] = left[i]
            i += 1
        else:
            Array[k] = right[j]
            j += 1
        k = k+1
#this conditon is for if one list is less than length.
    while i < len(left):
        Array[k] = left[i]
        i = i+1
        k = k+1
    while j < len(right):
        Array[k] = right[j]
        j = j +1
        k = k+1



#function for dividing and calling merge function
def mergesort(Array):
    n = len(Array)
    if n < 2:
        return
    mid = n/2
    left = []
    right = []

    for i in range(int(mid)):
        number = Array[i]
        left.append(number)
    for i in range(int(mid), int(n)):
        number = Array[i]
        right.append(number)
    mergesort(left)
    mergesort(right)

    merge(left, right, Array)

mergesort(Array)
for i in Array:
    print(i)










