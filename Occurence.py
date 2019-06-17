__author__ = 'sanand'

# To check counts of each words
def word_count(str):
    counts = dict()
    words = str.split()



    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print(word_count("my name is sacheen and it was my name"))


a = [1, 2, 3, 4]
for i in range(len(a)):
    print(a[i], end = ' ')


