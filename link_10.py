class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class doublyLL:
    def __init__(self):
        self.head = None

    def for_traversal(self):
        if self.head is None:
            print("LinkedList is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.nref

    def back_traversal(self):
        if self.head is None:
            print("LinkedList is empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref 
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.pref

obj = doublyLL()
obj.for_traversal()


