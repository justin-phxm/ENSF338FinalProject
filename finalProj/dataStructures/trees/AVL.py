import sys
sys.path.insert(0, "..")
from nodes.TNode import TNode
from trees.BST import BST

class AVL(BST):
    
    def __init__(self, data=None):
        if data == None:
            self.root = None

        if data == type(data):
            self.root = TNode(data=data)
        else:
            self.root = data

    # Not complete, have to balance tree
    def set_root(self, data):
        super().set_root(data)

    def get_root(self):
        return self.root()
    
    # Not complete, have to balance tree
    # Override
    def insert(self, data):
        movements = []
        if (type(data) == int):
            new_node = TNode(data)
        else:
            new_node = data

        if self.root == None:
            self.root = new_node
            new_node.set_balance(0)
            return

        
        current = self.root

        while current != None:
            parent = current

            if new_node.get_data() <= current.get_data():
                current = current.get_left_node()
                movements.append('left')
            else:
                current = current.get_right_node()
                movements.append('right')

        if new_node.get_data() <= parent.get_data():
            parent.set_left_node(new_node)
            new_node.set_parent_node(parent)
        else:
            parent.set_right_node(new_node)
            new_node.set_parent_node(parent)
        self._balance_tree(new_node, movements)

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

    # This is a helper function that is meant
    # to balance the BST into an AVL Tree
    def _balance_tree(self, inserted_node, movements):
        current = self.root
        ancestor = None # Parent node of the pivot node
        pivot = None    # Most recently encountered node with a balance of not 0
        son = None      # Child node of the pivot node

        # Going from root to inserted node to assign ancestor, pivot, and son nodes
        for direction in movements:
            assigned_pivot = False
            if current.get_balance() != 0:
                if current == self.root:
                    pivot = current
                else:
                    pivot = current
                    ancestor = pivot.get_parent_node()
                assigned_pivot = True

            if direction == "left":
                current = current.get_left_node()
            else:
                current = current.get_left_node()
            if assigned_pivot:
                son = current

        # If case 1: 'No pivot, no balance updates' occurs, we can just return
        if pivot == None:
            return
        balancing_node = inserted_node
        while balancing_node != pivot:
            self._find_balance(balancing_node)
            balancing_node = balancing_node.get_parent_node()

    # This is a helper function that is meant
    # to find the balance of a node
    def _find_balance(self, node):
        left_height = 0
        right_height = 0
        
        if node.get_left_node() == None and node.get_right_node() == None:
            node.set_balance(0)
            return
        
        if node.get_left_node() != None:
            left_height += 1
            self._find_balance(node.get_left_node())
        
        if node.get_right_node() != None:
            right_height += 1
            self._find_balance(node.get_right_node())

        node.set_balance(right_height - left_height)