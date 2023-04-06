from SLL import SLL
from DNode import DNode
def test_SLL_Constructors():
    sll = SLL()
    assert sll.head == None
    assert sll.tail == None
    assert sll.size == 0
    DmyNode = DNode(1)
    sll1 = SLL(DmyNode)
    assert sll1.head.data == 1
    assert sll1.tail.data == 1
    assert sll1.size == 1
def test_SLL_len():
    sll = SLL()
    assert len(sll) == 0
    DmyNode = DNode(1)
    sll1 = SLL(DmyNode)
    assert len(sll1) == 1
def test_SLL_insertHead():
    sll = SLL()
    Dnode1 = DNode(1)
    sll.insertHead(Dnode1)
    assert sll.head.data == 1
    assert sll.tail.data == 1
    assert sll.size == 1
    Dnode2 = DNode(2)
    sll.insertHead(Dnode2)
    assert sll.head.data == 2
    assert sll.tail.data == 1
    assert sll.size == 2
def test_SLL_insertTail():
    sll = SLL()
    Dnode1 = DNode(1)
    sll.insertTail(Dnode1)
    assert sll.head.data == 1
    assert sll.tail.data == 1
    assert sll.size == 1
    Dnode2 = DNode(2)
    sll.insertTail(Dnode2)
    assert sll.head.data == 1
    assert sll.tail.data == 2
    assert sll.size == 2

def test_SLL_insert():
    # Test 1: Insert at head
    sll = SLL()
    Dnode1 = DNode(1)
    sll.insert(Dnode1, 0)
    assert sll.head.data == 1
    assert sll.tail.data == 1
    assert sll.size == 1
    
    # Test 2: Insert at tail
    Dnode2 = DNode(2)
    sll.insert(Dnode2, 1)
    assert sll.head.data == 1
    assert sll.tail.data == 2
    assert sll.size == 2
    
    # Test 3: Insert in middle
    Dnode3 = DNode(3)
    sll.insert(Dnode3, 1)
    assert sll.head.data == 1
    assert sll.tail.data == 2
    assert sll.size == 3
    assert sll.head.next.data == 3
    assert sll.head.next.next.data == 2
    
    # Test 4: Insert at invalid index
    Dnode4 = DNode(4)
    exceptionRaised = False
    try:
        sll.insert(Dnode4, -1)
    except:
        exceptionRaised = True
    assert exceptionRaised
    assert sll.head.data == 1
    assert sll.tail.data == 2
    assert sll.size == 3
    
    # Test 5: Insert at invalid index
    Dnode5 = DNode(5)
    exceptionRaised = False
    try:
        sll.insert(Dnode5, 4)
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
    Dnode1 = DNode(1)
    sll.insertTail(Dnode1)
    assert sll.isSorted() == True

    # Test 3: Sorted list
    Dnode2 = DNode(2)
    sll.insertTail(Dnode2)
    assert sll.isSorted() == True

    # Test 4: Unsorted list
    Dnode3 = DNode(3)
    sll.insertHead(Dnode3)
    assert sll.isSorted() == False

def test_SLL_sortedInsert():
    # Test 1: Empty list
    sll = SLL()
    Dnode1 = DNode(1)
    sll.sortedInsert(Dnode1)
    assert sll.head.data == 1
    assert sll.tail.data == 1
    assert sll.size == 1

    # Test 2: Insert at tail
    Dnode2 = DNode(4)
    sll.sortedInsert(Dnode2)
    assert sll.head.data == 1
    assert sll.tail.data == 4
    assert sll.size == 2

    # Test 3: Insert at head
    Dnode3 = DNode(1)
    sll.sortedInsert(Dnode3)
    assert sll.head.data == 1
    assert sll.tail.data == 4
    assert sll.size == 3

    # Test 4: Insert in middle
    Dnode4 = DNode(3)
    sll.sortedInsert(Dnode4)
    assert sll.head.data == 1
    assert sll.tail.data == 4
    assert sll.size == 4
    assert sll.head.next.data == 1
    assert sll.head.next.next.data == 3

def test_SLL_search():
    # Test 1: Empty list
    sll = SLL()
    Dnode1 = DNode(1)
    assert sll.search(Dnode1) == None

    # Test 2: Single element list
    sll.insertTail(Dnode1)
    assert sll.search(Dnode1) == Dnode1

    # Test 3: Multiple element list
    Dnode2 = DNode(2)
    sll.insertTail(Dnode2)
    assert sll.search(Dnode1) == Dnode1
    assert sll.search(Dnode2) == Dnode2

    # Test 4: Not found
    Dnode3 = DNode(3)
    assert sll.search(Dnode3) == None

def test_SLL_deleteHead():
    # Test 1: Empty list
    sll = SLL()
    sll.deleteHead()
    assert sll.head == None
    assert sll.tail == None
    assert sll.size == 0

    # Test 2: Single element list
    Dnode1 = DNode(1)
    sll.insertTail(Dnode1)
    sll.deleteHead()
    assert sll.head == None
    assert sll.tail == None
    assert sll.size == 0

    # Test 3: Multiple element list
    Dnode2 = DNode(2)
    Dnode3 = DNode(3)
    Dnode4 = DNode(4)
    sll.insertTail(Dnode2)
    sll.insertTail(Dnode3)
    sll.insertTail(Dnode4)
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
    Dnode1 = DNode(1)
    sll.insertTail(Dnode1)
    sll.deleteTail()
    assert sll.head == None
    assert sll.tail == None
    assert sll.size == 0

    # Test 3: Multiple element list
    Dnode2 = DNode(2)
    Dnode3 = DNode(3)
    Dnode4 = DNode(4)
    sll.insertTail(Dnode2)
    sll.insertTail(Dnode3)
    sll.insertTail(Dnode4)
    sll.deleteTail()
    assert sll.head.data == 2
    assert sll.tail.data == 3
    assert sll.size == 2

def test_SLL_delete():
    # Test 1: Empty list
    sll = SLL()
    Dnode1 = DNode(1)
    sll.delete(Dnode1)
    assert sll.head == None
    assert sll.tail == None
    assert sll.size == 0

    # Test 2: Single element list
    sll.insertTail(Dnode1)
    sll.delete(Dnode1)
    assert sll.head == None
    assert sll.tail == None
    assert sll.size == 0

    # Test 3: Delete middle element
    Dnode2 = DNode(2)
    Dnode3 = DNode(3)
    Dnode4 = DNode(4)
    sll.insertTail(Dnode1)
    sll.insertTail(Dnode2)
    sll.insertTail(Dnode3)
    sll.insertTail(Dnode4)
    sll.delete(Dnode3)
    assert sll.head.data == 1
    assert sll.tail.data == 4
    assert sll.size == 3
    assert sll.head.next.data == 2
    assert sll.head.next.next.data == 4

    # Test 4: Delete head
    sll.delete(Dnode1)
    assert sll.head.data == 2
    assert sll.tail.data == 4
    assert sll.size == 2
    assert sll.head.next.data == 4
    assert sll.tail.data == 4

    # Test 5: Not found
    Dnode5 = DNode(5)
    sll.delete(Dnode5)
    assert sll.head.data == 2
    assert sll.tail.data == 4
    assert sll.size == 2

def test_SLL_sort():
    # Test 1: Empty list
    sll = SLL()
    sll.sort()
    assert sll.head == None
    assert sll.tail == None
    assert sll.size == 0

    # Test 2: Single element list
    Dnode1 = DNode(1)
    sll.insertTail(Dnode1)
    sll.sort()
    assert sll.head.data == 1
    assert sll.tail.data == 1
    assert sll.size == 1

    # Test 3: Multiple element list
    Dnode2 = DNode(2)
    Dnode3 = DNode(3)
    Dnode4 = DNode(4)
    sll.insertTail(Dnode4)
    sll.insertTail(Dnode3)
    sll.insertTail(Dnode2)
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
    Dnode1 = DNode(1)
    sll.insertTail(Dnode1)
    sll.clear()
    assert sll.head == None
    assert sll.tail == None
    assert sll.size == 0

    # Test 3: Multiple element list
    Dnode2 = DNode(2)
    Dnode3 = DNode(3)
    Dnode4 = DNode(4)
    sll.insertTail(Dnode2)
    sll.insertTail(Dnode3)
    sll.insertTail(Dnode4)
    sll.clear()
    assert sll.head == None
    assert sll.tail == None
    assert sll.size == 0