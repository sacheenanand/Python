__author__ = 'sanand'
# Remove duplicates in a string


# to remove duplicates in a given string



def duplicates_string(given_string):
    empty = ""
    for each_element in given_string:
        if each_element not in empty:
            empty += each_element
    return empty
print("Take out the duplicates" ,duplicates_string("AAAAA"))













