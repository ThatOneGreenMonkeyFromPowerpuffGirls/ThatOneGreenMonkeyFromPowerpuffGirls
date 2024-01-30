#!/usr/bin/python3

class Node():# Nooooooooooode
    def __init__(self, given_data):
        """Constructor method"""
        self.data = given_data
        self.next = None


class LinkedList():
    def __init__(self):
        """Constructor method"""
        self.head = None

    def insert_at_front(self, data):
        # Create a new node
        new_node = Node(data)

        # Check if the head node exists
        if self.head is None:
            self.head = new_node
        else:
            # Update the pointers so the new node is the head
            new_node.next = self.head            
            self.head = new_node


    def traverse(my_list):
        # Set the current node as the head
        current = my_list.head

        # Repeat until there are no more linked nodes
        while current is not None:
            print(current.data)
            current = current.next


# Instantiate an empty linked list object
my_list = LinkedList()

# Test innit
my_list.insert_at_front("treefutom")
print(my_list.head)
print(my_list)