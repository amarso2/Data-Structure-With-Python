class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
class LinkedList:
    def __init__(self):
        self.head = None
    # travesal linked list
    def printList(self):
        if self.head is None:
            print("List is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,end=" ")
                n=n.ref
ll1 =LinkedList()
ll1.printList()