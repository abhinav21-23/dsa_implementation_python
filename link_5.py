class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traversal(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end=" ")
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref 
            n.ref = new_node

    def after_node(self, data, x):
        n = self.head
        while n is not None:
            if x==n.data:
                break
            n = n.ref
        if n is None:
            print("Node is not present in the linked list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
        
    def before_node(self, data, x):
        if self.head is None:
            print("Linked is empty")
            return
        if self.head.data==x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not present in the linked list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

obj = LinkedList()
obj.add_begin(10)
obj.add_begin(20)
obj.add_end(30)
obj.after_node(40, 20)
obj.before_node(50, 10)
obj.traversal()