#! /usr/bin/env python3

class SimpleStack:
    def __init__(self, max_size):
        self._max_size = max_size
        self._list = [None] * max_size
        self._size = 0

    def push(self, element):
        if self.is_full():
            raise OverflowError("Out of bounds")

        self._list[self._size] = element
        self._size += 1

        return element

    def pop(self):
        if self.is_empty():
            raise IndexError("Empty")

        out = self._list[self._size - 1]
        self._list[self._size - 1] = 0
        self._size -= 1

        return out

    def peek(self):
        if self.is_empty():
            raise IndexError("Empty")

        return self._list[self._size - 1]

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._max_size
