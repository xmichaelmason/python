class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def head_insert(self, data) -> Node:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        return self.head
    
    def tail_insert(self, data) -> Node:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.size = 1
            return self.head
        current = self.traverse()
        current.next = new_node
        self.size += 1
        return self.head
    
    def position_insert(self, data, position) -> Node:
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
        current = None
        self.size -= 1
        return self.head
    
    def tail_delete(self):
        if self.head is None:
            return None
        if self.head.next is None:
            self.head = None
            self.size -= 1
            return None

        current = self.traverse(self.size - 1)
        current.next = None
        
        self.size -= 1
        return self.head
    
    def position_delete(self, position):
        if self.head is None:
            return None
        if self.head.next is None:
            self.head = None
            self.size -= 1
            return None
        if position >= self.size:
            raise IndexError("Index out of bounds")
        prev = self.traverse(position)
        current = self.traverse(position + 1)
        prev.next = current.next
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
    # Create a new linked list instance
    linked_list = SinglyLinkedList()

    # Test head insertion
    linked_list.head_insert(10)
    linked_list.head_insert(20)
    linked_list.head_insert(15)
    print("After head insertions:")
    current = linked_list.head
    while current:
        print(current.data)
        current = current.next
    print("Length of the list:", linked_list.find_length())

    # Test tail insertion
    linked_list.tail_insert(40)
    linked_list.tail_insert(50)
    linked_list.tail_insert(60)
    print("\nAfter tail insertions:")
    current = linked_list.head
    while current:
        print(current.data)
        current = current.next
    print("Length of the list:", linked_list.find_length())

    # Test position insertion
    linked_list.position_insert(25, 2)
    linked_list.position_insert(100, 6)
    print("\nAfter position insertions:")
    current = linked_list.head
    while current:
        print(current.data)
        current = current.next
    print("Length of the list:", linked_list.find_length())

    # Test deletion operations
    linked_list.head_delete()
    linked_list.tail_delete()
    linked_list.position_delete(2)
    print("\nAfter deletions:")
    current = linked_list.head
    while current:
        print(current.data)
        current = current.next
    print("Length of the list:", linked_list.find_length())

    # Test search operation
    print("\nSearching for 30:", linked_list.search(30))
    print("Searching for 100:", linked_list.search(100))