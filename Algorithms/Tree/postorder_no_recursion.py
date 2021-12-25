from collections import deque

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
        print(self.val)
        if self.left:
            elements += self.left.in_order()

        elements.append(self.val)
        if self.right:
            elements += self.right.in_order()
        return(elements)

tree = Node(100)
tree.left = Node(200)
tree.right = Node(300)
tree.left.left = Node(400)
tree.left.right = Node(500)

result = []

def helper(root):
    q = deque()
    q.append(root)

    while q:

        len_q = len(q)
        temp = []
        for _ in range(len_q):

            new_node = q.pop()

            if new_node:
                q.append(new_node.left)
                q.append(new_node.right)
                result.append(new_node.val)

helper(tree)
print(result[::-1])