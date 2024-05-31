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
                print(n.data,"-->",end=" ")
                n=n.ref
    # add element to the beginning of the list
    def add_end(self,data):
        new_node = Node(data)
        if  self.head is None:
            self.head = new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref = new_node
        

ll1 = LinkedList()
ll1.add_end(10)
ll1.add_end(200)
ll1.add_end(20)
print(ll1.printList())