# import sys
# sys.path.insert(0, "..")
# from dataStructures.nodes.TNode import TNode
# from dataStructures.trees.BST import BST

from TNode import TNode
from BST import BST

def test_BST_Constructors():
    # Default constructor
    first_BST = BST()
    assert type(first_BST) == BST

    # Constructor with int
    second_BST = BST(5)
    assert second_BST.search(5).get_data() == 5

    # Constructor with TNode
    node = TNode(data=3)
    third_BST = BST(node)
    assert third_BST.search(3).get_data() == 3

def test_BST_insert():
    # Inserting into an empty BST
    first_BST = BST()
    first_BST.insert(5)

    assert first_BST.search(5).get_data() == 5

    # Inserting into a BST with just a root node
    new_node = TNode(3)
    first_BST.insert(new_node)

    assert first_BST.search(3).get_data() == 3

def test_BST_set_root():
    # Setting root of an empty BST with an int
    first_BST = BST()
    first_BST.set_root(5)

    assert first_BST.get_root().get_data() == 5

    # Setting root of an empty BST with a TNode
    second_BST = BST()
    new_root = TNode(5)
    second_BST.set_root(new_root)

    assert second_BST.get_root().get_data() == 5

    # Setting root of a non-empty BST
    

def test_BST_delete():
    pass

def test_BST_print_in_order():
    pass

def test_BST_printBF():
    pass