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

    def insert_when_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("LinkedList is not empty")

    def insert_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            new_node.pref = n
            n.nref = new_node
            new_node.nref = None

    def after_node(self, data, x):
        new_node = Node(data)
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                if x==n.data:
                    break
                n = n.nref 
            if n is None:
                print("Node is not present in the linked list")
            else:
                new_node.nref = n.nref 
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node

    def before_node(self, data, x):
        new_node = Node(data)
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                if x==n.data:
                    break
                n = n.nref 
            if n is None:
                print("Node is not present in the linked list")
            else:
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node

obj = doublyLL()
obj.insert_when_empty(10)
obj.insert_end(20)
obj.insert_end(30)
obj.insert_begin(0)
obj.insert_begin(-10)
obj.after_node(40, 20)
obj.before_node(50, 0)
obj.for_traversal()
print()
obj.back_traversal()


