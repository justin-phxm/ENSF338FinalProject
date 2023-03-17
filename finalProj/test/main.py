import sys
sys.path.insert(0, "..")
from dataStructures.linear.SLL import SLL

def main():
    sll = SLL()
    for i in range(10):
        sll.append(i)
    print(sll[8])
main()