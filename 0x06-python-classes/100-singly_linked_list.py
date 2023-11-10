#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        """Defines a node of a singly linked list"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data getter"""
        return self._data

    @data.setter
    def data(self, value):
        """data setter"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """next_node getter"""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """next_node setter"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    def __init__(self):
        """Defines a singly linked list"""
        self.head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None\
                    and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
