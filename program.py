__author__ = 'sanand'

import threading

def cube(num):
    print("cube: {} ".format(num * num * num))
def square(num):
    print("square: {} ".format(num * num ))

if __name__ == "__main__":
    t1 = threading.Thread(target=cube, args=(3,))
    t2 = threading.Thread(target=square, args=(2,))

#starting thrread 1 and thread 2
t1.start()
t2.start()

# wait until thread1 and thread2 completes

t1.join()
t2.join()

print("Done")

