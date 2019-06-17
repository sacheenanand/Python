__author__ = 'sanand'

# to find upper case letters in strings

input_str_1 = "Sacheen"
input_str_2 = "sachEen"
input_str_3 = "saheenananD"

def find_uppercase_iterative(string):
    for i in range(len(string)):
      if string[i].isupper():
        return string[i]
    return "no uppercase found"


def find_uppercase_recursive(string, indx=0):
    if string[indx].isupper():
      return string[indx]
    if indx == len(string) - 1:
      return "No upper case found"
    return find_uppercase_recursive(string, indx+1)


print(find_uppercase_iterative(input_str_1))
print(find_uppercase_iterative(input_str_2))
print(find_uppercase_iterative(input_str_3))

print(find_uppercase_recursive(input_str_1))
print(find_uppercase_recursive(input_str_2))
print(find_uppercase_recursive(input_str_3))





