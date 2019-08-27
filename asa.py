__author__ = 'sanand'

# using recursive method
def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]

q = str(input("Enter a string to be reversed:-\n "))
print(reverse(q))
print(q.count("e"))



#and dna
# nd + a
# d +  na
# dna

#anand
#nand + a = nanda
#nanda
#anda+n = andan
#andan
#ndan+a = ndana
#ndana
#dana+n = danan

