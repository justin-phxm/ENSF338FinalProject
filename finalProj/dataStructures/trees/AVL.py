
from TNode import TNode
from BST import BST

class AVLTree(BST):
    
    def __init__(self, data=None):
        if data == None or type(data):
            self.root = TNode(data)
        else:
            self.root = data

    # Not complete, have to balance tree
    def set_root(self, data):
        super().set_root(data)

    def get_root(self):
        return self.root()
    
    # Not complete, have to balance tree
    def insert(self, data):
        super().insert(data)

    # Not complete, have to balance tree
    def delete(self, value):
        super().delete(value)

    def search(self, value):
        return super().search(value)
    
    def print_in_order(self, current=True):
        return super().print_in_order(current)
    
    def printBF(self):
        super().printBF()
    
    

    
    
    
