def firstNotRepeatingCharacter(s):
    for c in s:
        if s.index(c) == s.rindex(c):
            return c
    return '_'
q = str(input("Enter a string:-\n "))
print(firstNotRepeatingCharacter(q))


