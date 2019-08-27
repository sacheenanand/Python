__author__ = 'sanand'
# ## Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# ## determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
#
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
#
# <b>Example 1:</b>
#
# Input: "()"
# Output: true
#
# <b>Example 2:</b>
#
# Input: "()[]{}"
# Output: true
#
# <b>Example 3:</b>
#
# Input: "(]"
# Output: false
#
# <b>Example 4:</b>
#
# Input: "([)]"
# Output: false
#
# Input: "{[]}"
#
# Output: true</b>

'''
def valid_parenth(input):
    dic ={']':'[','}':'{',')':'('}
    stack = [];
    for char in input:
        if char in dic.values():
            stack.append(char)
        elif char in dic.keys():
            if stack == [] or dic[char] != stack.pop():
                return False
        else:
            return False
        return stack == []
print("is it ", valid_parenth("()"))


'''

'''
def isvalid_parenthesis(s):
    stack = []
    pairs = {'(':')', '[':']', '{':'}'}

    for char in s:
        if char in pairs:
            stack.append(pairs[char])
        else:
            if len(stack)==0 or stack.pop()!= char:
                return False
    return len(stack)==0
print("is it: ", isvalid_parenthesis("{}"))
print("is it: ", isvalid_parenthesis("{)"))
print("is it: ", isvalid_parenthesis("()"))
print("is it: ", isvalid_parenthesis(")"))
print("is it: ", isvalid_parenthesis("([{}])"))

'''

def Parenthesis(s):
    stack = []
    dict = {'(':')', '[':']', '{':'}'}

    for i in s:
        if i in dict:
            stack.append(dict[i])
        else:
            if len(stack) == 0 or stack.pop()!= i:
                return False
    return True

print("is it: ", Parenthesis("{}"))
print("is it: ", Parenthesis("{)"))
print("is it: ", Parenthesis("()"))
print("is it: ", Parenthesis(")"))
print("is it: ", Parenthesis("([{}])"))













