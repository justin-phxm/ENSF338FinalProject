from TNode import TNode

class BST:

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
        
        parent = None
        current = self.root
        while current != None:
            parent = current
            if new_node.get_data() <= current.get_data():
                current = current.get_left_node()
            else:
                current = current.get_right_node()
        
        if self.root == None:
            self.root = new_node
        elif new_node.get_data() <= parent.get_data():
            parent.set_left_node(new_node)
            parent.get_left_node().set_parent_node(parent)
        else:
            parent.set_right_node(new_node)
            parent.get_right_node().set_parent_node(parent)
        
        

    
    # finds the node with val as data and deletes it,
    # if not found prints a statement that the value is not in the tree
    def delete(self, value):
        current = self.root
        parent = None

        while current != None:
            
            # The value was found and now will be deleted
            if value == current.get_data():
                # Case 1: Where the node to be deleted is a leaf node
                if current.get_left_node() == None and current.get_right_node() == None:
                    if current == parent.get_left_node():
                        parent.set_left_node(None)
                    else:
                        parent.set_right_node(None)

                # Case 2: Where the node to be deleted has only one child
                elif current.get_left_node() == None or current.get_right_node() == None:
                    if current == parent.get_left_node():
                        if current.get_left_node() == None:
                            parent.set_left_node(current.get_right_node())
                        else:
                            parent.set_left_node(current.get_left_node())
                    else:
                        if current.get_left_node() == None:
                            parent.set_right_node(current.get_right_node())
                        else:
                            parent.set_right_node(current.get_left_node())
                
                # Case 3: Where the node to be deleted has two children
                else:
                    pass

            elif value <= current.get_data():
                current = current.get_left_node()
            else:
                current = current.get_right_node()
            parent = current.get_parent_node()
            
        pass

    # searches for the node with val as data and returns it
    # or returns null if not found
    def search(self, value):
        current = self.root
        while current != None:
            parent = self.root
            if value == parent.get_data():
                return parent
            elif value <= parent.get_data():
                current = current.get_left_node()
            else:
                current = current.get_right_node()
        return None

    # prints the content data of the tree in ascending order
    def print_in_order(self, current = True):
        if current != None:
            self.print_in_order(self.root.get_left_node())
            print(current.get_data())
            self.print_in_order(self.root.get_right_node())


    # prints the content of the tree in Breadth-First order, 
    # each level of the tree will be printed on a separate line
    def printBF(self):
        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            current = queue.pop(0) # Remove from front of queue
            print(current.get_data())
            if current.left is not None:
                queue.append(current.get_left_node())
            if current.right is not None:
                queue.append(current.get_right_node())