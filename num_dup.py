__author__ = 'sanand'

def remove_dup(dup_list):
    new_list =[]
    for i in dup_list:
        if i not in new_list:
            new_list.append(i)
    return new_list
a = remove_dup([1,2,2,4,4,1,1,1,3,3])
print(a)





