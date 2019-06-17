__author__ = 'sanand'

#3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
#    Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.
a = input(" Enter  a score\n")
try:
    score = float(a)
    if 0.0 <= score < 0.6:
        print("F")
    elif 1.0 >= score >= 0.9:
        print("A")
    elif 0.9 >= score >= 0.8:
        print("B")
    elif 0.8 >= score >= 0.7:
        print("C")
    elif 0.7 >= score >= 0.6:
        print("D")
    else:
        print(" your number is not in range between 0 and 1")
except:
    print("Please enter the score between 0.0 and 1.0")
    quit()










