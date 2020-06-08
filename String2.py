__author__ = 'sanand'
# Remove duplicates in a string


def sacheen(mystring):
    newstring = ""
    for each_element in mystring:
      if each_element not in newstring:
        newstring += each_element
    return newstring
print(sacheen("xxxxyyyyyyzzzzzzxxxxxaaaa"))









