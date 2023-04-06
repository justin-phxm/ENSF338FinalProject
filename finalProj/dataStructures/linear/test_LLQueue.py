# from queueLL import queueLL
from DNode import DNode
from QueueLL import QueueLL
def test_queueLL_Constructors():
    # Test 1: Empty queueLL
    queueLL = QueueLL()
    assert queueLL.head == None
    assert queueLL.tail == None
    assert queueLL.size == 0
    DmyNode = DNode(1)

    # Test 2: Non-empty queueLL
    queueLL1 = QueueLL(DmyNode)
    assert queueLL1.head.data == 1
    assert queueLL1.tail.data == 1
    assert queueLL1.size == 1

def test_queueLL_len():
    # Test 1: Empty queueLL
    queueLL = QueueLL()
    assert len(queueLL) == 0

    # Test 2: Non-empty queueLL
    DmyNode = DNode(1)
    queueLL1 = QueueLL(DmyNode)
    assert len(queueLL1) == 1

def test_queueLL_insertHead():
    # Test 1: Insert into empty queueLL
    queueLL = QueueLL()
    Dnode1 = DNode(1)
    queueLL.insertHead(Dnode1)
    assert queueLL.head == None
    assert queueLL.tail == None
    assert queueLL.size == 0

def test_queueLL_insertTail():
    # Test 1: Insert into empty queueLL
    queueLL = QueueLL()
    Dnode1 = DNode(1)
    queueLL.insertTail(Dnode1)
    assert queueLL.head == Dnode1
    assert queueLL.size == 1

def test_queueLL_enqueue():
    # Test 1: Insert into empty queueLL
    queueLL = QueueLL()
    Dnode1 = DNode(1)
    queueLL.enqueue(Dnode1)
    assert queueLL.head == Dnode1
    assert queueLL.size == 1

def test_queueLL_insert():
    # Test 1: Insert at head
    queueLL = QueueLL()
    Dnode1 = DNode(1)
    queueLL.insert(Dnode1, 0)
    assert queueLL.head== None
    assert queueLL.tail == None
    assert queueLL.size == 0
    
def test_queueLL_isSorted():
    queueLL = QueueLL()
    # Test 1: Empty list
    assert queueLL.isSorted() == True

    # Test 2: Single element list
    Dnode1 = DNode(1)
    queueLL.enqueue(Dnode1)
    assert queueLL.isSorted() == True

    # Test 3: Sorted list
    Dnode2 = DNode(2)
    queueLL.enqueue(Dnode2)
    assert queueLL.isSorted() == True

    # Test 4: Unsorted list
    Dnode3 = DNode(1)
    queueLL.enqueue(Dnode3)
    assert queueLL.isSorted() == False

def test_queueLL_sortedInsert():
    # Test 1: Empty list
    queueLL = QueueLL()
    Dnode1 = DNode(1)
    queueLL.sortedInsert(Dnode1)
    assert queueLL.head == None
    assert queueLL.tail == None
    assert queueLL.size == 0

def test_queueLL_search():
    queueLL = QueueLL()
    # Test 1: Empty list
    Dnode1 = DNode(1)
    assert queueLL.search(Dnode1) == None

    # Test 2: Single element list
    queueLL.enqueue(Dnode1)
    assert queueLL.search(Dnode1) == Dnode1

    # Test 3: Multiple element list
    Dnode2 = DNode(2)
    queueLL.enqueue(Dnode2)
    assert queueLL.search(Dnode1) == Dnode1
    assert queueLL.search(Dnode2) == Dnode2

    # Test 4: Not found
    Dnode3 = DNode(3)
    assert queueLL.search(Dnode3) == None

def test_queueLL_deleteHead():
    queueLL = QueueLL()
    Dnode1 = DNode(1)
    # Test 1: Single element list
    queueLL.enqueue(Dnode1)
    queueLL.deleteHead()
    assert queueLL.head == Dnode1
    assert queueLL.tail == Dnode1
    assert queueLL.size == 1

def test_queueLL_dequeue():
    queueLL = QueueLL()
    Dnode1 = DNode(1)
    Dnode2 = DNode(2)
    Dnode3 = DNode(3)
    # Test 1: Single element list
    queueLL.enqueue(Dnode1)
    returnNode = queueLL.dequeue()
    assert queueLL.head == None
    assert queueLL.tail == None
    assert queueLL.size == 0
    assert returnNode == Dnode1

    # Test 2: Multiple element list
    queueLL.enqueue(Dnode1)
    queueLL.enqueue(Dnode2)
    queueLL.enqueue(Dnode3)
    returnNode = queueLL.dequeue()
    assert queueLL.head == Dnode2
    assert queueLL.tail == Dnode3
    assert queueLL.size == 2
    assert returnNode == Dnode1

def test_queueLL_deleteTail():
    queueLL = QueueLL()
    Dnode1 = DNode(1)
    # Test 1: Single element list
    queueLL.enqueue(Dnode1)
    queueLL.deleteTail()
    assert queueLL.head == Dnode1
    assert queueLL.tail == Dnode1
    assert queueLL.size == 1

def test_queueLL_delete():
    queueLL = QueueLL()
    Dnode1 = DNode(1)
    # Test 1: Single element list
    queueLL.enqueue(Dnode1)
    queueLL.delete(Dnode1)
    assert queueLL.head == Dnode1
    assert queueLL.tail == Dnode1
    assert queueLL.size == 1

def test_queueLL_sort():
    queueLL = QueueLL()
    Dnode1 = DNode(1)
    Dnode2 = DNode(2)
    Dnode3 = DNode(3)
    Dnode4 = DNode(4)
    # Test 1: Empty list
    queueLL.sort()
    assert queueLL.head == None
    assert queueLL.tail == None
    assert queueLL.size == 0

    # Test 2: Single element list
    queueLL.enqueue(Dnode1)
    queueLL.sort()
    assert queueLL.head.data == 1
    assert queueLL.tail.data == 1
    assert queueLL.size == 1

    # Test 3: Multiple element list
    queueLL.enqueue(Dnode4)
    queueLL.enqueue(Dnode2)
    queueLL.enqueue(Dnode3)
    queueLL.sort()
    assert queueLL.head.data == 1
    assert queueLL.tail.data == 4
    assert queueLL.size == 4
    assert queueLL.head.next.data == 2
    assert queueLL.head.next.next.data == 3
    assert queueLL.head.next.next.next.data == 4

def test_queueLL_clear():
    queueLL = QueueLL()
    Dnode1 = DNode(1)
    Dnode2 = DNode(2)
    Dnode3 = DNode(3)
    Dnode4 = DNode(4)
    # Test 1: Empty list
    queueLL.clear()
    assert queueLL.head == None
    assert queueLL.tail == None
    assert queueLL.size == 0

    # Test 2: Single element list
    queueLL.enqueue(Dnode1)
    queueLL.clear()
    assert queueLL.head == None
    assert queueLL.tail == None
    assert queueLL.size == 0

    # Test 3: Multiple element list
    queueLL.enqueue(Dnode2)
    queueLL.enqueue(Dnode3)
    queueLL.enqueue(Dnode4)
    queueLL.clear()
    assert queueLL.head == None
    assert queueLL.tail == None
    assert queueLL.size == 0