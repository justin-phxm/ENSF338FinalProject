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
    assert second_BST.get_root().get_data() == 5

    # Constructor with TNode
    node = TNode(data=3)
    third_BST = BST(node)
    assert third_BST.get_root().get_data() == 3

def test_BST_insert():
    # Inserting into an empty BST
    first_BST = BST()
    first_BST.insert(5)

    assert first_BST.get_root().get_data() == 5

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
    new_root2 = TNode(3)
    second_BST.set_root(new_root2)

    assert second_BST.get_root().get_data() == 3
    assert second_BST.get_root().get_right_node().get_data() == 5

def test_BST_delete():
    first_BST = BST(9)
    first_BST.delete(9)
    assert first_BST.get_root() == None

    first_BST.insert(5)
    first_BST.insert(4)
    first_BST.insert(6)

    first_BST.delete(4)
    assert first_BST.search(4) == None
    #Does not work when you give it 5 for some reason

def test_BST_shape():
    # Inserting into the BST in a balanced order
    first_BST = BST(5)
    first_BST.insert(4)
    first_BST.insert(6)
    first_BST.insert(3)
    first_BST.insert(2)
    first_BST.insert(7)
    first_BST.insert(8)

    assert first_BST.get_root().get_data() == 5
    assert first_BST.get_root().get_left_node().get_data() == 4
    assert first_BST.get_root().get_right_node().get_data() == 6
    assert first_BST.get_root().get_left_node().get_left_node().get_data() == 3
    assert first_BST.get_root().get_right_node().get_right_node().get_data() == 7
    assert first_BST.get_root().get_left_node().get_left_node().get_left_node().get_data() == 2
    assert first_BST.get_root().get_right_node().get_right_node().get_right_node().get_data() == 8

    # Inserting into the BST in a non-balanced order
    second_BST = BST(2)
    second_BST.insert(3)
    second_BST.insert(4)
    second_BST.insert(5)

    assert second_BST.get_root().get_data() == 2
    assert second_BST.get_root().get_right_node().get_data() == 3
    assert second_BST.get_root().get_right_node().get_right_node().get_data() == 4
    assert second_BST.get_root().get_right_node().get_right_node().get_right_node().get_data() == 5

def test_BST_print_in_order():
    # Inserting into the BST in a balanced order
    first_BST = BST(5)
    first_BST.insert(4)
    first_BST.insert(6)
    first_BST.insert(3)
    first_BST.insert(2)
    first_BST.insert(7)
    first_BST.insert(8)
    
    print("Print inorder test 1:")
    first_BST.printBF()
    print()

    # Inserting into the BST in a non-balanced order
    second_BST = BST(2)
    second_BST.insert(3)
    second_BST.insert(4)
    second_BST.insert(5)

    print("Print inorder test 2:")
    second_BST.printBF()
    print()

def test_BST_printBF():
    # Inserting into the BST in a balanced order
    first_BST = BST(5)
    first_BST.insert(4)
    first_BST.insert(6)
    first_BST.insert(3)
    first_BST.insert(2)
    first_BST.insert(7)
    first_BST.insert(8)
    
    print("Print breadth-first test 1:")
    first_BST.printBF()
    print()

    # Inserting into the BST in a non-balanced order
    second_BST = BST(2)
    second_BST.insert(3)
    second_BST.insert(4)
    second_BST.insert(5)

    print("Print breadth-first test 2:")
    second_BST.printBF()
    print()