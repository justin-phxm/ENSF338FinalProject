# from dataStructures.nodes.Node import Node
from Node import Node
class CSLL:
    # CSLL Constructor
    #   creates a circular singly linked list
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.size = 0 if node==None else 1
        if(node is not None):
            node.next = self.head
    
    # __len__()
    #   returns the size of the list
    def __len__(self):
        return self.size
    
    # insertHead()
    #   inserts a node at the head of the list
    def insertHead(self, node):
        if self.head is None:
            self.head = node
            node.next = self.head
            self.tail = node
        else:
            node.next = self.head
            self.head = node
            self.tail.next = node
        self.size += 1

    # insertTail()
    #   inserts a node at the tail of the list
    def insertTail(self, node):
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        node.next = self.head
        self.size += 1
    
    # insert()
    #   inserts a node at the given index
    def insert(self, node, index):
        if (index < 0 or index > self.size):
            print("Index out of range"  )
            raise Exception
        else:
            if index == 0:
                if(self.head == None):
                    self.tail = node
                    self.head = node
                    node.next = self.head
                else:
                    self.tail.next = node
                    node.next = self.head
                    self.head = node
            else:
                current = self.head
                for i in range(index - 1):
                    current = current.next
                node.next = current.next
                current.next = node
                if(node.next == self.head):
                    self.tail = node
            self.size += 1

    # isSorted()
    #   returns True if the list is sorted in ascending order
    #   returns False otherwise
    def isSorted(self):
        current = self.head
        for i in range(self.size - 1):
            # if current.next is not self.head:
            if current.data > current.next.data:
                return False
            current = current.next
        return True 
    
    # sortedInsert()
    #   inserts a node into the list in ascending order
    #   if the list is not sorted, it will sort the list first
    def sortedInsert(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            node.next = self.head
            # self.size += 1
        else:
            current = self.head
            for i in range(self.size - 1):
                # if current.next is not None:
                if current.data > current.next.data:
                    self.sort()
                current = current.next
            current = self.head
            previous = None
            for i in range(self.size):
                if current.data > node.data:
                    if previous is None:
                        node.next = current
                        self.head = node
                        self.last.next = node
                    else:
                        previous.next = node
                        node.next = current
                    self.size += 1
                    return
                previous = current
                current = current.next
            previous.next = node
            node.next = self.head
            self.tail = node
        self.size += 1

    # search()
    #   searches for a node in the list
    def search(self, node):
        if self.head is None:
            print("List is empty")
            return None
        else:
            current = self.head
            for i in range(self.size):
                if current == node:
                    return node
                current = current.next
            return None
    
    # deleteHead()
    #   deletes the head of the list
    def deleteHead(self):
        if self.head is None:
            print("List is empty")
        else:
            if(self.size == 1):
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            self.size -= 1
    
    # deleteTail()
    #   deletes the tail of the list
    def deleteTail(self):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            previous = None
            if(self.size == 1):
                self.head = None
                self.tail = None
            else:
                for i in range(self.size - 1):
                    previous = current
                    current = current.next
                if previous is None:
                    self.head = None
                    self.tail = None
                else:
                    previous.next = None
                    self.tail = previous
                    self.tail.next = self.head
            self.size -= 1

    # delete()
    #   deletes a node from the list
    def delete(self, node):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            previous = None
            for i in range(self.size):
                if current == node:
                    if previous is None:
                        if(self.size == 1):
                            self.head = None
                            self.tail = None
                        else:
                            if current.next == self.tail:
                                self.tail.next = self.tail
                            self.head = current.next
                    else:
                        previous.next = current.next
                    self.size -= 1
                    return
                previous = current
                current = current.next
    
    # sort()
    #   sorts the list in ascending order
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
    
    # clear()
    #   clears the list
    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    # print()
    #   prints the list
    def print(self):
        print("SLL length:", self.size)
        sortedStatus = "Sorted" if self.isSorted() else "Unsorted"
        print("SLL Sorted:", sortedStatus)
        print("SLL Content:", end="")
        temp = self.head
        for i in range(self.size):
            print(temp.data, end=" ")
            temp = temp.next
        print()