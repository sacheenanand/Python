__author__ = 'sanand'

#Python | Program to accept the strings which contains all vowels

def check(string):
    vowels = set('aeiou')
    s = set({})
    for char in string:
        if char in vowels:
            s.add(char)
        else:
            pass

        if len(s) == len(vowels):
            print("accepted")
        else:
            print("not accepted")
string = "saeiounmawer"
check(string)


'''if __name__ == "__main__":
    string = "SAcEiouheen"
    string = string.lower()
    check(string)

'''
