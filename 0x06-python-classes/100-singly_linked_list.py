#!/usr/bin/python3
""" Module for singly linked list node creation"""


class Node:
    """ Class that defines a node in singly linked list"""

    def __init__(self, data, next_node=None):
        """Constructor

            Args:
                data: Node data
                next_node: next node address

            Raises:
                TypeError: data must be an integer
                TypeError: Node must be None or of class Node
        """

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Getter for data"""
        return self.__data

    @property
    def next_node(self):
        """Getter for next_node"""
        return self.__next_node

    @data.setter
    def data(self, value):
        """Setter for data"""

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """Setter for next_node"""

        if (not isinstance(value, Node) and value is not None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class that defines singly linked list"""

    def __init__(self):
        """Constructor"""

        self.__head = None

    def sorted_insert(self, value):
        """Method to insert a new node in a sorted order"""

        nnode = Node(value)
        if self.__head is None:
            nnode.next_node = None
            self.__head = nnode
        elif self.__head.data > value:
            nnode.next_node = self.__head
            self.__head = nnode
        else:
            hold = self.__head
            while hold.next_node is not None and hold.next_node.data < value:
                hold = hold.next_node
            nnode.next_node = hold.next_node
            hold.next_node = nnode

    def __str__(self):
        """Method to print the linked list"""

        value_list = []
        hold = self.__head
        while hold is not None:
            value_list.append(str(hold.data))
            value_list.append('\n')
            hold = hold.next_node
        value_list.pop()
        return '' .join(value_list)
