__author__ = 'sanand'


#a = [x**2 for x in range(6) if x % 2 == 0]
#print(a)


#b = [x**2 for x in range(6) if x % 2 != 0]
#print(b)


def insertionSort(alist):

    for i in range(1,len(alist)):

        #element to be compared
        current = alist[i]

        #comparing the current element with the unsorted portion and swapping
        while i>0 and alist[i-1]>current:
            alist[i] = alist[i-1]
            i = i-1
        alist[i] = current

        print(alist)

    return alist

print(insertionSort([5,2,1,9,0,4,6]))


