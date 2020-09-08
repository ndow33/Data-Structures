class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # 1. create the Node from the value
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
    
    def remove_head(self):
        if self.head is None and self.tail is None:
            return
        # what if we only have one element in our LinkedList?
        if not self.head.get_next():
            head = self.head
            # delete the linked list's head and tail reference
            self.head = None
            self.tail = None
            return head.get_value()
        else:
            # store the current head in a value
            val = self.head.get_value()
            # set self.head to the node after the head
            self.head = self.head.get_next
            return val

    def remove_tail(self):
        # if we have a non-empty linked list
        if self.head is None and self.tail is None:
            return
        # iterate over the linked list til 
        # we are at the second to last node
        current = self.head
        while current.get_next() is not self.tail:
            current = current.get_next()
        # move self.tail to the second to last node
        val = self.tail.get_value()
        self.tail = current
        return self.tail

