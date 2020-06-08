__author__ = 'sanand'

a_string = "Sacheen"
for each_element in a_string:
    print(each_element)

for i in range(len(a_string)):
    print(a_string[i])


# to check when strings are reversed are same
def string_reverse(string_1, string_2):
    for i in range(len(string_1)):
        i_2 = len(string_2)-i-1
        if string_1[i] != string_2[i_2]:
            return False
        return True
string_reverse("ABC", "CBA")
string_reverse("ABC", "AAA")






