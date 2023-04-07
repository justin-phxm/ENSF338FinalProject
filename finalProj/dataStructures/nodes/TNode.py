class TNode:
    def __init__(self, data=None):
        self.balance = 0
        self.left_height = 0
        self.right_height = 0
        
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent_node = None
        