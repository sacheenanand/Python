__author__ = 'sanand'


# to count words in a given string.

string1 = "Sacheen Anannd"
def count_words(string1):
    if(not string1):
        return 0

    num_words = 0
    prev_char = False
    for c in string1:
        cur_char = c.isalpha()

        if(not prev_char and cur_char):
            num_words += 1
        prev_char = cur_char
    return num_words
print(count_words(string1))









