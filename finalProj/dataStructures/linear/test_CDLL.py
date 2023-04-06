from CDLL import CDLL
from DNode import DNode

def test_cdll_Constructors():
    # Test 1: Default constructor
    cdll = CDLL()
    assert cdll.head == None
    assert cdll.size == 0

    # Test 2: Constructor with Dnode
    myDNode = DNode(1)
    cdll1 = CDLL(myDNode)
    assert cdll1.head.data == 1
    assert cdll1.size == 1
    assert cdll1.head.next == cdll1.head
    assert cdll1.tail.previous == cdll1.head

def test_cdll_len():
    cdll = CDLL()
    Dnode1 = DNode(1)
    # Test 1: Default constructor
    assert len(cdll) == 0
    
    # Test 2: Constructor with Dnode
    cdll1 = CDLL(Dnode1)
    assert len(cdll1) == 1

def test_cdll_insertHead():
    cdll = CDLL()
    Dnode1 = DNode(1)
    Dnode2 = DNode(2)
    Dnode3 = DNode(3)
    # Test 1: Insert at head
    cdll.insertHead(Dnode1)
    assert cdll.head.data == 1
    assert cdll.size == 1
    assert cdll.head.next == cdll.head
    assert cdll.head.previous == cdll.tail

    # Test 2: Insert new DNode at head
    cdll.insertHead(Dnode2)
    assert cdll.head.data == 2
    assert cdll.size == 2
    assert cdll.head.next == Dnode1
    assert cdll.head.next.next == cdll.head
    assert cdll.head.previous == cdll.tail

    # Test 3: Insert new head in list with 2 Dnodes
    cdll.insertHead(Dnode3)
    assert cdll.head.data == 3
    assert cdll.size == 3
    assert cdll.head.next == Dnode2
    assert cdll.head.next.next == Dnode1
    assert cdll.head.next.next.next == cdll.head
    assert cdll.head.previous == cdll.tail

def test_cdll_insertTail():
    cdll = CDLL()
    Dnode1 = DNode(1)
    Dnode2 = DNode(2)
    Dnode3 = DNode(3)
    # Test 1: Insert in empty list
    cdll.insertTail(Dnode1)
    assert cdll.head.data == 1
    assert cdll.tail.data == 1
    assert cdll.size == 1
    assert cdll.head.next == cdll.head
    assert cdll.head.previous == cdll.tail

    # Test 2: Insert at tail
    cdll.insertTail(Dnode2)
    assert cdll.head.data == 1
    assert cdll.tail.data == 2
    assert cdll.size == 2
    assert cdll.head.next == Dnode2
    assert cdll.head.next.next == cdll.head
    assert cdll.head.previous == cdll.tail

    # Test 3: Insert at tail in list with 2 Dnodes
    cdll.insertTail(Dnode3)
    assert cdll.head.data == 1
    assert cdll.tail.data == 3
    assert cdll.size == 3
    assert cdll.head.next == Dnode2
    assert cdll.head.next.next == Dnode3
    assert cdll.head.next.next.next == cdll.head
    assert cdll.head.previous == cdll.tail

def test_cdll_insert():
    cdll = CDLL()
    Dnode1 = DNode(1)
    Dnode2 = DNode(2)
    Dnode3 = DNode(3)
    Dnode4 = DNode(4)    
    Dnode5 = DNode(5)
    # Test 1: Insert at head
    cdll.insert(Dnode1, 0)
    assert cdll.head.data == 1
    assert cdll.size == 1
    assert cdll.tail.data == 1
    assert cdll.head.previous == cdll.tail    

    # Test 2: Insert at tail
    cdll.insert(Dnode2, 1)
    assert cdll.head.data == 1
    assert cdll.size == 2
    assert cdll.tail.data == 2
    assert cdll.head.previous == cdll.tail    

    # Test 3: Insert in middle
    cdll.insert(Dnode3, 1)
    assert cdll.head.data == 1
    assert cdll.tail.data == 2
    assert cdll.size == 3
    assert cdll.head.next.data == 3
    assert cdll.head.next.next.data == 2
    assert cdll.head.next.next.next == cdll.head
    assert cdll.head.previous == cdll.tail
    assert cdll.tail.previous.data == 3

    # Test 4: Insert at head in list with 3 Dnodes
    cdll.insert(Dnode4, 0)
    assert cdll.head.data == 4
    assert cdll.tail.data == 2
    assert cdll.size == 4
    assert cdll.head.next.data == 1
    assert cdll.head.next.next.data == 3
    assert cdll.head.next.next.next.data == 2
    assert cdll.head.next.next.next.next == cdll.head
    assert cdll.head.previous == cdll.tail

    # Test 5: Insert at invalid index
    exceptionRaised = False
    try:
        cdll.insert(Dnode4, -1)
    except:
        exceptionRaised = True
    assert exceptionRaised
    assert cdll.head.data == 4
    assert cdll.tail.data == 2
    assert cdll.size == 4
    assert cdll.head.previous == cdll.tail

    # Test 6: Insert at invalid index
    exceptionRaised = False
    try:
        cdll.insert(Dnode5, 5)
    except:
        exceptionRaised = True
    assert exceptionRaised
    assert cdll.head.data == 4
    assert cdll.tail.data == 2
    assert cdll.size == 4
    assert cdll.head.previous == cdll.tail

def test_cdll_isSorted():
    cdll = CDLL()
    # Test 1: Empty list
    assert cdll.isSorted() == True

    # Test 2: Single element list
    Dnode1 = DNode(1)
    cdll.insertTail(Dnode1)
    cdll.print()
    assert cdll.isSorted() == True

    # Test 3: Sorted list
    Dnode2 = DNode(2)
    cdll.insert(Dnode2, 1)
    cdll.print()
    assert cdll.isSorted() == True

    # Test 4: Unsorted list
    Dnode3 = DNode(3)
    cdll.insertHead(Dnode3)
    assert cdll.isSorted() == False

def test_cdll_sortedInsert():
    cdll = CDLL()
    Dnode1 = DNode(1)
    # Test 1: Empty list
    cdll.sortedInsert(Dnode1)
    assert cdll.head.data == 1
    assert cdll.tail.data == 1
    assert cdll.size == 1
    assert cdll.head.next == cdll.head
    assert cdll.tail.next == cdll.head
    assert cdll.head.previous == cdll.tail

    # Test 2: Insert at tail
    Dnode2 = DNode(4)
    cdll.sortedInsert(Dnode2)
    assert cdll.head.data == 1
    assert cdll.tail.data == 4
    assert cdll.size == 2
    assert cdll.tail.next == cdll.head
    assert cdll.head.next.data == 4
    assert cdll.head.previous == cdll.tail

    # Test 3: Insert at head
    Dnode3 = DNode(1)
    cdll.sortedInsert(Dnode3)
    assert cdll.head.data == 1
    assert cdll.tail.data == 4
    assert cdll.size == 3
    assert cdll.tail.next == cdll.head
    assert cdll.head.next.data == 1
    assert cdll.head.next.next.data == 4
    assert cdll.head.previous == cdll.tail

    # Test 4: Insert in middle
    Dnode4 = DNode(3)
    cdll.sortedInsert(Dnode4)
    assert cdll.tail.data == 4
    assert cdll.size == 4
    assert cdll.head.data == 1
    assert cdll.head.next.data == 1
    assert cdll.head.next.next.data == 3
    assert cdll.head.next.next.next.data == 4
    assert cdll.tail.next == cdll.head
    assert cdll.head.previous == cdll.tail

def test_cdll_search():
    cdll = CDLL()
    Dnode1 = DNode(1)
    # Test 1: Empty list
    assert cdll.search(Dnode1) == None

    # Test 2: Single element list
    cdll.insertTail(Dnode1)
    assert cdll.search(Dnode1) == Dnode1

    # Test 3: Multiple element list
    Dnode2 = DNode(2)
    cdll.insertTail(Dnode2)
    assert cdll.search(Dnode1) == Dnode1
    assert cdll.search(Dnode2) == Dnode2

    # Test 4: Not found
    Dnode3 = DNode(3)
    assert cdll.search(Dnode3) == None

def test_cdll_deleteHead():
    cdll = CDLL()
    # Test 1: Empty list
    cdll.deleteHead()
    assert cdll.head == None
    assert cdll.tail == None
    assert cdll.size == 0

    # Test 2: Single element list
    Dnode1 = DNode(1)
    cdll.insertTail(Dnode1)
    cdll.deleteHead()
    assert cdll.head == None
    assert cdll.tail == None
    assert cdll.size == 0

    # Test 3: Multiple element list
    Dnode2 = DNode(2)
    Dnode3 = DNode(3)
    Dnode4 = DNode(4)
    cdll.insertTail(Dnode2)
    cdll.insertTail(Dnode3)
    cdll.insertTail(Dnode4)
    cdll.deleteHead()
    assert cdll.head.data == 3
    assert cdll.tail.data == 4
    assert cdll.size == 2
    assert cdll.head.next.data == 4
    assert cdll.head.previous.data == cdll.tail.data

def test_cdll_deleteTail():
    cdll = CDLL()
    # Test 1: Empty list
    cdll.deleteTail()
    assert cdll.head == None
    assert cdll.tail == None
    assert cdll.size == 0

    # Test 2: Single element list
    Dnode1 = DNode(1)
    cdll.insertTail(Dnode1)
    cdll.deleteTail()
    assert cdll.head == None
    assert cdll.tail == None
    assert cdll.size == 0

    # Test 3: Multiple element list
    Dnode2 = DNode(2)
    Dnode3 = DNode(3)
    Dnode4 = DNode(4)
    cdll.insertTail(Dnode2)
    cdll.insertTail(Dnode3)
    cdll.insertTail(Dnode4)
    cdll.deleteTail()
    assert cdll.head.data == 2
    assert cdll.tail.data == 3
    assert cdll.size == 2
    assert cdll.head.next.data == 3
    assert cdll.tail.next == cdll.head
    assert cdll.head.previous.data == cdll.tail.data

def test_cdll_delete():
    cdll = CDLL()
    Dnode1 = DNode(1)
    Dnode2 = DNode(2)
    Dnode3 = DNode(3)
    Dnode4 = DNode(4)
    Dnode5 = DNode(5)
    # Test 1: Empty list
    cdll.delete(Dnode1)
    assert cdll.head == None
    assert cdll.tail == None
    assert cdll.size == 0

    # Test 2: Single element list
    cdll.insertTail(Dnode1)
    cdll.delete(Dnode1)
    assert cdll.head == None
    assert cdll.tail == None
    assert cdll.size == 0

    # Test 3: Delete middle element
    cdll.insertTail(Dnode1)
    cdll.insertTail(Dnode2)
    cdll.insertTail(Dnode3)
    cdll.insertTail(Dnode4)
    cdll.delete(Dnode2)
    assert cdll.head.data == 1
    assert cdll.tail.data == 4
    assert cdll.size == 3
    assert cdll.head.next.data == 3
    assert cdll.head.previous.data == cdll.tail.data
    
    # Test 4: Delete head
    cdll.delete(Dnode1)
    assert cdll.head.data == 3
    assert cdll.tail.data == 4
    assert cdll.size == 2
    assert cdll.head.next.data == 4
    assert cdll.head.previous.data == cdll.tail.data

    # Test 5: Not found
    cdll.delete(Dnode5)
    assert cdll.head.data == 3
    assert cdll.tail.data == 4
    assert cdll.size == 2
    assert cdll.head.previous.data == cdll.tail.data

    # Test 6: Delete tail
    cdll.delete(Dnode3)
    assert cdll.head.data == 4
    assert cdll.tail.data == 4
    assert cdll.size == 1

def test_cdll_sort():
    cdll = CDLL()
    # Test 1: Empty list
    cdll.sort()
    assert cdll.head == None
    assert cdll.tail == None
    assert cdll.size == 0

    # Test 2: Single element list
    Dnode1 = DNode(1)
    cdll.insertTail(Dnode1)
    cdll.sort()
    assert cdll.head.data == 1
    assert cdll.tail.data == 1
    assert cdll.size == 1

    # Test 3: Multiple element list
    Dnode2 = DNode(2)
    Dnode3 = DNode(3)
    Dnode4 = DNode(4)
    cdll.insertHead(Dnode4)
    cdll.insert(Dnode3, 1)
    cdll.insertTail(Dnode2)
    cdll.sort()
    assert cdll.head.data == 1
    assert cdll.tail.data == 4
    assert cdll.size == 4
    assert cdll.head.next.data == 2
    assert cdll.head.next.next.data == 3
    assert cdll.head.next.next.next.data == 4

def test_cdll_clear():
    cdll = CDLL()
    Dnode1 = DNode(1)
    Dnode2 = DNode(2)
    Dnode3 = DNode(3)
    Dnode4 = DNode(4)
    # Test 1: Empty list
    cdll.clear()
    assert cdll.head == None
    assert cdll.tail == None
    assert cdll.size == 0

    # Test 2: Single element list
    cdll.insertTail(Dnode1)
    cdll.clear()
    assert cdll.head == None
    assert cdll.tail == None
    assert cdll.size == 0

    # Test 3: Multiple element list
    cdll.insertTail(Dnode2)
    cdll.insertTail(Dnode3)
    cdll.insertTail(Dnode4)
    cdll.clear()
    assert cdll.head == None
    assert cdll.tail == None
    assert cdll.size == 0