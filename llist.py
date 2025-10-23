from node import Node
class LList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._current = None
        self._size = 0

    def append(self, data):
        new_node = Node(data)
        if not self._head:
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def goto_start(self):
        self._current = self._head

    def next(self):
        if self._current is not None:
            self._current = self._current.next

    def get_data(self):
        if self._current is None:
            raise IndexError("Current pointer is None (end of list or empty list).")
        return self._current.data

    def at_end(self):
        return self._current is None

    def __len__(self):
        return self._size
