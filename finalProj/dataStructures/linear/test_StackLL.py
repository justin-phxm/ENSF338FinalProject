# from stackLL import stackLL
from DNode import DNode
from StackLL import StackLL
def test_stackLL_Constructors():
    stackLL = StackLL()
    assert stackLL.head == None
    assert stackLL.tail == None
    assert stackLL.size == 0
    DmyNode = DNode(1)

    stackLL1 = StackLL(DmyNode)
    assert stackLL1.head.data == 1
    assert stackLL1.tail.data == 1
    assert stackLL1.size == 1

def test_stackLL_len():
    # Test 1: Empty stackLL
    stackLL = StackLL()
    assert len(stackLL) == 0

    # Test 2: Non-empty stackLL
    DmyNode = DNode(1)
    stackLL1 = StackLL(DmyNode)
    assert len(stackLL1) == 1

def test_stackLL_insertHead():
    # Test 1: Insert into empty stackLL
    stackLL = StackLL()
    Dnode1 = DNode(1)
    stackLL.insertHead(Dnode1)
    assert stackLL.head.data == 1
    assert stackLL.tail.data == 1
    assert stackLL.size == 1
    
    # Test 2: Insert into non-empty stackLL
    Dnode2 = DNode(2)
    stackLL.insertHead(Dnode2)
    assert stackLL.head.data == 2
    assert stackLL.tail.data == 1
    assert stackLL.size == 2


def test_stackLL_insertTail():
    # Test 1: Insert into empty stackLL
    stackLL = StackLL()
    Dnode1 = DNode(1)
    stackLL.insertTail(Dnode1)
    assert stackLL.head == None
    assert stackLL.size == 0

# def test_stackLL_insert():
#     # Test 1: Insert at head
#     stackLL = stackLL()
#     Dnode1 = DNode(1)
#     stackLL.insert(Dnode1, 0)
#     assert stackLL.head.data == 1
#     assert stackLL.tail.data == 1
#     assert stackLL.size == 1
    
#     # Test 2: Insert at tail
#     Dnode2 = DNode(2)
#     stackLL.insert(Dnode2, 1)
#     assert stackLL.head.data == 1
#     assert stackLL.tail.data == 2
#     assert stackLL.size == 2
    
#     # Test 3: Insert in middle
#     Dnode3 = DNode(3)
#     stackLL.insert(Dnode3, 1)
#     assert stackLL.head.data == 1
#     assert stackLL.tail.data == 2
#     assert stackLL.size == 3
#     assert stackLL.head.next.data == 3
#     assert stackLL.head.next.next.data == 2
    
#     # Test 4: Insert at invalid index
#     Dnode4 = DNode(4)
#     exceptionRaised = False
#     try:
#         stackLL.insert(Dnode4, -1)
#     except:
#         exceptionRaised = True
#     assert exceptionRaised
#     assert stackLL.head.data == 1
#     assert stackLL.tail.data == 2
#     assert stackLL.size == 3
    
#     # Test 5: Insert at invalid index
#     Dnode5 = DNode(5)
#     exceptionRaised = False
#     try:
#         stackLL.insert(Dnode5, 4)
#     except:
#         exceptionRaised = True
#     assert exceptionRaised
#     assert stackLL.head.data == 1
#     assert stackLL.tail.data == 2
#     assert stackLL.size == 3
    
# def test_stackLL_isSorted():
#     # Test 1: Empty list
#     stackLL = stackLL()
#     assert stackLL.isSorted() == True

#     # Test 2: Single element list
#     Dnode1 = DNode(1)
#     stackLL.insertTail(Dnode1)
#     assert stackLL.isSorted() == True

#     # Test 3: Sorted list
#     Dnode2 = DNode(2)
#     stackLL.insertTail(Dnode2)
#     assert stackLL.isSorted() == True

#     # Test 4: Unsorted list
#     Dnode3 = DNode(3)
#     stackLL.insertHead(Dnode3)
#     assert stackLL.isSorted() == False

# def test_stackLL_sortedInsert():
#     # Test 1: Empty list
#     stackLL = stackLL()
#     Dnode1 = DNode(1)
#     stackLL.sortedInsert(Dnode1)
#     assert stackLL.head.data == 1
#     assert stackLL.tail.data == 1
#     assert stackLL.size == 1

#     # Test 2: Insert at tail
#     Dnode2 = DNode(4)
#     stackLL.sortedInsert(Dnode2)
#     assert stackLL.head.data == 1
#     assert stackLL.tail.data == 4
#     assert stackLL.size == 2

#     # Test 3: Insert at head
#     Dnode3 = DNode(1)
#     stackLL.sortedInsert(Dnode3)
#     assert stackLL.head.data == 1
#     assert stackLL.tail.data == 4
#     assert stackLL.size == 3

#     # Test 4: Insert in middle
#     Dnode4 = DNode(3)
#     stackLL.sortedInsert(Dnode4)
#     assert stackLL.head.data == 1
#     assert stackLL.tail.data == 4
#     assert stackLL.size == 4
#     assert stackLL.head.next.data == 1
#     assert stackLL.head.next.next.data == 3

# def test_stackLL_search():
#     # Test 1: Empty list
#     stackLL = stackLL()
#     Dnode1 = DNode(1)
#     assert stackLL.search(Dnode1) == None

#     # Test 2: Single element list
#     stackLL.insertTail(Dnode1)
#     assert stackLL.search(Dnode1) == Dnode1

#     # Test 3: Multiple element list
#     Dnode2 = DNode(2)
#     stackLL.insertTail(Dnode2)
#     assert stackLL.search(Dnode1) == Dnode1
#     assert stackLL.search(Dnode2) == Dnode2

#     # Test 4: Not found
#     Dnode3 = DNode(3)
#     assert stackLL.search(Dnode3) == None

# def test_stackLL_deleteHead():
#     # Test 1: Empty list
#     stackLL = stackLL()
#     stackLL.deleteHead()
#     assert stackLL.head == None
#     assert stackLL.tail == None
#     assert stackLL.size == 0

#     # Test 2: Single element list
#     Dnode1 = DNode(1)
#     stackLL.insertTail(Dnode1)
#     stackLL.deleteHead()
#     assert stackLL.head == None
#     assert stackLL.tail == None
#     assert stackLL.size == 0

#     # Test 3: Multiple element list
#     Dnode2 = DNode(2)
#     Dnode3 = DNode(3)
#     Dnode4 = DNode(4)
#     stackLL.insertTail(Dnode2)
#     stackLL.insertTail(Dnode3)
#     stackLL.insertTail(Dnode4)
#     stackLL.deleteHead()
#     assert stackLL.head.data == 3
#     assert stackLL.tail.data == 4
#     assert stackLL.size == 2
# def test_stackLL_deleteTail():
#     # Test 1: Empty list
#     stackLL = stackLL()
#     stackLL.deleteTail()
#     assert stackLL.head == None
#     assert stackLL.tail == None
#     assert stackLL.size == 0

#     # Test 2: Single element list
#     Dnode1 = DNode(1)
#     stackLL.insertTail(Dnode1)
#     stackLL.deleteTail()
#     assert stackLL.head == None
#     assert stackLL.tail == None
#     assert stackLL.size == 0

#     # Test 3: Multiple element list
#     Dnode2 = DNode(2)
#     Dnode3 = DNode(3)
#     Dnode4 = DNode(4)
#     stackLL.insertTail(Dnode2)
#     stackLL.insertTail(Dnode3)
#     stackLL.insertTail(Dnode4)
#     stackLL.deleteTail()
#     assert stackLL.head.data == 2
#     assert stackLL.tail.data == 3
#     assert stackLL.size == 2

# def test_stackLL_delete():
#     # Test 1: Empty list
#     stackLL = stackLL()
#     Dnode1 = DNode(1)
#     stackLL.delete(Dnode1)
#     assert stackLL.head == None
#     assert stackLL.tail == None
#     assert stackLL.size == 0

#     # Test 2: Single element list
#     stackLL.insertTail(Dnode1)
#     stackLL.delete(Dnode1)
#     assert stackLL.head == None
#     assert stackLL.tail == None
#     assert stackLL.size == 0

#     # Test 3: Delete middle element
#     Dnode2 = DNode(2)
#     Dnode3 = DNode(3)
#     Dnode4 = DNode(4)
#     stackLL.insertTail(Dnode1)
#     stackLL.insertTail(Dnode2)
#     stackLL.insertTail(Dnode3)
#     stackLL.insertTail(Dnode4)
#     stackLL.delete(Dnode3)
#     assert stackLL.head.data == 1
#     assert stackLL.tail.data == 4
#     assert stackLL.size == 3
#     assert stackLL.head.next.data == 2
#     assert stackLL.head.next.next.data == 4

#     # Test 4: Delete head
#     stackLL.delete(Dnode1)
#     assert stackLL.head.data == 2
#     assert stackLL.tail.data == 4
#     assert stackLL.size == 2
#     assert stackLL.head.next.data == 4
#     assert stackLL.tail.data == 4

#     # Test 5: Not found
#     Dnode5 = DNode(5)
#     stackLL.delete(Dnode5)
#     assert stackLL.head.data == 2
#     assert stackLL.tail.data == 4
#     assert stackLL.size == 2

# def test_stackLL_sort():
#     # Test 1: Empty list
#     stackLL = stackLL()
#     stackLL.sort()
#     assert stackLL.head == None
#     assert stackLL.tail == None
#     assert stackLL.size == 0

#     # Test 2: Single element list
#     Dnode1 = DNode(1)
#     stackLL.insertTail(Dnode1)
#     stackLL.sort()
#     assert stackLL.head.data == 1
#     assert stackLL.tail.data == 1
#     assert stackLL.size == 1

#     # Test 3: Multiple element list
#     Dnode2 = DNode(2)
#     Dnode3 = DNode(3)
#     Dnode4 = DNode(4)
#     stackLL.insertTail(Dnode4)
#     stackLL.insertTail(Dnode3)
#     stackLL.insertTail(Dnode2)
#     stackLL.sort()
#     assert stackLL.head.data == 1
#     assert stackLL.tail.data == 4
#     assert stackLL.size == 4
#     assert stackLL.head.next.data == 2
#     assert stackLL.head.next.next.data == 3
#     assert stackLL.head.next.next.next.data == 4

# def test_stackLL_clear():
#     # Test 1: Empty list
#     stackLL = stackLL()
#     stackLL.clear()
#     assert stackLL.head == None
#     assert stackLL.tail == None
#     assert stackLL.size == 0

#     # Test 2: Single element list
#     Dnode1 = DNode(1)
#     stackLL.insertTail(Dnode1)
#     stackLL.clear()
#     assert stackLL.head == None
#     assert stackLL.tail == None
#     assert stackLL.size == 0

#     # Test 3: Multiple element list
#     Dnode2 = DNode(2)
#     Dnode3 = DNode(3)
#     Dnode4 = DNode(4)
#     stackLL.insertTail(Dnode2)
#     stackLL.insertTail(Dnode3)
#     stackLL.insertTail(Dnode4)
#     stackLL.clear()
#     assert stackLL.head == None
#     assert stackLL.tail == None
#     assert stackLL.size == 0