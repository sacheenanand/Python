__author__ = 'sanand'

#Insertion sort is both faster and well-arguably more simplistic than both bubble sort and selection sort.
# Funny enough, it’s how many people sort their cards when playing a card game! On each loop iteration, insertion
# sort removes one element from the array. It then finds the location where that element belongs within another
# sorted array and inserts it there. It repeats this process until no input elements remain.

#best case is big of n
# worst case is big of n^2
list = [9, 5, 2, 4, 3, 3]



for j in range(1, len(list)):
    current = list[j]
    i = j-1
    while i >= 0 and list[i] > current:
        list[i+1] = list[i]
        i = i -1
    list[i + 1] = current
    print(list)










