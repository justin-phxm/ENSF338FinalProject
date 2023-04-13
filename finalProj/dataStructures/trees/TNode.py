class TNode:

    def __init__(self, data=None, balance=0,height=1, P=None, L=None, R=None):
        self.data = data
        self.balance = balance
        self.height = height
        self.parent_node = P
        self.left_node = L
        self.right_node = R

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_balance(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance
    
    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def set_parent_node(self, parent):
        self.parent_node = parent
    
    def get_parent_node(self):
        return self.parent_node
    
    def set_left_node(self, left):
        self.left_node = left

    def get_left_node(self):
        return self.left_node
    
    def set_right_node(self, right):
        self.right_node = right

    def get_right_node(self):
        return self.right_node

    # prints the node information to console in a user friendly format
    def print(self, ):
        pass
    
    # returns the data member as a string (will be used for the tree prints)
    def toString(self):
        pass

    # Finds the balance of a node
    def find_balance(self):
        left_height = 0
        right_height = 0
        current_left = self.left_node
        current_right = self.right_node
        while current_left != None:
            left_height += 1
            if current_left.left_node != None:
                current_left = current_left.left


        pass

