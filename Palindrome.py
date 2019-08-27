__author__ = 'sanand'

import string

def is_palindrome(s):
    s = s.lower()
    #s = s.translate(None, string.punctuation)
    s = s.replace(" ", "")

    return s == s[::-1]

str_1 = "racecar"
str_2 = " bad dab"

print(is_palindrome(str_1))
print(is_palindrome(str_2))
