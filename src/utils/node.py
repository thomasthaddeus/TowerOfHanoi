"""node.py
This module contains the definition of the Node class.

The Node class is a basic building block for various data structures like linked lists. Each Node instance
holds a value and a reference to another Node, enabling the construction of linked or chain-like structures.
"""

class Node:
    """
    A Node is a fundamental part of data structures like linked lists. 
    It contains a value and a reference to another node, forming a chain.

    Attributes:
        value: The data value stored in the node.
        link_node: A reference to the next node in the chain, if any.
    """
    def __init__(self, value, link_node=None):
        """
        Initialize a new Node instance.

        Args:
            value: The value to be stored in the node. The type of value depends on the usage context of the node.
            link_node (Node, optional): A reference to another Node object. This is used to link nodes together in structures like linked lists. Defaults to None.
        """
        self.value = value
        self.link_node = link_node

    def set_next_node(self, link_node):
        """
        Set the reference to the next node in the chain.

        Args:
            link_node (Node): A Node object that will be the next node in the chain.
        """
        self.link_node = link_node

    def get_next_node(self):
        """
        Retrieve the next node in the chain.

        Returns:
            Node: The next node in the chain. Returns None if there is no linked node.
        """
        return self.link_node

    def get_value(self):
        """
        Get the value stored in the node.

        Returns:
            The value stored in the node. The type of the value depends on how the node is used.
        """
        return self.value
