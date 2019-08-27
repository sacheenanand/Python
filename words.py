__author__ = 'sanand'


# Python program to print even length words in a string

def words(s):
    s = s.split(' ')
    for element in s:
        if len(element) % 2 == 0:
            print(element)
s = "I am crazy as fcuk and I am joking"
words(s)


def print_odd_words(t):
    t = t.split(' ')
    for odd in t:
        if len(odd) % 2 != 0:
            print(odd)
t = "I am crazy as fcuk and I am joking"
print_odd_words(t)



