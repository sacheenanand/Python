__author__ = 'sanand'
#working with To Files at same time
#There are times when you may want to read a file and write to another file at same time.

d_path = "dog_breeds.txt"
d_r_path = " dog_breeds_reversed.txt"

with open(d_path, 'r') as reader, open(d_r_path, 'w') as writer:
    dog_breeds = reader.readlines()
    writer.writelines(dog_breeds.__reversed__())
    #writer.writelines(dog_breeds.reversed())


