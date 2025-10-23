"""
Filename:lstack.py
Author: <McDougal, Owen>
Created: <10/23/2025>
Instructor: Holtslander
"""
from node import Node

class LStack:
    def __init__(self):
        self._head = None
        self._size = 0

    def push(self, data):
        new_node = Node(data, self._head)
        self._head = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        data = self._head.get_data()
        self._head = self._head.get_next()
        self._size -= 1
        return data

    def clear(self):
        self._head = None
        self._size = 0

    def is_empty(self) -> bool:
        return self._size == 0

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._head.get_data()

    def __len__(self) -> int:
        return self._size
