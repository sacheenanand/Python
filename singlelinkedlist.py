__author__ = 'sanand'

# insert a node end of a list
#insert a node at begining of the list
#



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def printlist(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("There is nothing in the list")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def iterative_length(self):

        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def recursive_length(self, node):
        if node is None:
            return 0
        return 1 + self.recursive_length(node.next)



llist = Linkedlist()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
#print(llist.iterative_length())
print(llist.recursive_length(llist.head))
#llist.append("Vanitha")
#llist.prepend("Apple")
#print(llist.head.data)
#print(llist.head.next.data)
#llist.insert_after_node(llist.head.next, "E")

llist.printlist()












