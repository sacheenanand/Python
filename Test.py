__author__ = 'sanand'
print("sacheen to test")

with open("xyx.txt", "w") as f:
    f.write("hello world")
with open("xyx.txt", "r") as f:
    sacheen = f.read()
print(sacheen)
with open("xyx.txt", "a") as f:
    f.write("\npython opening and closing")
with open("xyx.txt") as f:
    same = f.read()
print(same)


