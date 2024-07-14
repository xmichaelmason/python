#! /usr/bin/env python3

class SimpleQueue:
    def __init__(self, max_size):
        self._max_size = max_size
        self._list = [None] * max_size
        self._size = 0

    def enqueue(self, element):
        if self.is_full():
            raise OverflowError("Queue is full")

        self._list[self._size] = element
        self._size += 1

        return element

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        out = self._list[0]

        # Shift all elements to the left
        for i in range(1, self._size):
            self._list[i - 1] = self._list[i]

        self._size -= 1
        return out

    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        return self._list[0]

    def rear(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        return self._list[self._size - 1]

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._max_size


if __name__ == "__main__":
    q = SimpleQueue(5)

    print (q.is_empty(), q.is_full())

    print(q.enqueue(1))
    print(q.enqueue(2))
    print(q.enqueue(3))

    print(q.front(), q.rear())
    print (q.is_empty(), q.is_full())

    try:
        print(q.enqueue(4))
        print(q.enqueue(5))
        q.enqueue(6)
    except OverflowError as e:
        print("Error: ", e)

    try:
        print(q.dequeue())
        print(q.dequeue())
        print(q.dequeue())
        print(q.dequeue())
        print(q.dequeue())
        print(q.dequeue())
    except IndexError as e:
        print("Error: ", e)
