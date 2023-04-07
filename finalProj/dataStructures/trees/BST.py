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
        pass

    def get_root(self):
        pass

    # If data is int, creates a new node with data val to be inserted into the tree
    # If data is TNode, inserts the node passed as argument into the tree
    def insert(data):
        if (type(data) == int):
            pass
        else:
            pass
    
    # finds the node with val as data and deletes it,
    # if not found prints a statement that the value is not in the tree
    def delete(self, value):
        pass

    # searches for the node with val as data and returns it
    # or returns null if not found
    def search(self, value):
        pass

    # prints the content data of the tree in ascending order
    def print_in_order(self):
        pass

    # prints the content of the tree in Breadth-First order, 
    # each level of the tree will be printed on a separate line
    def printBF(self):
        pass