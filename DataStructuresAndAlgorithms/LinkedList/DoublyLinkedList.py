#!/usr/bin/env python3
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def head_insert(self, data) -> Node:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1
        return self.head
    
    def tail_insert(self, data) -> Node:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.size += 1
            return self.head
        current = self.reverse_traverse(self.size - 1)
        new_node.prev = current
        current.next = new_node
        self.tail = current.next
        self.size += 1
        return self.head
    
    def position_insert(self, data, position):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.size += 1
            return self.head

        if position >= self.size:
            return

        current = self.traverse(position)
        current.next.prev = new_node
        new_node.next = current.next
        new_node.prev = current
        current.next = new_node
        self.size += 1

        return self.head

        
    def traverse(self, position = None) -> Node:
        current = self.head
        if position is None:
            while current.next is not None:
                current = current.next
        else:
            if position >= self.size:
                return
            counter = 0
            while counter < position - 1:
                current = current.next
                counter += 1
        return current

    def reverse_traverse(self, position = None):
        current = self.tail
        if position is None:
            current = current.prev
        else:
            if position >= self.size:
                return
            counter = self.size - 1
            while counter > position:
                current = current.prev
                counter -= 1
        return current
    
    def head_delete(self):
        current = self.head
        if current is None:
            return None
        self.head = current.next
        self.head.prev = None
        current = None
        self.size -= 1
        return self.head
    
    def tail_delete(self):
        if self.head is None:
            return None
        if self.head.next is None:
            self.head = None
            self.tail = self.head.prev
            self.size -= 1
            return None

        prev = self.reverse_traverse(1)  # Corrected index passed to traverse
        prev.next = None
        self.tail = prev
        self.size -= 1
        return self.head
    
    def position_delete(self, position):
        if self.head is None:
            return None
        if position >= self.size:
            return

        if position == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            self.size -= 1
            return self.head

        prev = self.traverse(position - 1)
        current = prev.next
        if current.next:
            current.next.prev = prev
        prev.next = current.next
        current = None
        self.size -= 1
        return self.head

    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def find_length(self):
        current = self.head
        counter = 0
        while current is not None:
            current = current.next
            counter += 1
        return counter
    

if __name__ == "__main__":
    # Create a new doubly linked list
    dll = DoublyLinkedList()

    # Test head insertion
    print("Inserting 1 at head")
    dll.head_insert(1)
    print(f"List length: {dll.find_length()}")
    print(f"Head: {dll.head.data}")
    print(f"Tail: {dll.tail.data}")

    print("Inserting 2 at head")
    dll.head_insert(2)
    print(f"List length: {dll.find_length()}")
    print(f"Head: {dll.head.data}")
    print(f"Tail: {dll.tail.data}")

    print("Inserting 3 at head")
    dll.head_insert(3)
    print(f"List length: {dll.find_length()}")
    print(f"Head: {dll.head.data}")
    print(f"Tail: {dll.tail.data}")

    # Test tail insertion
    print("Inserting 4 at tail")
    dll.tail_insert(4)
    print(f"List length: {dll.find_length()}")
    print(f"Head: {dll.head.data}")
    print(f"Tail: {dll.tail.data}")

    # Test position insertion
    print("Inserting 5 at position 2 (0-based index)")
    dll.position_insert(5, 2)
    print(f"List length: {dll.find_length()}")
    print(f"Head: {dll.head.data}")
    print(f"Tail: {dll.tail.data}")

    # Test head deletion
    print("Deleting head")
    dll.head_delete()
    print(f"List length: {dll.find_length()}")
    print(f"New head: {dll.head.data}")
    print(f"Tail: {dll.tail.data}")

    # Test tail deletion
    print("Deleting tail")
    dll.tail_delete()
    print(f"List length: {dll.find_length()}")
    print(f"Head: {dll.head.data}")
    print(f"New tail: {dll.tail.data}")

    # Test position deletion
    print("Deleting at position 1 (0-based index)")
    dll.position_delete(1)
    print(f"List length: {dll.find_length()}")
    print(f"Head: {dll.head.data}")
    print(f"Tail: {dll.tail.data}")

    # Test search
    print("Searching for values")
    print(f"Search for 2: {dll.search(2)}")
    print(f"Search for 5: {dll.search(5)}")
    print(f"Search for 10: {dll.search(10)}")

    print("All tests completed!")
