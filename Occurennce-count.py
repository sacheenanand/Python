__author__ = 'sanand'


# to program the occurence of each word in a given sentence.

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print(word_count("My name is Sacheen and brother name is Jatheen and dad name is Anand and mom name is Vanitha and son name is Arin"))






