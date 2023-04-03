# from dataStructures.nodes.Node import Node
from Node import Node
class SLL:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.size = 0 if node==None else 1
    def __len__(self):
        return self.size
    def insertHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1
    def insertTail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
    def insert(self, node, index):
        if (index < 0 or index > self.size):
            print("Index out of range"  )
            raise Exception
        else:
            if index == 0:
                node.next = self.head
                self.head = node
                self.tail = node
            else:
                current = self.head
                for i in range(index - 1):
                    current = current.next
                node.next = current.next
                current.next = node
                if node.next is None:
                    self.tail = node
            self.size += 1
    def isSorted(self):
        current = self.head
        while current is not None:
            if current.next is not None:
                if current.data > current.next.data:
                    return False
            current = current.next
        return True 
    def sortedInsert(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            current = self.head
            while current is not None:
                if current.next is not None:
                    if current.data > current.next.data:
                        self.sort()
                current = current.next
            current = self.head
            previous = None
            while current is not None:
                if current.data > node.data:
                    if previous is None:
                        node.next = current
                        self.head = node
                    else:
                        previous.next = node
                        node.next = current
                    self.size += 1
                    return
                previous = current
                current = current.next
            previous.next = node
            self.tail = node
            self.size += 1
    def search(self, node):
        if self.head is None:
            print("List is empty")
            return None
        else:
            current = self.head
            while current is not None:
                if current == node:
                    return node
                current = current.next
            return None
    def deleteHead(self):
        if self.head is None:
            print("List is empty")
        else:
            if(self.tail == self.head):
                self.tail = None
            self.head = self.head.next
            self.size -= 1
    def deleteTail(self):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            previous = None
            while current.next is not None:
                previous = current
                current = current.next
            if previous is None:
                self.head = None
                self.tail = None
            else:
                previous.next = None
                self.tail = previous
            self.size -= 1
    def delete(self, node):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            previous = None
            while current is not None:
                if current == node:
                    if previous is None:
                        self.head = current.next
                        self.tail = current.next
                    else:
                        previous.next = current.next
                    self.size -= 1
                    return
                previous = current
                current = current.next
    def sort(self):
        if self.head is None:
            print("List is empty")
        else:
            for i in range(self.size):
                current = self.head
                for j in range(self.size - i - 1):
                    if(current.data > current.next.data):
                        temp = current.data
                        current.data = current.next.data
                        current.next.data = temp
                    current = current.next
    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0
    def print(self):
        print("SLL length:", self.size)
        sortedStatus = "Sorted" if self.isSorted() else "Unsorted"
        print("SLL Sorted:", sortedStatus)
        print("SLL Content:", end="")
        for i in range(self.size):
            temp = self.head
            print(temp.data, end=" ")
            temp = temp.next
        print()