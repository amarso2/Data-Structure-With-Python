# In linked list add element at beginning position
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
    # add element to the beginning of the list
    def add_start(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
        print(data,"is added to the beginning of the list")

ll1 = LinkedList()
ll1.add_start(10)
ll1.add_start(20)
print(ll1.printList())