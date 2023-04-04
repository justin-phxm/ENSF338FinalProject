from DLL import DLL
from DNode import DNode
def test_DLL_Constructors():
    # Test 1: Default constructor
    dll = DLL()
    assert dll.head == None
    assert dll.tail == None
    assert dll.size == 0

    # Test 2: Constructor with node
    myNode = DNode(1)
    dll1 = DLL(myNode)
    assert dll1.head.data == 1
    assert dll1.tail.data == 1
    assert dll1.size == 1

def test_DLL_len():
    # Test 1: Default constructor
    dll = DLL()
    assert len(dll) == 0
    myNode = DNode(1)
    dll1 = DLL(myNode)
    assert len(dll1) == 1

def test_DLL_insertHead():
    # Test 1: Insert at head
    dll = DLL()
    node1 = DNode(1)
    dll.insertHead(node1)
    assert dll.head.data == 1
    assert dll.tail.data == 1
    assert dll.size == 1
    assert dll.head.previous == None

    # Test 2: Insert new Node at head
    node2 = DNode(2)
    dll.insertHead(node2)
    assert dll.head.data == 2
    assert dll.tail.data == 1
    assert dll.size == 2
    assert dll.head.previous == None
    assert dll.head.next.previous == dll.head
    assert dll.tail.previous == dll.head


def test_DLL_insertTail():
    # Test 1: Insert in empty list
    dll = DLL()
    node1 = DNode(1)
    dll.insertTail(node1)
    assert dll.head.data == 1
    assert dll.tail.data == 1
    assert dll.size == 1
    assert dll.head.previous == None
 
    # Test 2: Insert at tail
    node2 = DNode(2)
    node3 = DNode(3)
    dll.insertTail(node2)
    dll.insertTail(node3)
    assert dll.head.data == 1
    assert dll.tail.data == 3
    assert dll.size == 3
    assert dll.tail.previous == dll.head.next

def test_DLL_insert():
    # Test 1: Insert at head
    dll = DLL()
    node1 = DNode(1)
    dll.insert(node1, 0)
    assert dll.head.data == 1
    assert dll.tail.data == 1
    assert dll.size == 1
    assert dll.head.previous == None

    # Test 2: Insert at tail
    node2 = DNode(2)
    dll.insert(node2, 1)
    assert dll.head.data == 1
    assert dll.tail.data == 2
    assert dll.size == 2
    assert dll.tail.previous == dll.head

    # Test 3: Insert in middle
    node3 = DNode(3)
    dll.insert(node3, 1)
    assert dll.head.data == 1
    assert dll.tail.data == 2
    assert dll.size == 3
    assert dll.head.next.data == 3
    assert dll.head.next.next.data == 2
    assert dll.tail.previous == dll.head.next
    assert dll.head.next.previous == dll.head

    # Test 4: Insert at invalid index
    node4 = DNode(4)
    exceptionRaised = False
    try:
        dll.insert(node4, -1)
    except:
        exceptionRaised = True
    assert exceptionRaised
    assert dll.head.data == 1
    assert dll.tail.data == 2
    assert dll.size == 3

    # Test 5: Insert at invalid index
    node5 = DNode(5)
    exceptionRaised = False
    try:
        dll.insert(node5, 4)
    except:
        exceptionRaised = True
    assert exceptionRaised
    assert dll.head.data == 1
    assert dll.tail.data == 2
    assert dll.size == 3
    
def test_DLL_isSorted():
    # Test 1: Empty list
    dll = DLL()
    assert dll.isSorted() == True

    # Test 2: Single element list
    node1 = DNode(1)
    dll.insertTail(node1)
    assert dll.isSorted() == True

    # Test 3: Sorted list
    node2 = DNode(2)
    dll.insertTail(node2)
    assert dll.isSorted() == True

    # Test 4: Unsorted list
    node3 = DNode(3)
    dll.insertHead(node3)
    assert dll.isSorted() == False

def test_DLL_sortedInsert():
    # Test 1: Empty list
    dll = DLL()
    node1 = DNode(1)
    dll.sortedInsert(node1)
    assert dll.head.data == 1
    assert dll.tail.data == 1
    assert dll.size == 1

    # Test 2: Insert at tail
    node2 = DNode(4)
    dll.sortedInsert(node2)
    assert dll.head.data == 1
    assert dll.tail.data == 4
    assert dll.size == 2
    assert dll.tail.previous == dll.head

    # Test 3: Insert at head
    node3 = DNode(1)
    dll.sortedInsert(node3)
    assert dll.head.data == 1
    assert dll.tail.data == 4
    assert dll.size == 3
    assert dll.head.next.previous.data == 1

    # Test 4: Insert in middle
    node4 = DNode(3)
    dll.sortedInsert(node4)
    assert dll.head.data == 1
    assert dll.tail.data == 4
    assert dll.size == 4
    assert dll.head.next.data == 1
    assert dll.head.next.next.data == 3
    assert dll.tail.previous.data == 3

    # Test 5: Insert duplicate
    node5 = DNode(3)
    dll.sortedInsert(node5)
    assert dll.head.data == 1
    assert dll.tail.data == 4
    assert dll.size == 5
    assert dll.head.next.data == 1
    assert dll.head.next.next.data == 3
    assert dll.head.next.next.next.data == 3
    assert dll.tail.previous.data == 3

def test_DLL_search():
    # Test 1: Empty list
    dll = DLL()
    node1 = DNode(1)
    assert dll.search(node1) == None

    # Test 2: Single element list
    dll.insertTail(node1)
    assert dll.search(node1) == node1

    # Test 3: Multiple element list
    node2 = DNode(2)
    dll.insertTail(node2)
    assert dll.search(node1) == node1
    assert dll.search(node2) == node2

    # Test 4: Not found
    node3 = DNode(3)
    assert dll.search(node3) == None

def test_SLL_deleteHead():
    # Test 1: Empty list
    dll = DLL()
    dll.deleteHead()
    assert dll.head == None
    assert dll.tail == None
    assert dll.size == 0

    # Test 2: Single element list
    node1 = DNode(1)
    dll.insertTail(node1)
    dll.deleteHead()
    assert dll.head == None
    assert dll.tail == None
    assert dll.size == 0

    # Test 3: Multiple element list
    node2 = DNode(2)
    node3 = DNode(3)
    node4 = DNode(4)
    dll.insertTail(node2)
    dll.insertTail(node3)
    dll.insertTail(node4)
    dll.deleteHead()
    assert dll.head.data == 3
    assert dll.tail.data == 4
    assert dll.size == 2
    assert dll.head.previous == None
    assert dll.head.next.previous == dll.head

def test_SLL_deleteTail():
    # Test 1: Empty list
    dll = DLL()
    dll.deleteTail()
    assert dll.head == None
    assert dll.tail == None
    assert dll.size == 0

    # Test 2: Single element list
    node1 = DNode(1)
    dll.insertTail(node1)
    dll.deleteTail()
    assert dll.head == None
    assert dll.tail == None
    assert dll.size == 0

    # Test 3: Multiple element list
    node2 = DNode(2)
    node3 = DNode(3)
    node4 = DNode(4)
    dll.insertTail(node2)
    dll.insertTail(node3)
    dll.insertTail(node4)
    dll.deleteTail()
    assert dll.head.data == 2
    assert dll.tail.data == 3
    assert dll.size == 2
    assert dll.tail.previous.data == 2
    assert dll.tail.next == None

def test_DLL_delete():
    # Test 1: Empty list
    dll = DLL()
    node1 = DNode(1)
    dll.delete(node1)
    assert dll.head == None
    assert dll.tail == None
    assert dll.size == 0

    # Test 2: Single element list
    dll.insertTail(node1)
    dll.delete(node1)
    assert dll.head == None
    assert dll.tail == None
    assert dll.size == 0

    # Test 3: Delete middle element
    node1 = DNode(1)
    node2 = DNode(2)
    node3 = DNode(3)
    node4 = DNode(4)
    dll.insertTail(node1)
    dll.insertTail(node2)
    dll.insertTail(node3)
    dll.insertTail(node4)
    dll.delete(node3)
    assert dll.head.data == 1
    assert dll.tail.data == 4
    assert dll.size == 3
    assert dll.head.next.data == 2
    assert dll.head.next.next.data == 4
    assert dll.tail.previous.data == 2

    # Test 4: Delete head
    dll.delete(node1)
    assert dll.head.data == 2
    assert dll.tail.data == 4
    assert dll.size == 2
    assert dll.head.next.data == 4
    assert dll.tail.data == 4
    assert dll.tail.previous.data == 2

    # Test 5: Not found
    node5 = DNode(5)
    dll.delete(node5)
    assert dll.head.data == 2
    assert dll.tail.data == 4
    assert dll.size == 2

def test_DLL_sort():
    
    # Test 1: Empty list
    dll = DLL()
    dll.sort()
    assert dll.head == None
    assert dll.tail == None
    assert dll.size == 0

    # Test 2: Single element list
    node1 = DNode(1)
    dll.insertTail(node1)
    dll.sort()
    assert dll.head.data == 1
    assert dll.tail.data == 1
    assert dll.size == 1
    assert dll.head.previous == None

    # Test 3: Multiple element list
    node2 = DNode(2)
    node3 = DNode(3)
    node4 = DNode(4)
    dll.insertTail(node4)
    dll.insertTail(node3)
    dll.insertTail(node2)
    dll.sort()
    assert dll.head.data == 1
    assert dll.tail.data == 4
    assert dll.size == 4
    assert dll.head.next.data == 2
    assert dll.head.next.next.data == 3
    assert dll.head.next.next.next.data == 4
    assert dll.head.previous == None
    assert dll.tail.previous.data == 3

def test_SLL_clear():
    # Test 1: Empty list
    dll = DLL()
    dll.clear()
    assert dll.head == None
    assert dll.tail == None
    assert dll.size == 0

    # Test 2: Single element list
    node1 = DNode(1)
    dll.insertTail(node1)
    dll.clear()
    assert dll.head == None
    assert dll.tail == None
    assert dll.size == 0

    # Test 3: Multiple element list
    node2 = DNode(2)
    node3 = DNode(3)
    node4 = DNode(4)
    dll.insertTail(node2)
    dll.insertTail(node3)
    dll.insertTail(node4)
    dll.clear()
    assert dll.head == None
    assert dll.tail == None
    assert dll.size == 0