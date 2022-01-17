

from collections import deque
from difflib import restore
from itertools import count
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
node1.left = Node(3)
node1.right = Node(2)

node1.left.left = Node(5)
node1.right.right = Node(9)

node1.left.left.left = Node(6)
node1.right.right.right = Node(7)


def helper(root):
    if root is None:
        return []

    result = []

    q = deque()
    q.append((root, 1))

    countid = 1
    while q:

        len_q = len(q)

        temp = []


        for _ in range(len_q):
            (node,id) = q.popleft()

            if id == countid:
                countid += 1
            else:
                return False

            if node.left:
                q.append((node.left,2*id))
            if node.right:
                q.append((node.right, 2*id+1))
            
            # last = id

            # if first is None:
            #     first = id

        # result.append(last-first+1)

    return True



store = helper(node1)
print(store)