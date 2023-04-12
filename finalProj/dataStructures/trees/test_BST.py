from BST import BST
from TNode import TNode

def test_BST_Constructors():
    first_BST = BST()
    assert type(first_BST) == BST

    second_BST = BST(5)
    assert second_BST.search(5).get_data() == 5

def test_BST_insert():
    first_BST = BST()
    first_BST.insert(5)

    new_node = TNode(3)
    first_BST.insert(new_node)

    assert first_BST.search(5).get_data() == 5
    assert first_BST.search(3).get_data() == 3

def test_BST_set_root():
    pass

def test_BST_delete():
    pass

def test_BST_print_in_order():
    pass

def test_BST_printBF():
    pass