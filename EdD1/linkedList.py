from node import Node
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, elem):
        if self.head:
            pass
        else:
            self.head = Node(elem)

