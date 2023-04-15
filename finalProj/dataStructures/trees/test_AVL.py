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
    assert first_AVL.get_root().get_balance() == 0

    # Inserting into an AVL with just a root node
    new_node = TNode(3)
    first_AVL.insert(new_node)

    assert first_AVL.search(3).get_data() == 3
    
    
    # Inserting into an AVL with no rotation or pivot (case 1)
    first_AVL = AVL()
    first_AVL.insert(4)
    first_AVL.insert(2)
    first_AVL.insert(7)
    first_AVL.insert(1)
    first_AVL.insert(5)
    first_AVL.insert(10)

    first_AVL.insert(8)

    assert first_AVL.get_root().get_left_node().get_left_node().get_data() == 1
    assert first_AVL.get_root().get_left_node().get_data() == 2
    assert first_AVL.get_root().get_data() == 4
    assert first_AVL.get_root().get_right_node().get_data() == 7
    assert first_AVL.get_root().get_right_node().get_left_node().get_data() == 5
    assert first_AVL.get_root().get_right_node().get_right_node().get_data() == 10
    assert first_AVL.get_root().get_right_node().get_right_node().get_left_node().get_data() == 8

    # Inserting into an AVL with no rotation but with has a pivot (case 2)
    second_AVL = AVL()
    second_AVL.insert(3)
    second_AVL.insert(2)
    second_AVL.insert(4)
    second_AVL.insert(5)
    
    second_AVL.insert(1)

    assert second_AVL.get_root().get_data() == 3
    assert second_AVL.get_root().get_balance() == 0

    assert second_AVL.get_root().get_left_node().get_data() == 2
    assert second_AVL.get_root().get_left_node().get_balance() == -1

    assert second_AVL.get_root().get_left_node().get_left_node().get_data() == 1
    assert second_AVL.get_root().get_left_node().get_left_node().get_balance() == 0

    assert second_AVL.get_root().get_right_node().get_data() == 4
    assert second_AVL.get_root().get_right_node().get_balance() == 1

    assert second_AVL.get_root().get_right_node().get_right_node().get_data() == 5
    assert second_AVL.get_root().get_right_node().get_right_node().get_balance() == 0

    # Inserting into an AVL in with a rotation (case 3a: outside subtree)
    third_AVL = AVL()
    third_AVL.insert(60)
    third_AVL.insert(40)
    third_AVL.insert(80)
    third_AVL.insert(20)
    third_AVL.insert(50)
    third_AVL.insert(95)
    third_AVL.insert(10)
    third_AVL.insert(30)

    third_AVL.insert(5)
    print("AVL Print BF")
    third_AVL.printBF()
    print()
    assert third_AVL.get_root().get_data() == 60
    assert third_AVL.get_root().get_balance() == -1

    assert third_AVL.get_root().get_left_node().get_data() == 20
    # assert third_AVL.get_root().get_left_node().get_balance() == 0

    assert third_AVL.get_root().get_right_node().get_data() == 80
 #   assert third_AVL.get_root().get_right_node().get_balance() == 1

    assert third_AVL.get_root().get_left_node().get_left_node().get_data() == 10
 #   assert third_AVL.get_root().get_left_node().get_left_node().get_balance() == -1

    assert third_AVL.get_root().get_left_node().get_right_node().get_data() == 40
 #   assert third_AVL.get_root().get_left_node().get_right_node().get_balance() == 0

    assert third_AVL.get_root().get_right_node().get_right_node().get_data() == 95
  #  assert third_AVL.get_root().get_right_node().get_right_node().get_balance() == 0

    assert third_AVL.get_root().get_left_node().get_left_node().get_left_node().get_data() == 5 
  #  assert third_AVL.get_root().get_left_node().get_left_node().get_left_node().get_balance() == 0

    assert third_AVL.get_root().get_left_node().get_right_node().get_left_node().get_data() == 30
  #  assert third_AVL.get_root().get_left_node().get_right_node().get_left_node().get_balance() == 0

    assert third_AVL.get_root().get_left_node().get_right_node().get_right_node().get_data() == 50
  #  assert third_AVL.get_root().get_left_node().get_right_node().get_right_node().get_balance() == 0

    # Inserting into an AVL in with a rotation (case 3b: inside subtree)
    fourth_AVL = AVL()
    fourth_AVL.insert(2)
    fourth_AVL.insert(1)
    fourth_AVL.insert(6)
    fourth_AVL.insert(4)
    fourth_AVL.insert(7)

    fourth_AVL.insert(5)

    print("AVL Print BF")
    fourth_AVL.printBF()
    print()

    assert fourth_AVL.get_root().get_data() == 4
    # assert fourth_AVL.get_root().get_balance() == 0

    assert fourth_AVL.get_root().get_left_node().get_data() == 2
    # assert fourth_AVL.get_root().get_left_node().get_balance() == -1

    assert fourth_AVL.get_root().get_right_node().get_data() == 6
    # assert fourth_AVL.get_root().get_right_node().get_balance() == 0

    assert fourth_AVL.get_root().get_left_node().get_left_node().get_data() == 1    
    # assert fourth_AVL.get_root().get_left_node().get_left_node().get_balance() == 0

    assert fourth_AVL.get_root().get_right_node().get_left_node().get_data() == 5
    # assert fourth_AVL.get_root().get_right_node().get_left_node().get_balance() == 0

    assert fourth_AVL.get_root().get_right_node().get_right_node().get_data() == 7   
    # assert fourth_AVL.get_root().get_right_node().get_right_node().get_balance() == 0

def test_AVL_set_root():
    # Setting root of an empty AVL with an int
    first_AVL = AVL()
    first_AVL.set_root(5)

    assert first_AVL.get_root().get_data() == 5
 
    # Setting root of an empty AVL with a TNode
    second_AVL = AVL()
    new_root = TNode(5)
    second_AVL.set_root(new_root)

    assert second_AVL.get_root().get_data() == 5

    # Setting root of a non-empty AVL
    new_root2 = TNode(3)
    second_AVL.set_root(new_root2)

    assert second_AVL.get_root().get_data() == 3
    assert second_AVL.get_root().get_right_node().get_data() == 5
    
