__author__ = 'sanand'

#. Bubble sort steps through the list and compares adjacent pairs of elements. The elements are swapped if they are in the
# wrong order. The pass through the unsorted portion of the list is repeated until the list is sorted.
# Because Bubble sort repeatedly passes through the unsorted part of the list, it has a worst case complexity of O(n²).


list = [5, 0, 3, 2, 4, 9, 8, 6, 21, 1]



#list = [3, 2, 1, 0, 4, 5, 6, 7, 8, 9]

for j in range(0, 9):
    check = False
# for one time swap
    for i in range(0, 9):
        if list[i] > list[i+1]:
            swap = list[i]
            list[i] = list[i+1]
            list[i+1] = swap
            check = True
    if check == False:
        break

print(j,list)




