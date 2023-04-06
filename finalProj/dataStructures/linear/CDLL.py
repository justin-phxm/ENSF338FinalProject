# from dataStructures.nodes.Node import Node
# from DNode import DNode
from DLL import DLL
class CDLL(DLL):
    # CDLL Constructor
    #   creates a circular singly linked list
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.size = 0 if node==None else 1
        if(node is not None):
            node.next = self.head
            node.previous = self.tail
    
    # insertHead()
    #   inserts a node at the head of the list
    def insertHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            node.next = self.head
            node.previous = self.tail
        else:
            node.next = self.head
            node.previous = self.tail
            self.head = node
            self.tail.next = node
            self.tail.previous = node
        self.size += 1

    # insertTail()
    #   inserts a node at the tail of the list
    def insertTail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            node.next = self.head
            node.previous = self.tail
        else:
            node.next = self.head
            node.previous = self.tail
            self.tail.next = node
            self.head.previous = node
        self.tail = node
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
                    self.head = node
                    self.tail = node
                    node.next = self.head
                    node.previous = self.tail
                else:
                    node.next = self.head
                    node.previous = self.tail
                    self.tail.next = node
                    self.head.previous = node
                    self.head = node
            else:
                current = self.head
                for i in range(index - 1):
                    current = current.next
                node.next = current.next
                node.previous = current
                node.next.previous = node
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
            node.previous = self.tail
        else:
            if(self.isSorted() == False):
                self.sort()
            current = self.head
            previous = None
            for i in range(self.size):
                if current.data > node.data:
                    if previous is None:
                        node.next = current
                        node.previous = self.tail
                        self.tail.next = node
                        self.head.previous = node
                        self.head = node
                    else:
                        previous.next = node
                        current.previous = node
                        node.next = current
                        node.previous = previous
                    self.size += 1
                    return
                previous = current
                current = current.next
            # Inserts into the tail
            previous.next = node
            current.previous = node
            node.next = self.head
            node.previous = previous
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
                self.head.previous = self.tail
                self.tail.next = self.head
            self.size -= 1
    
    # deleteTail()
    #   deletes the tail of the list
    def deleteTail(self):
        if self.head is None:
            print("List is empty")
        else:
            if(self.size == 1):
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.previous
                self.tail.next = self.head
                self.head.previous = self.tail
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
                                self.tail.previous = self.tail
                                self.tail.next = self.tail
                            self.tail.next = current.next
                            current.next.previous = self.tail
                            self.head = current.next
                    else:
                        previous.next = current.next
                        current.next.previous = previous
                        if current == self.tail:
                            self.tail = previous
                    self.size -= 1
                    return
                previous = current
                current = current.next
            print("Node not found")
    
    # print()
    #   prints the list
    def print(self):
        print("CDLL length:", self.size)
        sortedStatus = "Sorted" if self.isSorted() else "Unsorted"
        print("CDLL Sorted:", sortedStatus)
        print("CDLL Content:", end="")
        temp = self.head
        for i in range(self.size):
            print(temp.data, end=" ")
            temp = temp.next
        print()