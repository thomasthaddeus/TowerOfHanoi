""" stack.py

This module defines the Stack class, a basic implementation of a stack data 
structure using linked nodes.

Stacks are a type of data structure that follow a 
Last In, First Out (LIFO) principle, where the last item added is the first to 
be removed.

This Stack class includes methods to push, pop, peek, and check the size and capacity of the stack.

Returns:
    _type_: _description_
"""

from utils.node import Node

class Stack:
    """
    A Stack is a collection of elements with a LIFO (Last In, First Out) principle. 
    This implementation uses linked nodes to store data.

    Attributes:
        size (int): The number of elements in the stack.
        top_item (Node): The top item of the stack.
        limit (int): The maximum capacity of the stack.
        name (str): The name of the stack.
    """
    def __init__(self, name):
        """
        Initialize a new Stack instance.

        Args:
            name (str): The name of the stack.
        """
        self.size = 0
        self.top_item = None
        self.limit = 1000
        self.name = name

    def push(self, value):
        """
        Add a new item to the top of the stack.

        If the stack is full, it will output a message indicating no more items 
        can be added.

        Args:
            value: The value to be added to the stack. The type depends on the 
            stack's usage.
        """
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            print("No more room!")

    def pop(self):
        """
        Remove and return the top item from the stack.

        If the stack is empty, it outputs a message indicating that there are 
        no items to pop.

        Returns:
            The value of the top item. The type of the value depends on the 
            stack's usage.
        """
        if self.size > 0:
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        print("This stack is totally empty.")

    def peek(self):
        """
        Return the value of the top item without removing it from the stack.

        Returns:
            The value of the top item. Returns None if the stack is empty. The 
            type of the value depends on the stack's usage.
        """
        if self.size > 0:
            return self.top_item.get_value()
        print("Nothing to see here!")

    def has_space(self):
        """
        Check if the stack has space to add more items.

        Returns:
            bool: True if the stack has space, False otherwise.
        """
        return self.limit > self.size

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.size == 0

    def get_size(self):
        """
        Get the current size of the stack.

        Returns:
            int: The number of items in the stack.
        """
        return self.size

    def get_name(self):
        """
        Get the name of the stack.

        Returns:
            str: The name of the stack.
        """
        return self.name

    def print_items(self):
        """
        Print all items in the stack.

        This method traverses the stack from top to bottom and prints each 
        item's value. The stack's current state is displayed in the order items 
        would be popped.
        """
        pointer = self.top_item
        print_list = []
        while pointer:
            print_list.append(pointer.get_value())
            pointer = pointer.get_next_node()
        print_list.reverse()
        print(f"{self.get_name()} Stack: {print_list}")
