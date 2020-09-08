class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        self.next_node = new_next



class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None





    def add_to_tail(self, value):
        # make a new node with the value and a next value of none
        new_node = Node(value, None)
        # check if there is no head
        if self.head is None:
            # set the head and the tail to new node
            self.head = new_node
            self.tail = new_node
            print('Get it')
        # check if there is only one node
        elif self.head.get_next() is None and self.tail.get_next() is None:
            # set the next node to the tail
            self.head.set_next(new_node)
            self.tail = new_node
            print('Got it')
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
            print('Good')






    def remove_head(self):
        # check if there is no head
        if self.head is None:
            self.head = None
            self.tail = None
            return None
        # does our head have a next value?
        # if not, there is only one element in the list
        elif self.head.get_next() is None:
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()
        else:
            value = self.head.get_value()
            # set the head reference to the current head's next node in the list
            self.head = self.head.get_next()
            # return value
            return value





    def remove_tail(self):
        # if we have an empty linked list
        if self.head is None:
            self.head = None
            self.tail = None
            return None
        # does our head have a next value?
        # if not, there is only one element in the list
        elif self.head.get_next() is None:
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()
        else:
            current = self.head
            while current.get_next() is not self.tail:
                current = current.get_next()
            val = self.tail.get_value()
            self.tail = current
            current.set_next(None)
            return val



'''# Remove tail proofs

# Make a new, empty list
new_list = LinkedList()
print(f'1: Make a new, empty linked list. Head: {new_list.head}, Tail: {new_list.tail}')

# 2
print('Add the value 10 as a new node. Have this node be the head and the tail with none as the next node')
new_list.add_to_tail(10) # should be 10, none, 10, none
print(f'2: Head: {new_list.head.value}, Next node: {new_list.head.next_node}, Tail: {new_list.tail.value}, Next Node: {new_list.tail.next_node}')

# 3
print('add another value to the tail: this time it is 20. 20 should be the tail and the next node after the head')
new_list.add_to_tail(20)
print(f'3: Head: {new_list.head.value}, Next node: {new_list.head.next_node.value}, Tail: {new_list.tail.value}, Next Node: {new_list.tail.next_node}')

# remove
# 4
new_list.remove_tail()
print(f'4: Head: {new_list.head.value}, Next node: {new_list.head.next_node}, Tail: {new_list.tail.value}, Next Node: {new_list.tail.next_node}')
# 5
new_list.remove_tail()
print(f'5: Head: {new_list.head}, Tail: {new_list.tail}')
'''


'''
# Remove head proofs
# 1
print('Make a new list with head and tail set to none')
new_list = LinkedList()
print(f'1: Head: {new_list.head}, Tail: {new_list.tail}')
# add
# 2 
print('Add the value 10 as a new node. Have this node be the head and the tail with none as the next node')
new_list.add_to_tail(10) # should be 10, none, 10, none
print(f'2: Head: {new_list.head.value}, Next node: {new_list.head.next_node}, Tail: {new_list.tail.value}, Next Node: {new_list.tail.next_node}')

# 3
print('add another value to the tail: this time it is 20. 20 should also be the next node after the head')
new_list.add_to_tail(20)
print(f'3: Head: {new_list.head.value}, Next node: {new_list.head.next_node.value}, Tail: {new_list.tail.value}, Next Node: {new_list.tail.next_node}')

# remove
# 4
new_list.remove_head()
print(f'4: Head: {new_list.head.value}, Next node: {new_list.head.next_node}, Tail: {new_list.tail.value}, Next Node: {new_list.tail.next_node}')
# 5
new_list.remove_head()
print(f'5: Head: {new_list.head}, Tail: {new_list.tail}')
'''

