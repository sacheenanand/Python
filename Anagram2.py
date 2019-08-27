__author__ = 'sanand'


def anagram(str1, str2):
    count1 = [0] * NUM_CHARACTERS
    count2 = [0] * NUM_CHARACTERS

    for c in str1:
        count1[ord(c)] += 1
    for c in str2:
        count2[ord(c)] += 1
    is_anagram = True
    if count1 != count2:
        is_anagram = False
    return is_anagram
str1 = "ct"
str2 = "tc"
anagram(str1, str2)






