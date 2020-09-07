"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass."""

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
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
