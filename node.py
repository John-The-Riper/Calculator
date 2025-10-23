"""
Filename:mode.py
Author: <McDougal, Owen>
Created: <10/23/2025>
Instructor: Holtslander
"""
class Node:
    def __init__(self, data, next=None):
        self._data = data
        self._next = next

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_next(self, node):
        self._next = node
