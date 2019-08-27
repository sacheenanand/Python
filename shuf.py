__author__ = 'sanand'
'''
from random import shuffle

li =[2, 4,6,9]

shuffle(li)
print(li)


def testang(a, b):

    if sorted(a.lower()) == sorted(b.lower()):
        print("strings are anagram")
    else:
        print("Not an anagram")
a = "dad"
b = "mad"

testang(a, b)


list = [1,2,3,1,4,1]
list1 = [3,3,4,5,6,7,8]
list2 = [-1, -1, 2, 3, 4, 5, 6, 7, 2, 2, -1, -1, -1]


def mostlyused(givenlist):
    max_count = -1
    item = None
    count = {}
    for i in givenlist:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

        if count[i] > max_count:
            max_count = count[i]
            item = i
#    return max_count
    return item


print("The maximun items that appeard " ,mostlyused(list))
print("The maximun items that appeard " ,mostlyused(list1))
print("The maximun items that appeard " ,mostlyused(list2))

'''

# given two list find the common elements
'''
def given_two_list(list1, list2):
    pos0 = 0
    pos1 = 0
    result = []

    while pos0 < len(list1) and pos1 < len(list2):
        if list1[pos0] == list2[pos1]:
            result.append(list1[pos0])
            pos0 += 1
            pos1 += 1

        elif list1[pos0] > list2[pos1]:
            pos1+=1
        else:
            pos0+=1
    return result
list_a1 = [1, 3, 6, 7, 9, 10,19]
list_a2 = [1, 2, 4, 5, 9, 10,19]

print("the common elements ", given_two_list(list_a1,list_a2))
'''

'''
larg = -1

for num in [10, 20, 30 , 40]:
    if num > larg:
        larg = num
print(num)
'''

'''
def even_num(ls):
    return [num for num in ls if num % 2 == 0]
print("even numbers are ", even_num([10, 3, 2, 8, 12, 28,3,9,13,17,11,24,1190,1191]))ail

# Palindome

def palindrome(s):
    head, tail =0, len(s)-1
    while head < tail:
        while not s[head].isalnum():
            head +=1
        while not s[tail].isalnum():
            tail -=1
        if s[head]!= s[tail]:
            return False

        head+=1
        tail-=1
    return True

print("is it ",palindrome("bob") )
print("is it ", palindrome("boo"))
print("is it",palindrome("tot"))
print("is it ",palindrome("bab2"))

# reverse a string
s = "sac"
def reverse(s):
    if len(s)==0:
        return s
    else:
        return reverse(s[1:])+ s[0]
print(reverse(s))



#bubble sort practising



list = [10, 9, 8, 2, 4, 1]



def bubble_sort(list):
    for j in range(0,5):
        for i in range(0, 5):
            if list[i]>list[i+1]:
                swap = list[i]
                list[i] = list[i+1]
                list[i+1]=swap
    return list
print(bubble_sort(list))


#selection sort algorithm.

list = [10, 9, 8, 2, 4, 1]

def selection_sort(list):
    for i in range(0, 6):
        min = i
        for m in range(i+1, 6):
            if list[min] > list[m]:
                min = m
                temp = list[i]
                list[i] = list[min]
                list[min] = temp
    return list
print(selection_sort(list))


list = [9, 3, 4, 5, 6, 3, 1, 2, 1,1,1]
def bubble(list):
    for j in range(0, 10):
        for i in range(0, 10):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
    return list
print("here is the sorting", bubble(list))

'''

def sum1(n):
    count = 0
    for i in range(0,n+1):
        count +=i
    return count
print("here is my total", sum1(10))






