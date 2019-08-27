__author__ = 'sanand'



#A good example problem for showing algorithms with different orders of magnitude is the classic anagram detection problem for strings.
#One string is an anagram of another if the second is simply a rearrangement of the first. For example, 'heart' and 'earth' are anagrams.
#The strings 'python' and 'typhon' are anagrams as well. For the sake of simplicity, we will assume that the two strings in question are of
#equal length and that they are made up of symbols from the set of
#26 lowercase alphabetic characters. Our goal is to write a boolean function that will take two strings and return whether they are anagrams

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
b = "bbo"

Anagram(a,b)





