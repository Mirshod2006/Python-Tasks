class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prior = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    
    def push(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prior = current

    def insert(self,value,index):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            i = 0
            while index > i and current.next is not None:
                current = current.next
                i += 1
            new_node.next = current
            if current.prior:
                new_node.prior = current.prior
                current.prior.next = new_node
            current.prior = new_node
            if i == 0:
                self.head = new_node

    def pop(self):
        if self.head is None:
            print("Your list is Empty!")
            return 0
        else:
            current = self.head
            while  current.next is not None:
                current = current.next
            value = current.data
            if current.prior:
                current.prior.next = None
            return value
    def display(self):
        if self.head is None:
            print("The list is empty.")
            return
        current = self.head
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

lst = [20,12,31,71,95,82,70,51,66] 
dll1 = DoubleLinkedList()
dll2 = DoubleLinkedList()
for i in lst:
    dll1.push(i)
second_lst = []
current = dll1.head
while current is not None:
    i = current.data%10
    second_lst.append(i)
    current = current.next

second_lst.sort()
for i in second_lst:
    dll2.push(i)
dll2.display()