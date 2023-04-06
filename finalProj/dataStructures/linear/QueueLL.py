from SLL import SLL

# QueueLL
#   A stack implemented by extending SLL
class QueueLL(SLL):
    def insertHead(self, node):
        return

    def enqueue(self, node):
        enqueue = self.insertTail(node)

    def insert(self, node, index):
        return

    def sortedInsert(self, node):
        return
        
    def deleteHead(self):
        return
        
    def dequeue(self):
        returnHead = self.head
        super().deleteHead()
        return returnHead
    
    def delete(self, node):
        return
    
    def deleteTail(self):
        return
    
    def print(self):
        print("QueueLL length:", self.size)
        sortedStatus = "Sorted" if self.isSorted() else "Unsorted"
        print("QueueLL Sorted:", sortedStatus)
        print("QueueLL Content:", end="")
        temp = self.head
        for i in range(self.size):
            print(temp.data, end=" ")
            temp = temp.next
        print()