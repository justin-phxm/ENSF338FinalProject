from CSLL import CSLL
from Node import Node

def test_csll_Constructors():
    # Test 1: Default constructor
    csll = CSLL()
    assert csll.head == None
    assert csll.size == 0

    # Test 2: Constructor with node
    myNode = Node(1)
    csll1 = CSLL(myNode)
    assert csll1.head.data == 1
    assert csll1.size == 1
    assert csll1.head.next == csll1.head

def test_csll_len():
    # Test 1: Default constructor
    csll = CSLL()
    assert len(csll) == 0
    myNode = Node(1)

    # Test 2: Constructor with node
    csll1 = CSLL(myNode)
    assert len(csll1) == 1

def test_csll_insertHead():
    # Test 1: Insert at head
    csll = CSLL()
    node1 = Node(1)
    csll.insertHead(node1)
    assert csll.head.data == 1
    assert csll.size == 1
    assert csll.head.next == csll.head

    # Test 2: Insert new Node at head
    node2 = Node(2)
    csll.insertHead(node2)
    assert csll.head.data == 2
    assert csll.size == 2
    assert csll.head.next == node1
    assert csll.head.next.next == csll.head

    # Test 3: Insert new head in list with 2 nodes
    node3 = Node(3)
    csll.insertHead(node3)
    assert csll.head.data == 3
    assert csll.size == 3
    assert csll.head.next == node2
    assert csll.head.next.next == node1
    assert csll.head.next.next.next == csll.head
    
def test_csll_insertTail():
    # Test 1: Insert in empty list
    csll = CSLL()
    node1 = Node(1)
    csll.insertTail(node1)
    assert csll.head.data == 1
    assert csll.tail.data == 1
    assert csll.size == 1
    assert csll.head.next == csll.head

    # Test 2: Insert at tail
    node2 = Node(2)
    csll.insertTail(node2)
    assert csll.head.data == 1
    assert csll.tail.data == 2
    assert csll.size == 2
    assert csll.head.next == node2
    assert csll.head.next.next == csll.head

    # Test 3: Insert at tail in list with 2 nodes
    node3 = Node(3)
    csll.insertTail(node3)
    assert csll.head.data == 1
    assert csll.tail.data == 3
    assert csll.size == 3
    assert csll.head.next == node2
    assert csll.head.next.next == node3
    assert csll.head.next.next.next == csll.head

def test_csll_insert():
    # Test 1: Insert at head
    csll = CSLL()
    node1 = Node(1)
    csll.insert(node1, 0)
    assert csll.head.data == 1
    assert csll.size == 1
    assert csll.tail.data == 1

    # Test 2: Insert at tail
    node2 = Node(2)
    csll.insert(node2, 1)
    assert csll.head.data == 1
    assert csll.size == 2
    assert csll.tail.data == 2
    
    # Test 3: Insert in middle
    node3 = Node(3)
    csll.insert(node3, 1)
    assert csll.head.data == 1
    assert csll.tail.data == 2
    assert csll.size == 3
    assert csll.head.next.data == 3
    assert csll.head.next.next.data == 2
    assert csll.head.next.next.next == csll.head
  
    # Test 4: Insert at head in list with 3 nodes
    node4 = Node(4)
    csll.insert(node4, 0)
    assert csll.head.data == 4
    assert csll.tail.data == 2
    assert csll.size == 4
    assert csll.head.next.data == 1
    assert csll.head.next.next.data == 3
    assert csll.head.next.next.next.data == 2
    assert csll.head.next.next.next.next == csll.head

    # Test 5: Insert at invalid index
    node4 = Node(4)
    exceptionRaised = False
    try:
        csll.insert(node4, -1)
    except:
        exceptionRaised = True
    assert exceptionRaised
    assert csll.head.data == 4
    assert csll.tail.data == 2
    assert csll.size == 4
   
    # Test 6: Insert at invalid index
    node5 = Node(5)
    exceptionRaised = False
    try:
        csll.insert(node5, 5)
    except:
        exceptionRaised = True
    assert exceptionRaised
    assert csll.head.data == 4
    assert csll.tail.data == 2
    assert csll.size == 4
    
def test_csll_isSorted():
    # Test 1: Empty list
    csll = CSLL()
    assert csll.isSorted() == True

    # Test 2: Single element list
    node1 = Node(1)
    csll.insertTail(node1)
    csll.print()
    assert csll.isSorted() == True

    # Test 3: Sorted list
    node2 = Node(2)
    csll.insertTail(node2)
    csll.print()
    assert csll.isSorted() == True

    # Test 4: Unsorted list
    node3 = Node(3)
    csll.insertHead(node3)
    assert csll.isSorted() == False

def test_csll_sortedInsert():
    # Test 1: Empty list
    csll = CSLL()
    node1 = Node(1)
    csll.sortedInsert(node1)
    assert csll.head.data == 1
    assert csll.tail.data == 1
    assert csll.size == 1
    assert csll.head.next == csll.head
    assert csll.tail.next == csll.head

    # Test 2: Insert at tail
    node2 = Node(4)
    csll.sortedInsert(node2)
    assert csll.head.data == 1
    assert csll.tail.data == 4
    assert csll.size == 2
    assert csll.tail.next == csll.head
    assert csll.head.next.data == 4

    # Test 3: Insert at head
    node3 = Node(1)
    csll.sortedInsert(node3)
    assert csll.head.data == 1
    assert csll.tail.data == 4
    assert csll.size == 3
    assert csll.tail.next == csll.head
    assert csll.head.next.data == 1
    assert csll.head.next.next.data == 4

    # Test 4: Insert in middle
    node4 = Node(3)
    csll.sortedInsert(node4)
    assert csll.tail.data == 4
    assert csll.size == 4
    assert csll.head.data == 1
    assert csll.head.next.data == 1
    assert csll.head.next.next.data == 3
    assert csll.head.next.next.next.data == 4
    assert csll.tail.next == csll.head

def test_csll_search():
    # Test 1: Empty list
    csll = CSLL()
    node1 = Node(1)
    assert csll.search(node1) == None

    # Test 2: Single element list
    csll.insertTail(node1)
    assert csll.search(node1) == node1

    # Test 3: Multiple element list
    node2 = Node(2)
    csll.insertTail(node2)
    assert csll.search(node1) == node1
    assert csll.search(node2) == node2

    # Test 4: Not found
    node3 = Node(3)
    assert csll.search(node3) == None

def test_csll_deleteHead():
    # Test 1: Empty list
    csll = CSLL()
    csll.deleteHead()
    assert csll.head == None
    assert csll.tail == None
    assert csll.size == 0

    # Test 2: Single element list
    node1 = Node(1)
    csll.insertTail(node1)
    csll.deleteHead()
    assert csll.head == None
    assert csll.tail == None
    assert csll.size == 0

    # Test 3: Multiple element list
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    csll.insertTail(node2)
    csll.insertTail(node3)
    csll.insertTail(node4)
    csll.deleteHead()
    assert csll.head.data == 3
    assert csll.tail.data == 4
    assert csll.size == 2
    assert csll.head.next.data == 4

def test_csll_deleteTail():
    # Test 1: Empty list
    csll = CSLL()
    csll.deleteTail()
    assert csll.head == None
    assert csll.tail == None
    assert csll.size == 0

    # Test 2: Single element list
    node1 = Node(1)
    csll.insertTail(node1)
    csll.deleteTail()
    assert csll.head == None
    assert csll.tail == None
    assert csll.size == 0

    # Test 3: Multiple element list
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    csll.insertTail(node2)
    csll.insertTail(node3)
    csll.insertTail(node4)
    csll.deleteTail()
    assert csll.head.data == 2
    assert csll.tail.data == 3
    assert csll.size == 2
    assert csll.head.next.data == 3
    assert csll.tail.next == csll.head

def test_csll_delete():
    csll = CSLL()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    # Test 1: Empty list
    csll.delete(node1)
    assert csll.head == None
    assert csll.tail == None
    assert csll.size == 0

    # Test 2: Single element list
    csll.insertTail(node1)
    csll.delete(node1)
    assert csll.head == None
    assert csll.tail == None
    assert csll.size == 0

    # Test 3: Delete middle element
    csll.insertTail(node1)
    csll.insertTail(node2)
    csll.insertTail(node3)
    csll.delete(node2)
    assert csll.head.data == 1
    assert csll.tail.data == 3
    assert csll.size == 2
    assert csll.head.next.data == 3
    
    # Test 4: Delete head
    csll.delete(node1)
    assert csll.head.data == 3
    assert csll.tail.data == 3
    assert csll.size == 1
    assert csll.head.next.data == 3

    # Test 5: Not found
    node5 = Node(5)
    csll.delete(node5)
    assert csll.head.data == 3
    assert csll.tail.data == 3
    assert csll.size == 1

    # Test 6: Delete tail
    csll.delete(node3)
    assert csll.head == None
    assert csll.tail == None
    assert csll.size == 0

def test_csll_sort():
    # Test 1: Empty list
    csll = CSLL()
    csll.sort()
    assert csll.head == None
    assert csll.tail == None
    assert csll.size == 0

    # Test 2: Single element list
    node1 = Node(1)
    csll.insertTail(node1)
    csll.sort()
    assert csll.head.data == 1
    assert csll.tail.data == 1
    assert csll.size == 1

    # Test 3: Multiple element list
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    csll.insertTail(node4)
    csll.insertTail(node3)
    csll.insertTail(node2)
    csll.sort()
    assert csll.head.data == 1
    assert csll.tail.data == 4
    assert csll.size == 4
    assert csll.head.next.data == 2
    assert csll.head.next.next.data == 3
    assert csll.head.next.next.next.data == 4

def test_csll_clear():
    csll = CSLL()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    # Test 1: Empty list
    csll.clear()
    assert csll.head == None
    assert csll.tail == None
    assert csll.size == 0

    # Test 2: Single element list
    csll.insertTail(node1)
    csll.clear()
    assert csll.head == None
    assert csll.tail == None
    assert csll.size == 0

    # Test 3: Multiple element list
    csll.insertTail(node2)
    csll.insertTail(node3)
    csll.insertTail(node4)
    csll.clear()
    assert csll.head == None
    assert csll.tail == None
    assert csll.size == 0