#! /usr/bin/env python3

class CircularQueue:
    def __init__(self, max_size):
        self._max_size = max_size
        self._list = [None] * max_size
        self._front = 0
        self._rear = 0

    def put(self, element):
        if self._rear == self._max_size:
            raise OverflowError("Out of bounds")

        self._list[self._rear] = element

        # Wrap rear index using modulo for circular behavior
        self._rear = (self._rear + 1) % self._max_size

        return element

    def remove(self):
        if self._front == self._rear:
            raise IndexError("Empty")

        out = self._list[self._front]

        # Wrap front index using modulo for circular behavior
        self._front = (self._front + 1) % self._max_size

        return out

    def front(self):
        if self.is_empty():
            raise IndexError("Empty")

        return self._list[self._front]

    def rear(self):
        if self.is_empty():
            raise IndexError("Empty")

        return self._list[self._rear - 1]

    def is_full(self):
        # Queue is full if rear is before front
        return (self._rear - 1) % self._max_size == self._front

    def is_empty(self):
        # Queue is empty if front equals rear
        return self._front == self._rear


if __name__ == "__main__":
    q = CircularQueue(5)

    print (q.is_empty(), q.is_full())

    print(q.put(1))
    print(q.put(2))
    print(q.put(3))

    print(q.front(), q.rear())
    print (q.is_empty(), q.is_full())

    try:
        print(q.put(4))
        print(q.put(5))
        q.put(6)
    except OverflowError as e:
        print("Error: ", e)

    try:
        print(q.remove())
        print(q.remove())
        print(q.remove())
        print(q.remove())
    except IndexError as e:
        print("Error: ", e)
