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
        self.__head = None

    def sorted_insert(self, value):
        new = Node(value)
        tmp = self.__head
        add_start = False

        if not self.__head:
            self.__head = new
            new.next_node = None
        else:
            if value < self.__head.data:
                add_start = True
            while tmp.next_node and value > tmp.next_node.data\
                    and not add_start:
                tmp = tmp.next_node
            if not add_start:
                new.next_node = tmp.next_node
                tmp.next_node = new
            else:
                new.next_node = tmp
                self.__head = new
            new.data = value

    def __str__(self):
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
