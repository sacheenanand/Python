__author__ = 'sanand'

# to find in a string which is non repeating character.

#abbccda

def non_repeating(given_string):
    count = {}

    for each_item in given_string:
        if each_item not in count:
            count[each_item] = 1
        else:
            count[each_item] += 1
#            print(count)

    for each_item in given_string:
        if count[each_item] == 1:
            return each_item
    return None
print("Non-repeat", non_repeating("abcab") )

# should return 'c'
print("Non-repeat",non_repeating("abab"))
# should return None
print("Non-repeat",non_repeating("aabbbc"))
 # should return 'c'
print("Non-repear",non_repeating("aabbdbc"))

 # should return 'd')
