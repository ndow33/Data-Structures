"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.

class Stack:
    def __init__(self, size=0):
        self.size = size
        self.values = []
        # self.storage = ?

    def __len__(self):
        return len(self.values)

    def push(self, value):
        return self.values.append(value)

    def pop(self):
        if len(self.values) >= 1:
            return self.values.pop()
        else:
            return
"""

"""
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
"""
from singly_linked_list import Node

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        if self.head is None and self.tail is None:
            return 0
        else:
            current = self.head
            counter = 1
            while current.get_next() is not None:
                counter += 1
                current = current.get_next()

            return counter

    def push(self, value):
        # create a new node
        new_node = Node(value)
        # If there is no head or tail it is an empty linked list so
        # create a new node that is both head and tail...
        if self.tail == None and self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            # 2. Set the old tail's next to refer to the new Node
            self.tail.set_next(new_node)
            # 3. Reassign self.tail to refer to the new Node
            self.tail = new_node

    def pop(self):
        # check for a non-empty linked list
        if self.head is None and self.tail is None:
            return
        # iterate over the linked list til we are at the second to last node
        current = self.head
        while current.get_next() is not self.tail:
            current = current.get_next()
        # set current to the tail's value and tail to none
        val = current.next.get_value()
        current.set_next(None)
        return val
        

"""
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
