'''Implement a stack using a linked list in Python with operations such as push, pop, peek, isEmpty, and size.'''

class myStack:

    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, x):
        newNode = Node(x)
        newNode.next = self.top
        self.top = newNode
        self.count += 1

    def pop(self):
        if self.top is None:
            return -1

        value = self.top.data
        self.top = self.top.next
        self.count -= 1

        return value

    def peek(self):
        if self.top is None:
            return -1

        return self.top.data

    def isEmpty(self):
        return self.top is None

    def size(self):
        return self.count