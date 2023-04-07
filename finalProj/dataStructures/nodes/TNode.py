class TNode:

    
    def __init__(self, data=None, balance=None, P=None, L=None, R=None):
        self.balance = balance
        self.left_height = 0
        self.right_height = 0
        
        self.data = data
        self.left_node = L
        self.right_node = R
        self.parent_node = P

    def set_data(self, new_data):
        pass

    def get_data(self):
        pass
    
    # prints the node information to console in a user friendly format
    def print(self, ):
        pass
    
    # returns the data member as a string (will be used for the tree prints)
    def toString(self):
        pass

