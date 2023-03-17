from dataStructures.nodes.Node import Node
class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        else:
            current = self.head
            for i in range(index):
                current = current.next
            return current.data

    def __setitem__(self, index, data):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        else:
            current = self.head
            for i in range(index):
                current = current.next
            current.data = data

    def __delitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        else:
            if index == 0:
                self.head = self.head.next
            else:
                current = self.head
                for i in range(index - 1):
                    current = current.next
                current.next = current.next.next
            self.size -= 1

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insert(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        else:
            node = Node(data)
            if index == 0:
                node.next = self.head
                self.head = node
            else:
                current = self.head
                for i in range(index - 1):
                    current = current.next
                node.next = current.next
                current.next = node
            self.size += 1

    def remove(self, data):
        if self.head is None:
            raise ValueError("Value not found")
        else:
            current = self.head
            previous = None
            while current is not None:
                if current.data == data:
                    if previous is None:
                        self.head = current.next
                    else:
                        previous.next = current.next
                    self.size -= 1
                    return
