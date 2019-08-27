__author__ = 'sanand'

#Selection sort is also quite simple but frequently outperforms bubble sort.
# If you are choosing between the two, it’s best to just default right to selection sort.
# With Selection sort, we divide our input list / array into two parts: the sublist of
# items already sorted and the sublist of items remaining to be sorted that make up the rest of the list.
# We first find the smallest element in the unsorted sublist and place it at the end of the sorted sublist.
# Thus, we are continuously grabbing the smallest unsorted element and placing it in sorted order in the sorted sublist.
# This process continues iteratively until the list is fully sorted.


#list = [5, 4, 6, 4, 8, 2, 1, 6 ,7, 9,100, 1]

list = [5, 4,3 ]
for i in range(len(list)):
#assuming the first element in the list
    min = i
    for j in range(i+1, len(list)):
        if list[min] > list[j]:
            min = j
            temp = list[i]
            list[i] = list[min]
            list[min] = temp
print(list)







