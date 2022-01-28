import collections
import re

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

node1 = Node(1)
node1.left = Node(2)
node1.left.left = Node(4)
node1.left.right = Node(5)
node1.right = Node(3)
node1.right.left = Node(6)

node1.right.right = Node(7)
node2 = None

result = [0]
def dfs(root, target):
    target = target -root.val

    if not root.left and not root.right:
        if target == 0:
            result[0] = True
    
    if root.left:
        dfs(root.left, target)
    if root.right:
        dfs(root.right, target)


dfs(node1, 7)

print(result[0])
    

