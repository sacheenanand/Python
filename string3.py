__author__ = 'sanand'
'''
s = "this is a string"
s2 = "this is also string"

print(s[0])
print(len(s))

for char in s:
    print(char)
####
s3 = "sacheen anand\n"
####
for i in range(len(s3)):
    print(s3[i])
####
a_string = "ABC"
print(a_string)
####
b_string = "DEF"
print(b_string[1])

c_string = "GHI"
####
for char in c_string:
    print(char)
####
d_string = "pqr"
for i in range(len(d_string)):
    print(d_string[i])
'''

####
#string1 = "ABC"
#string2 = "CBA"
'''
def reverse_eachother(string1, string2):
    for i in range(len(string1)):
        i2 = len(string2)-i-1
    if string1[i] != string2[i2]:
      return False
    return True

reverse_eachother("ABC", "CBA")

'''

def is_unique(s):
    return len(s) == len(set(s))
s1 = "unique"
s2 = "bear"

print(is_unique(s1))
print(is_unique(s2))




