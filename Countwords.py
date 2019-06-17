__author__ = 'sanand'


str = "as ddf asas kasmal"
def count_words(str):
    if (not str):
        return 0

    numbers = 0
    prev = False

    for c in str:
        cur = c.isalpha()

        if(not prev and cur):
            numbers += 1
        prev = cur
    return numbers
print(count_words(str))




