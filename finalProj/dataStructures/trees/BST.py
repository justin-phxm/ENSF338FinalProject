from dataStructures.nodes import TNode

class BSTree:

    # Overloaded constructor
    # Default Constructor initializes root to null
    # BST(int data) creates a TNode with it as the root
    # BST(TNode data) uses the given TNode as the root of the tree
    def __init__(self, data=None):
        
        if (data == None or type(data) == int):
            self.root = TNode(data)

        else:
            self.root = data

    def set_root(self, data):
        if self.root == None:
            if (type(data) == int):
                self.root = TNode(data)
            else:
                self.root = data
        else:
            # TODO Must change the data field of the root
            # and change the structure of the tree accordingly
            pass

    def get_root(self):
        return self.root

    # If data is int, creates a new node with data val to be inserted into the tree
    # If data is TNode, inserts the node passed as argument into the tree
    def insert(self, data):
        if (type(data) == int):
            new_node = TNode(data)
        else:
            new_node = data
        
        parent_node = None
        current_node = self.root
        while current_node != None:
            parent_node = current_node
            if new_node.data <= current_node.data:
                current_node = current_node.left_node
            else:
                current_node = current_node.right_node
        
        if self.root == None:
            self.root = new_node
        elif new_node.data <= parent_node.data:
            parent_node.left_node = new_node
        else:
            parent_node.right_node = new_node
        

    
    # finds the node with val as data and deletes it,
    # if not found prints a statement that the value is not in the tree
    def delete(self, value):
        current_node = self.root
        parent_node = None

        while current_node != None:
            parent_node = current_node
            if value == current_node.data:
                pass
            elif value <= current_node.data:
                current_node = current_node.left
        pass

    # searches for the node with val as data and returns it
    # or returns null if not found
    def search(self, value):
        current_node = self.root
        while current_node != None:
            parent_node = self.root
            if value == parent_node.data:
                return parent_node
            elif value <= parent_node.data:
                current_node = current_node.left_node
            else:
                current_node = current_node.right_node
        return None

    # prints the content data of the tree in ascending order
    def print_in_order(self):
        pass

    # prints the content of the tree in Breadth-First order, 
    # each level of the tree will be printed on a separate line
    def printBF(self):
        pass