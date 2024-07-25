class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def head_insert(self, data) -> Node:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
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
            self.size += 1
            return self.head
        current = self.traverse()
        current.next = new_node
        new_node.prev = current
        self.size += 1
        return self.head
    
    def position_insert(self, data, position):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return self.head
        if position >= self.size:
            self.size += 1
            return self.tail_insert(data)
        current = self.traverse(position)
        new_node.next = current.next
        current.next = new_node
        new_node.prev = current
        self.size += 1
        return self.head
        
    def traverse(self, position = None) -> Node:
        current = self.head
        if position is None:
            while current.next is not None:
                current = current.next
        else:
            if position >= self.size:
                position = self.size - 1
            counter = 0
            while counter < position - 1:
                current = current.next
                counter += 1
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
            self.head = None  # Corrected this line
            self.size -= 1
            return None

        prev = self.traverse(self.size - 1)  # Corrected index passed to traverse
        prev.next = None
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
    # Test cases
    dll = DoublyLinkedList()

    # Insertion tests
    dll.head_insert(1)
    dll.head_insert(2)
    dll.tail_insert(3)
    dll.position_insert(4, 1)

    # Display the list
    current = dll.head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

    # Deletion tests
    dll.head_delete()
    dll.tail_delete()
    dll.position_delete(1)

    # Display the list after deletions
    current = dll.head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

    # Search and length tests
    print("Length of the list:", dll.find_length())
    print("Is 4 in the list?", dll.search(4))
    print("Is 1 in the list?", dll.search(1))