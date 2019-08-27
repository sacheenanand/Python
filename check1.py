__author__ = 'sanand'


list = [3, 2, 1, 9, 8, 7, 6]
for i in range(0, len(list)):
    minmum = i
#    print("I want the min value", minmum)
#   print("whats up ", list[minmum])
    for j in range(i+1, len(list)):
        if list[minmum] > list[j]:
            minmum = j
#           print("I am j value",list[j])
            temp = list[i]
            list[i]=list[minmum]
            list[minmum]=temp
print(list)





