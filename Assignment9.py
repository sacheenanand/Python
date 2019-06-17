__author__ = 'sanand'



counts = dict()
names = ['sacheen', 'jatheen','Arin','Ishaan', 'Nishka', 'Utpal', 'Vanitha','sacheen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1

print(counts)





