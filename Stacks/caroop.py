#!/usr/bin/python3

class Node():
    # Constructor method
    def __init__(self, data):
        self.data = data
        self.next = None
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_next(self, new_next):
        self.next = new_next


class Stack():

    # Constructor method
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        # Check if the stack is NOT empty
        if not self.is_empty():
            # Point to the next element in the list
            new_node.set_next(self.top)
        # Set top to point to the new node
        self.top = new_node   

    def pop(self):
        popped_data = None
        if self.is_empty():
            print("Stack is empty - nothing to pop")
        else:
            # Get data and change pointer to next item
            popped_data = self.top.get_data()
            self.top = self.top.get_next()
        return popped_data
    
    def peek(self):
        peeked_data = None
        if self.is_empty():
            print("Stack is empty - nothing to peek")
        else:
            # Get data from the top of the stack
            peeked_data = self.top.get_data()

        return peeked_data
    
    def test_my_stack():
        my_stack = Stack()
        my_stack.push("carrots")
        my_stack.push("turnips")

        peeked_element = my_stack.peek()
        print(peeked_element)

        popped_element = my_stack.pop()
        print(popped_element)

my_stack = Stack()
my_stack.push("carrots")
my_stack.push("turnips")
my_stack.peek()