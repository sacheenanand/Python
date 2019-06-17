__author__ = 'sanand'

while True:
    try:
        filename = input("what text file need to be opened  ")
        with open(filename) as f:
            print(f.read())
            break
    except FileNotFoundError:
        print("Sorry your file name " + filename + " is not found\n try again")
