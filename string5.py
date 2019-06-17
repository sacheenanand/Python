__author__ = 'sanand'

#to check if string is palindrome or not.

import string


def is_palindrome(s):
    s = s.lower()
    s = s.translate(string.punctuation)
    s = s.strip()
    s = s.replace(" ", "")

    if s == s[:: -1]:
        return True
    else:
        return False


#    return s == s[:: -1]

s1 = "raceCar"
s2 = "car"
s3 = "saaaas"
s4 = "racecar racecar"

print(is_palindrome(s1))
print(is_palindrome(s2))
print(is_palindrome(s3))
print(is_palindrome(s4))


