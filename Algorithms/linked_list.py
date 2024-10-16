class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def pop(self):
        if not self.head:
            return None
        if self.head.next is None:
            value = self.head.data
            self.head = None
            return value
        current = self.head
        while current.next.next:
            current = current.next

        value = self.head.data
        self.head = None
        return value
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")