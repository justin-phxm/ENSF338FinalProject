from BST import BST
from TNode import TNode

def test_BST_Constructors():
    first_BST = BST()
    assert type(first_BST.get_root()) == TNode

    second_BST = BST(5)
    assert first_BST.search(5).get_data() == 5