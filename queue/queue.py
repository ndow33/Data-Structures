"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.

class Queue:
    def __init__(self, size = 0):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        return self.storage.insert(0, value)

    def dequeue(self):
        if len(self.storage)>=1:
            return self.storage.pop()
        else:
            return
"""
"""
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass."""
from singly_linked_list import Node

class Queue:
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

    def enqueue(self, value):
        # store the value of head
        old_head = self.head
        # set the value of head to the input value
        self.head = value
        # set the value after head to the previous value of the head
        self.head.next = old_head

    def dequeue(self):
        if len(self.storage)>=1:
            return self.storage.pop()
        else:
            return

""""
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
