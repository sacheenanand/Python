__author__ = 'sanand'

'''# using recursive method
def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]

q = str(input("Enter a string to be reversed:-\n "))
print(reverse(q))
print(q.count("e"))



#and dna
# nd + a
# d +  na
# dna

#anand
#nand + a = nanda
#nanda
#anda+n = andan
#andan
#ndan+a = ndana
#ndana
#dana+n = danan

'''

# repeat problems


list = [1,2,3,1,4,1]

list1 = [1,2,3,1,4,1,2,2,2,2, 8,8,8,8,8,8,8,8, 9,9,9,9,9,9,9,9,9,9,9,9,99,9]

list2 = [-1, -1, 2, 3, 4, 5, 6, 7, 2, 2, -1, -1, -1]


def repeat_numbers(given_list):
    number_counts = -1
    number_item = None
    dict = {}

    for items in given_list:
        if items not in dict:
            dict[items] = 1
        else:
            dict[items] += 1
        if dict[items] > number_counts:
            number_counts = dict[items]
            number_item = items
    return items
print("The maximun items that appeard " ,repeat_numbers(list))
print("The maximun items that appeard " ,repeat_numbers(list1))
print("The maximun items that appeard " ,repeat_numbers(list2))







