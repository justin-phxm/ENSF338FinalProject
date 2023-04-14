import sys
sys.path.insert(0, "..")
from nodes.TNode import TNode
from trees.BST import BST

class AVL(BST):
    
    def __init__(self, data=None):
        if data == None:
            self.root = None

        if (type(data) == int):
            self.root = TNode(data=data)
        else:
            self.root = data

    # Not complete, have to balance tree
    def set_root(self, data):
        super().set_root(data)

    def get_root(self):
        return self.root

    # Not complete, have to balance tree
    # Override
    def insert(self, data):
        if (type(data) == int):
            new_node = TNode(data)
        else:
            new_node = data
        
        self.root = self._insert_then_balance(self.root, new_node)
        
        
    # This is a helper function that is meant
    # to balance the BST into an AVL Tree
    def _insert_then_balance(self, curr_node, inserting_node):
        # Inserting the new node into the right spot
        if curr_node == None:
            return inserting_node
        elif inserting_node.get_data() <= curr_node.get_data():
            curr_node.set_left_node(self._insert_then_balance(curr_node.get_left_node(), inserting_node))
        else:
            curr_node.set_right_node(self._insert_then_balance(curr_node.get_right_node(), inserting_node))
        
        # Changing the height of the current node (it starts at the bottom of the tree)
        curr_node.set_height(1 + max(self._find_height(curr_node.get_left_node()), self._find_height(curr_node.get_right_node())))

        # After updating the height, it becomes easier to find the balance of the node
        curr_node.set_balance(self._find_balance(curr_node))

        # Here we look at different cases and change the shape of the tree
        # depending on the balance and the value of the inserting node

        # Left Left Case ()
        if curr_node.get_balance() > 1 and inserting_node.get_data() < curr_node.get_left_node().get_data():
            return self._right_rotation(curr_node)
        
        # Left Right Case ()
        if curr_node.get_balance() > 1 and inserting_node.get_data() > curr_node.get_left_node().get_data():
            curr_node.set_left_node(self._left_rotation(curr_node.get_left_node()))
            return self._right_rotation(curr_node)
        
        # Right Right Case ()
        if curr_node.get_balance() < -1 and inserting_node.get_data() > curr_node.get_left_node().get_data():
            return self._left_rotation(curr_node)

        # Right Left Case ()
        if curr_node.get_balance() < -1 and inserting_node.get_data() < curr_node.get_right_node().get_data():
            curr_node.set_right_node(self._right_rotation(curr_node.get_right_node()))
            return self._left_roation(curr_node)

        return curr_node                               

    # This is a helper function that is meant
    # to find the height of a node
    def _find_height(self, node):
        if node == None:
            return 0
        else:
            return node.get_height()

    # This is a helper function that is meant
    # to find the balance of a node
    def _find_balance(self, node):
        if node == None:
            return 0
        else:
            return self._find_height(node.get_right_node()) - self._find_height(node.get_left_node())
         
    def _right_rotation(self, node):
        new_root = node.get_left_node()
        node.set_left_node(new_root.get_right_node())
        new_root.set_right_node(node)

        node.set_height(1 + max(self._find_height(node.get_left_node()), self._find_height(node.get_right_node())))
        new_root.set_height(1 + max(self._find_height(new_root.get_left_node(), self._find_height(new_root.get_right_node()))))

        return new_root
    
    def _left_rotation(self, node):
        new_root = node.get_right_node()
        node.set_right_node(new_root.get_left_node())
        new_root.set_left_node(node)

        node.set_height(1 + max(self._find_height(node.get_left_node()), self._find_height(node.get_right_node())))
        new_root.set_height(1 + max(self._height(new_root.get_left_node()), self._height(new_root.get_right_node())))

        return new_root

    #TODO Bonus
    # Not complete, have to balance tree
    def delete(self, value):
        super().delete(value)

    def search(self, value):
        return super().search(value)
    
    def print_in_order(self, current=True):
        return super().print_in_order(current)
    
    def printBF(self):
        super().printBF()

    