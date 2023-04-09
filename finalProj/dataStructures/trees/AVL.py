
from TNode import TNode
from BST import BST

class AVLTree(BST):
    
    def __init__(self, data):
        self.balance = 0
        self.left_height = 0
        self.right_height = 0
        
        self.data = data
        self.left_node = None
        self.right_node = None
    
    
    
