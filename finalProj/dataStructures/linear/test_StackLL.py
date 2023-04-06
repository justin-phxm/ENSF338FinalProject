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

def test_stackLL_push():
    # Test 1: Insert into empty stackLL
    stackLL = StackLL()
    Dnode1 = DNode(1)
    stackLL.push(Dnode1)
    assert stackLL.head.data == 1
    assert stackLL.tail.data == 1
    assert stackLL.size == 1
    
    # Test 2: Insert into non-empty stackLL
    Dnode2 = DNode(2)
    stackLL.push(Dnode2)
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

def test_stackLL_insert():
    # Test 1: Insert at head
    stackLL = StackLL()
    Dnode1 = DNode(1)
    stackLL.insert(Dnode1, 0)
    assert stackLL.head== None
    assert stackLL.tail == None
    assert stackLL.size == 0
    
def test_stackLL_isSorted():
    stackLL = StackLL()
    # Test 1: Empty list
    assert stackLL.isSorted() == True

    # Test 2: Single element list
    Dnode1 = DNode(1)
    stackLL.push(Dnode1)
    assert stackLL.isSorted() == True

    # Test 3: Sorted list
    Dnode2 = DNode(2)
    stackLL.push(Dnode2)
    assert stackLL.isSorted() == False

    # Test 4: Unsorted list
    Dnode3 = DNode(3)
    stackLL.push(Dnode3)
    assert stackLL.isSorted() == False

def test_stackLL_sortedInsert():
    # Test 1: Empty list
    stackLL = StackLL()
    Dnode1 = DNode(1)
    stackLL.sortedInsert(Dnode1)
    assert stackLL.head == None
    assert stackLL.tail == None
    assert stackLL.size == 0

def test_stackLL_search():
    stackLL = StackLL()
    # Test 1: Empty list
    Dnode1 = DNode(1)
    assert stackLL.search(Dnode1) == None

    # Test 2: Single element list
    stackLL.push(Dnode1)
    assert stackLL.search(Dnode1) == Dnode1

    # Test 3: Multiple element list
    Dnode2 = DNode(2)
    stackLL.push(Dnode2)
    assert stackLL.search(Dnode1) == Dnode1
    assert stackLL.search(Dnode2) == Dnode2

    # Test 4: Not found
    Dnode3 = DNode(3)
    assert stackLL.search(Dnode3) == None

def test_stackLL_deleteHead():
    stackLL = StackLL()
    Dnode1 = DNode(1)
    # Test 1: Single element list
    stackLL.push(Dnode1)
    stackLL.deleteHead()
    assert stackLL.head == Dnode1
    assert stackLL.tail == Dnode1
    assert stackLL.size == 1

def test_stackLL_pop():
    stackLL = StackLL()
    Dnode1 = DNode(1)
    # Test 1: Single element list
    stackLL.push(Dnode1)
    poppedNode = stackLL.pop()
    assert stackLL.head == None
    assert stackLL.tail == None
    assert stackLL.size == 0
    assert poppedNode == Dnode1

def test_stackLL_deleteTail():
    stackLL = StackLL()
    Dnode1 = DNode(1)
    # Test 1: Single element list
    stackLL.push(Dnode1)
    stackLL.deleteTail()
    assert stackLL.head == Dnode1
    assert stackLL.tail == Dnode1
    assert stackLL.size == 1

def test_stackLL_delete():
    stackLL = StackLL()
    Dnode1 = DNode(1)
    # Test 1: Single element list
    stackLL.push(Dnode1)
    stackLL.delete(Dnode1)
    assert stackLL.head == Dnode1
    assert stackLL.tail == Dnode1
    assert stackLL.size == 1

def test_stackLL_sort():
    stackLL = StackLL()
    Dnode1 = DNode(1)
    Dnode2 = DNode(2)
    Dnode3 = DNode(3)
    Dnode4 = DNode(4)
    # Test 1: Empty list
    stackLL.sort()
    assert stackLL.head == None
    assert stackLL.tail == None
    assert stackLL.size == 0

    # Test 2: Single element list
    stackLL.push(Dnode1)
    stackLL.sort()
    assert stackLL.head.data == 1
    assert stackLL.tail.data == 1
    assert stackLL.size == 1

    # Test 3: Multiple element list
    stackLL.push(Dnode4)
    stackLL.push(Dnode2)
    stackLL.push(Dnode3)
    stackLL.sort()
    assert stackLL.head.data == 1
    assert stackLL.tail.data == 4
    assert stackLL.size == 4
    assert stackLL.head.next.data == 2
    assert stackLL.head.next.next.data == 3
    assert stackLL.head.next.next.next.data == 4

def test_stackLL_clear():
    stackLL = StackLL()
    Dnode1 = DNode(1)
    Dnode2 = DNode(2)
    Dnode3 = DNode(3)
    Dnode4 = DNode(4)
    # Test 1: Empty list
    stackLL.clear()
    assert stackLL.head == None
    assert stackLL.tail == None
    assert stackLL.size == 0

    # Test 2: Single element list
    stackLL.push(Dnode1)
    stackLL.clear()
    assert stackLL.head == None
    assert stackLL.tail == None
    assert stackLL.size == 0

    # Test 3: Multiple element list
    stackLL.push(Dnode2)
    stackLL.push(Dnode3)
    stackLL.push(Dnode4)
    stackLL.clear()
    assert stackLL.head == None
    assert stackLL.tail == None
    assert stackLL.size == 0