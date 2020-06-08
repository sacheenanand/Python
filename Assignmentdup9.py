__author__ = 'sanand'

counts = dict()
names = ['sacheen', 'jatheen','Arin','Ishaan', 'Nishka', 'Utpal', 'Vanitha','sacheen', 'jatheen']
for name in names:
    counts[name] = counts.get(name, 0) +1
print(counts)
