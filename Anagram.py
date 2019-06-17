__author__ = 'sanand'

#Test using sort library.

def Anagram(s1, s2):
    if sorted(s1.lower()) == sorted(s2.lower()):
        print("Strings are anagram")
    else:
        print("String are not angram")

s1 = "Tac is cat"
s2 = "cat is tac"

Anagram(s1, s2)



# bob obb


def Anagram(a, b):
    if sorted(a.lower()) == sorted(b.lower()):
        print("String are Anagram")
    else:
        print("Strings are not Anagram")
a = "bob"
b = "tac"

Anagram(a,b)





