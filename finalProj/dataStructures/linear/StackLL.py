# from dataStructures.nodes.Node import Node
from SLL import SLL

# StackLL
#   A stack implemented by extending SLL
class StackLL(SLL):
    # push(node)
    #   inserts a node at the head of the list
    def push(self, node):
        push = self.insertHead(node)
        
    def insertTail(self, node):
        return 

    def insert(self, node, index):
        return

    def sortedInsert(self, node):
        return
        
    def deleteHead(self):
        return
    
    # pop()
    #   removes and returns the tail of the list
    def pop(self):
        returnHead = self.head
        super().deleteHead()
        return returnHead
    
    def deleteTail(self):
        return
    def delete(self, node):
        return

    def print(self):
        print("StackLL length:", self.size)
        sortedStatus = "Sorted" if self.isSorted() else "Unsorted"
        print("StackLL Sorted:", sortedStatus)
        print("StackLL Content:", end="")
        temp = self.head
        for i in range(self.size):
            print(temp.data, end=" ")
            temp = temp.next
        print()