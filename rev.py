__author__ = 'sanand'

def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
q = str(input("Enter a string to be reversed  "))
print(reverse(q))




