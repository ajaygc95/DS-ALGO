class Node:
    def __init__(self, val ) -> None:
        self.val = val
        self.right = None
        self.left = None

    def insert(self, item):
        new_node = Node(item)
        if self.val is None:
            self.val = new_node
            return

        if item < self.val:
            if self.left:
                self.left.insert(item)
            else:
                self.left = new_node

        else:
            if self.right:
                self.right.insert(item)
            else:
                self.right = new_node

    def in_order(self):
        elements = []

        if self.left:
            elements += self.left.in_order()
        print(self.val)
        elements.append(self.val)
        if self.right:
            elements += self.right.in_order()

        return(elements)

node1 = Node(100)
node1.left = Node(200)
node1.left.left = Node(400)
node1.right = Node(300)
node1.left.right = Node(500)

node1.in_order()

from collections import deque
visited = []

def helpr(root):

    visited.append(root)

    q = deque()
    q.append(root)

    while q :
        new_node = q.popleft()
        for item in adjlist[new_node]:
            print(item)

