__author__ = 'sanand'

#def reverse(string):
#    if len(string) == 0:
#        return string
#    else:
#        return reverse(string[1:]) + string[0]
#q = str(input("Enter a string to be reversed  "))
#print(reverse(q))



list = [5,4,1,2,0]
#print(len(list))

for j in range(0, 4):
    check = False
    for i in range(0, 4):
        if list[i] > list[i+1]:
            swap = list[i]
            list[i] = list[i+1]
            list[i+1] = swap
            check = True
    if check == False:

        break
print(j, list)




