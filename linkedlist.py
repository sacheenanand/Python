__author__ = 'sanand'


# python single linked list , creating a new list, inserting a node , delete a node and display a node

#create a node
#create a linked list
# add node to linked list
# print linked list


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:

                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode
    def printlist(self):
        curnode = self.head

        while True:
            if curnode is None:
                break
            print(curnode)
            curnode = curnode.next





# node should always have data

firstNode = Node("John")
list = Linked_list()
list.insert(firstNode)
secondNode = Node("sacheen")
list.insert(secondNode)
thirdNode = Node("Arin")
list.insert(thirdNode)

list.printlist()





