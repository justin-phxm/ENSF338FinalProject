from AVL import AVL
from TNode import TNode

def test_AVL_Constructors():
    # Default Constructor
    first_AVL = AVL()
    assert type(first_AVL) == AVL

    # Constructor with int
    second_AVL = AVL(5)
    assert second_AVL.get_root().get_data() == 5

    # Constructor with node
    node = TNode(3)
    third_AVL = AVL(node)
    assert third_AVL.get_root().get_data() == 3

def test_AVL_insert():
    # Inserting into an empty AVL
    first_AVL = AVL()
    first_AVL.insert(5)

    assert first_AVL.get_root().get_data() == 5

    # Inserting into an AVL with just a root node
    new_node = TNode(3)
    first_AVL.insert(new_node)

    assert first_AVL.search(3).get_data() == 3

def test_AVL_set_root():
    # Setting root of an empty AVL with an int
    first_AVL = AVL()
    first_AVL.set_root(5)

    assert first_AVL.get_root().get_data() == 5
 
    # Setting root of an empty AVL with a TNode
    second_AVL = AVL()
    new_root = TNode(5)
    second_AVL.set_root()
    
