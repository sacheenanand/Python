__author__ = 'sanand'



list1 = [1, 3, 5, 8 , 9]
list2 =[1, 2, 5, 7, 8 ]

def find(list1, list2):
    p1 = 0
    p2 = 0

    result = []

    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] == list2[p2]:
            result.append(list1[p1])
            p1 += 1
            p2 += 1

        elif list1[p1] > list2[p2]:
            p2 += 1

        else:
            p1 += 1
    return result

a = find(list1, list2)
print(a)



def reverse(str):
    if len(str) == 0:
        return str
    else:
        return reverse(str[1:]) + str[0]
str = "Utpal"
print(reverse(str))




