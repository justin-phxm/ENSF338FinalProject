from SLL import SLL
from Node import Node
def test_SLL_Constructors():
    sll = SLL()
    assert sll.head == None
    assert sll.tail == None
    assert sll.size == 0
    myNode = Node(1)
    sll1 = SLL(myNode)
    assert sll1.head.data == 1
    assert sll1.tail.data == 1
    assert sll1.size == 1
def test_SLL_len():
    sll = SLL()
    assert len(sll) == 0
    myNode = Node(1)
    sll1 = SLL(myNode)
    assert len(sll1) == 1
def test_SLL_insertHead():
    sll = SLL()
    node1 = Node(1)
    sll.insertHead(node1)
    assert sll.head.data == 1
    assert sll.tail.data == 1
    assert sll.size == 1
    node2 = Node(2)
    sll.insertHead(node2)
    assert sll.head.data == 2
    assert sll.tail.data == 1
    assert sll.size == 2
def test_SLL_insertTail():
    sll = SLL()
    node1 = Node(1)
    sll.insertTail(node1)
    assert sll.head.data == 1
    assert sll.tail.data == 1
    assert sll.size == 1
    node2 = Node(2)
    sll.insertTail(node2)
    assert sll.head.data == 1
    assert sll.tail.data == 2
    assert sll.size == 2
def test_SLL_insert():
    # Test 1: Insert at head
    sll = SLL()
    node1 = Node(1)
    sll.insert(node1, 0)
    assert sll.head.data == 1
    assert sll.tail.data == 1
    assert sll.size == 1
    # Test 2: Insert at tail
    node2 = Node(2)
    sll.insert(node2, 1)
    assert sll.head.data == 1
    assert sll.tail.data == 2
    assert sll.size == 2
    # Test 3: Insert in middle
    node3 = Node(3)
    sll.insert(node3, 1)
    assert sll.head.data == 1
    assert sll.tail.data == 2
    assert sll.size == 3
    assert sll.head.next.data == 3
    assert sll.head.next.next.data == 2
    # Test 4: Insert at invalid index
    node4 = Node(4)
    exceptionRaised = False
    try:
        sll.insert(node4, -1)
    except:
        exceptionRaised = True
    assert exceptionRaised
    assert sll.head.data == 1
    assert sll.tail.data == 2
    assert sll.size == 3
    # Test 5: Insert at invalid index
    node5 = Node(5)
    exceptionRaised = False
    try:
        sll.insert(node5, 4)
    except:
        exceptionRaised = True
    assert exceptionRaised
    assert sll.head.data == 1
    assert sll.tail.data == 2
    assert sll.size == 3
    
def test_SLL_isSorted():
    # Test 1: Empty list
    sll = SLL()
    assert sll.isSorted() == True

    # Test 2: Single element list
    node1 = Node(1)
    sll.insertTail(node1)
    assert sll.isSorted() == True

    # Test 3: Sorted list
    node2 = Node(2)
    sll.insertTail(node2)
    assert sll.isSorted() == True

    # Test 4: Unsorted list
    node3 = Node(3)
    sll.insertHead(node3)
    assert sll.isSorted() == False

def test_SLL_sortedInsert():
    # Test 1: Empty list
    sll = SLL()
    node1 = Node(1)
    sll.sortedInsert(node1)
    assert sll.head.data == 1
    assert sll.tail.data == 1
    assert sll.size == 1

    # Test 2: Insert at tail
    node2 = Node(4)
    sll.sortedInsert(node2)
    assert sll.head.data == 1
    assert sll.tail.data == 4
    assert sll.size == 2

    # Test 3: Insert at head
    node3 = Node(1)
    sll.sortedInsert(node3)
    assert sll.head.data == 1
    assert sll.tail.data == 4
    assert sll.size == 3

    # Test 4: Insert in middle
    node4 = Node(3)
    sll.sortedInsert(node4)
    assert sll.head.data == 1
    assert sll.tail.data == 4
    assert sll.size == 4
    assert sll.head.next.data == 1
    assert sll.head.next.next.data == 3

def test_SLL_search():
    # Test 1: Empty list
    sll = SLL()
    node1 = Node(1)
    assert sll.search(node1) == None

    # Test 2: Single element list
    sll.insertTail(node1)
    assert sll.search(node1) == node1

    # Test 3: Multiple element list
    node2 = Node(2)
    sll.insertTail(node2)
    assert sll.search(node1) == node1
    assert sll.search(node2) == node2

    # Test 4: Not found
    node3 = Node(3)
    assert sll.search(node3) == None

def test_SLL_deleteHead():
    # Test 1: Empty list
    sll = SLL()
    sll.deleteHead()
    assert sll.head == None
    assert sll.tail == None
    assert sll.size == 0

    # Test 2: Single element list
    node1 = Node(1)
    sll.insertTail(node1)
    sll.deleteHead()
    assert sll.head == None
    assert sll.tail == None
    assert sll.size == 0

    # Test 3: Multiple element list
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    sll.insertTail(node2)
    sll.insertTail(node3)
    sll.insertTail(node4)
    sll.deleteHead()
    assert sll.head.data == 3
    assert sll.tail.data == 4
    assert sll.size == 2
def test_SLL_deleteTail():
    # Test 1: Empty list
    sll = SLL()
    sll.deleteTail()
    assert sll.head == None
    assert sll.tail == None
    assert sll.size == 0

    # Test 2: Single element list
    node1 = Node(1)
    sll.insertTail(node1)
    sll.deleteTail()
    assert sll.head == None
    assert sll.tail == None
    assert sll.size == 0

    # Test 3: Multiple element list
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    sll.insertTail(node2)
    sll.insertTail(node3)
    sll.insertTail(node4)
    sll.deleteTail()
    assert sll.head.data == 2
    assert sll.tail.data == 3
    assert sll.size == 2

def test_SLL_delete():
    # Test 1: Empty list
    sll = SLL()
    node1 = Node(1)
    sll.delete(node1)
    assert sll.head == None
    assert sll.tail == None
    assert sll.size == 0

    # Test 2: Single element list
    sll.insertTail(node1)
    sll.delete(node1)
    assert sll.head == None
    assert sll.tail == None
    assert sll.size == 0

    # Test 3: Multiple element list
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    sll.insertTail(node1)
    sll.insertTail(node2)
    sll.insertTail(node3)
    sll.insertTail(node4)
    sll.delete(node3)
    assert sll.head.data == 1
    assert sll.tail.data == 4
    assert sll.size == 3
    assert sll.head.next.data == 2
    assert sll.head.next.next.data == 4

    # Test 4: Not found
    node5 = Node(5)
    sll.delete(node5)
    assert sll.head.data == 1
    assert sll.tail.data == 4
    assert sll.size == 3
    assert sll.head.next.data == 2
    assert sll.head.next.next.data == 4
def test_SLL_sort():
    
    # Test 1: Empty list
    sll = SLL()
    sll.sort()
    assert sll.head == None
    assert sll.tail == None
    assert sll.size == 0

    # Test 2: Single element list
    node1 = Node(1)
    sll.insertTail(node1)
    sll.sort()
    assert sll.head.data == 1
    assert sll.tail.data == 1
    assert sll.size == 1

    # Test 3: Multiple element list
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    sll.insertTail(node4)
    sll.insertTail(node3)
    sll.insertTail(node2)
    sll.sort()
    assert sll.head.data == 1
    assert sll.tail.data == 4
    assert sll.size == 4
    assert sll.head.next.data == 2
    assert sll.head.next.next.data == 3
    assert sll.head.next.next.next.data == 4

def test_SLL_clear():
    # Test 1: Empty list
    sll = SLL()
    sll.clear()
    assert sll.head == None
    assert sll.tail == None
    assert sll.size == 0

    # Test 2: Single element list
    node1 = Node(1)
    sll.insertTail(node1)
    sll.clear()
    assert sll.head == None
    assert sll.tail == None
    assert sll.size == 0

    # Test 3: Multiple element list
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    sll.insertTail(node2)
    sll.insertTail(node3)
    sll.insertTail(node4)
    sll.clear()
    assert sll.head == None
    assert sll.tail == None
    assert sll.size == 0