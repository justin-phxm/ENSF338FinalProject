# from dataStructures.nodes.Node import Node
from DNode import DNode
class DLL:
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
            self.head.previous = node
            self.head = node
        self.size += 1

    def insertTail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node
        self.size += 1

    def insert(self, node, index):
        if (index < 0 or index > self.size):
            print("Index out of range"  )
            raise IndexError
        else:
            if index == 0:
                node.next = self.head
                self.head = node
                self.tail = node
            else:
                current = self.head
                for i in range(index - 1):
                    current = current.next
                if(current.next is not None):
                    current.next.previous = node
                node.next = current.next
                current.next = node
                node.previous = current
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
            if(self.isSorted() == False):
                self.sort()
            current = self.head

            while current is not None:
                if current.data > node.data:
                    if current.previous is None:
                        node.next = current
                        current.previous = node
                        self.head = node
                    else:
                        current.previous.next = node
                        node.previous = current.previous
                        node.next = current
                        current.previous = node
                    self.size += 1
                    return
                current = current.next
            
            self.tail.next = node
            node.previous = self.tail
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
            if(self.head.next is not None):
                self.head.next.previous = None
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
            while current is not None:
                if current == node:
                    if current.previous is None:
                        self.head = node.next
                    else:
                        current.previous.next = current.next
                        current.next.previous = current.previous
                    if(current.next is None):
                        self.tail = current.previous
                    self.size -= 1
                    return
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