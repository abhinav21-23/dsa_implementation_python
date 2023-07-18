class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

# node1 = Node(10)
# print(node1)
class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:   
                print(n.data)
                n = n.ref

obj = LinkedList()
obj.print_LL()