import sys
sys.path.insert(0, "..")
from dataStructures.linear.SLL import SLL
from dataStructures.nodes.Node import Node
def main():
    sll = SLL()
    for i in range(10):
        sll.append(i)
    sll.print()

    myNode = Node(11)
    sll.sortedInsert(myNode)
    sll.print()
    
    sll.insertHead(myNode)
    sll.print()
    
    # sll.deleteTail()
    # sll.print()
    # print(sll.search(5))
main()