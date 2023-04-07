
from dataStructures.nodes import TNode

class AVLTree:
    
    def __init__(self, data):
        self.balance = 0
        self.left_height = 0
        self.right_height = 0
        
        self.data = data
        self.left_node = None
        self.right_node = None
    
    def add(self, data):
        pass
