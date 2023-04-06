from CSLL import CSLL
from DNode import DNode

def test_csll_Constructors():
    # Test 1: Default constructor
    csll = CSLL()
    assert csll.head == None
    assert csll.size == 0

    # Test 2: Constructor with Dnode
    myDNode = DNode(1)
    csll1 = CSLL(myDNode)
    assert csll1.head.data == 1
    assert csll1.size == 1
    assert csll1.head.next == csll1.head

def test_csll_len():
    # Test 1: Default constructor
    csll = CSLL()
    assert len(csll) == 0
    myDNode = DNode(1)

    # Test 2: Constructor with Dnode
    csll1 = CSLL(myDNode)
    assert len(csll1) == 1

def test_csll_insertHead():
    # Test 1: Insert at head
    csll = CSLL()
    Dnode1 = DNode(1)
    csll.insertHead(Dnode1)
    assert csll.head.data == 1
    assert csll.size == 1
    assert csll.head.next == csll.head

    # Test 2: Insert new DNode at head
    Dnode2 = DNode(2)
    csll.insertHead(Dnode2)
    assert csll.head.data == 2
    assert csll.size == 2
    assert csll.head.next == Dnode1
    assert csll.head.next.next == csll.head

    # Test 3: Insert new head in list with 2 Dnodes
    Dnode3 = DNode(3)
    csll.insertHead(Dnode3)
    assert csll.head.data == 3
    assert csll.size == 3
    assert csll.head.next == Dnode2
    assert csll.head.next.next == Dnode1
    assert csll.head.next.next.next == csll.head
    
def test_csll_insertTail():
    # Test 1: Insert in empty list
    csll = CSLL()
    Dnode1 = DNode(1)
    csll.insertTail(Dnode1)
    assert csll.head.data == 1
    assert csll.tail.data == 1
    assert csll.size == 1
    assert csll.head.next == csll.head

    # Test 2: Insert at tail
    Dnode2 = DNode(2)
    csll.insertTail(Dnode2)
    assert csll.head.data == 1
    assert csll.tail.data == 2
    assert csll.size == 2
    assert csll.head.next == Dnode2
    assert csll.head.next.next == csll.head

    # Test 3: Insert at tail in list with 2 Dnodes
    Dnode3 = DNode(3)
    csll.insertTail(Dnode3)
    assert csll.head.data == 1
    assert csll.tail.data == 3
    assert csll.size == 3
    assert csll.head.next == Dnode2
    assert csll.head.next.next == Dnode3
    assert csll.head.next.next.next == csll.head

def test_csll_insert():
    # Test 1: Insert at head
    csll = CSLL()
    Dnode1 = DNode(1)
    csll.insert(Dnode1, 0)
    assert csll.head.data == 1
    assert csll.size == 1
    assert csll.tail.data == 1

    # Test 2: Insert at tail
    Dnode2 = DNode(2)
    csll.insert(Dnode2, 1)
    assert csll.head.data == 1
    assert csll.size == 2
    assert csll.tail.data == 2
    
    # Test 3: Insert in middle
    Dnode3 = DNode(3)
    csll.insert(Dnode3, 1)
    assert csll.head.data == 1
    assert csll.tail.data == 2
    assert csll.size == 3
    assert csll.head.next.data == 3
    assert csll.head.next.next.data == 2
    assert csll.head.next.next.next == csll.head
  
    # Test 4: Insert at head in list with 3 Dnodes
    Dnode4 = DNode(4)
    csll.insert(Dnode4, 0)
    assert csll.head.data == 4
    assert csll.tail.data == 2
    assert csll.size == 4
    assert csll.head.next.data == 1
    assert csll.head.next.next.data == 3
    assert csll.head.next.next.next.data == 2
    assert csll.head.next.next.next.next == csll.head

    # Test 5: Insert at invalid index
    Dnode4 = DNode(4)
    exceptionRaised = False
    try:
        csll.insert(Dnode4, -1)
    except:
        exceptionRaised = True
    assert exceptionRaised
    assert csll.head.data == 4
    assert csll.tail.data == 2
    assert csll.size == 4
   
    # Test 6: Insert at invalid index
    Dnode5 = DNode(5)
    exceptionRaised = False
    try:
        csll.insert(Dnode5, 5)
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
    Dnode1 = DNode(1)
    csll.insertTail(Dnode1)
    csll.print()
    assert csll.isSorted() == True

    # Test 3: Sorted list
    Dnode2 = DNode(2)
    csll.insertTail(Dnode2)
    csll.print()
    assert csll.isSorted() == True

    # Test 4: Unsorted list
    Dnode3 = DNode(3)
    csll.insertHead(Dnode3)
    assert csll.isSorted() == False

def test_csll_sortedInsert():
    # Test 1: Empty list
    csll = CSLL()
    Dnode1 = DNode(1)
    csll.sortedInsert(Dnode1)
    assert csll.head.data == 1
    assert csll.tail.data == 1
    assert csll.size == 1
    assert csll.head.next == csll.head
    assert csll.tail.next == csll.head

    # Test 2: Insert at tail
    Dnode2 = DNode(4)
    csll.sortedInsert(Dnode2)
    assert csll.head.data == 1
    assert csll.tail.data == 4
    assert csll.size == 2
    assert csll.tail.next == csll.head
    assert csll.head.next.data == 4

    # Test 3: Insert at head
    Dnode3 = DNode(1)
    csll.sortedInsert(Dnode3)
    assert csll.head.data == 1
    assert csll.tail.data == 4
    assert csll.size == 3
    assert csll.tail.next == csll.head
    assert csll.head.next.data == 1
    assert csll.head.next.next.data == 4

    # Test 4: Insert in middle
    Dnode4 = DNode(3)
    csll.sortedInsert(Dnode4)
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
    Dnode1 = DNode(1)
    assert csll.search(Dnode1) == None

    # Test 2: Single element list
    csll.insertTail(Dnode1)
    assert csll.search(Dnode1) == Dnode1

    # Test 3: Multiple element list
    Dnode2 = DNode(2)
    csll.insertTail(Dnode2)
    assert csll.search(Dnode1) == Dnode1
    assert csll.search(Dnode2) == Dnode2

    # Test 4: Not found
    Dnode3 = DNode(3)
    assert csll.search(Dnode3) == None

def test_csll_deleteHead():
    # Test 1: Empty list
    csll = CSLL()
    csll.deleteHead()
    assert csll.head == None
    assert csll.tail == None
    assert csll.size == 0

    # Test 2: Single element list
    Dnode1 = DNode(1)
    csll.insertTail(Dnode1)
    csll.deleteHead()
    assert csll.head == None
    assert csll.tail == None
    assert csll.size == 0

    # Test 3: Multiple element list
    Dnode2 = DNode(2)
    Dnode3 = DNode(3)
    Dnode4 = DNode(4)
    csll.insertTail(Dnode2)
    csll.insertTail(Dnode3)
    csll.insertTail(Dnode4)
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
    Dnode1 = DNode(1)
    csll.insertTail(Dnode1)
    csll.deleteTail()
    assert csll.head == None
    assert csll.tail == None
    assert csll.size == 0

    # Test 3: Multiple element list
    Dnode2 = DNode(2)
    Dnode3 = DNode(3)
    Dnode4 = DNode(4)
    csll.insertTail(Dnode2)
    csll.insertTail(Dnode3)
    csll.insertTail(Dnode4)
    csll.deleteTail()
    assert csll.head.data == 2
    assert csll.tail.data == 3
    assert csll.size == 2
    assert csll.head.next.data == 3
    assert csll.tail.next == csll.head

def test_csll_delete():
    csll = CSLL()
    Dnode1 = DNode(1)
    Dnode2 = DNode(2)
    Dnode3 = DNode(3)

    # Test 1: Empty list
    csll.delete(Dnode1)
    assert csll.head == None
    assert csll.tail == None
    assert csll.size == 0

    # Test 2: Single element list
    csll.insertTail(Dnode1)
    csll.delete(Dnode1)
    assert csll.head == None
    assert csll.tail == None
    assert csll.size == 0

    # Test 3: Delete middle element
    csll.insertTail(Dnode1)
    csll.insertTail(Dnode2)
    csll.insertTail(Dnode3)
    csll.delete(Dnode2)
    assert csll.head.data == 1
    assert csll.tail.data == 3
    assert csll.size == 2
    assert csll.head.next.data == 3
    
    # Test 4: Delete head
    csll.delete(Dnode1)
    assert csll.head.data == 3
    assert csll.tail.data == 3
    assert csll.size == 1
    assert csll.head.next.data == 3

    # Test 5: Not found
    Dnode5 = DNode(5)
    csll.delete(Dnode5)
    assert csll.head.data == 3
    assert csll.tail.data == 3
    assert csll.size == 1

    # Test 6: Delete tail
    csll.delete(Dnode3)
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
    Dnode1 = DNode(1)
    csll.insertTail(Dnode1)
    csll.sort()
    assert csll.head.data == 1
    assert csll.tail.data == 1
    assert csll.size == 1

    # Test 3: Multiple element list
    Dnode2 = DNode(2)
    Dnode3 = DNode(3)
    Dnode4 = DNode(4)
    csll.insertTail(Dnode4)
    csll.insertTail(Dnode3)
    csll.insertTail(Dnode2)
    csll.sort()
    assert csll.head.data == 1
    assert csll.tail.data == 4
    assert csll.size == 4
    assert csll.head.next.data == 2
    assert csll.head.next.next.data == 3
    assert csll.head.next.next.next.data == 4

def test_csll_clear():
    csll = CSLL()
    Dnode1 = DNode(1)
    Dnode2 = DNode(2)
    Dnode3 = DNode(3)
    Dnode4 = DNode(4)
    # Test 1: Empty list
    csll.clear()
    assert csll.head == None
    assert csll.tail == None
    assert csll.size == 0

    # Test 2: Single element list
    csll.insertTail(Dnode1)
    csll.clear()
    assert csll.head == None
    assert csll.tail == None
    assert csll.size == 0

    # Test 3: Multiple element list
    csll.insertTail(Dnode2)
    csll.insertTail(Dnode3)
    csll.insertTail(Dnode4)
    csll.clear()
    assert csll.head == None
    assert csll.tail == None
    assert csll.size == 0