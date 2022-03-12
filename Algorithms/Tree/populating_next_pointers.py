class Node:
    def __init__(self, val ) -> None:
        self.val = val
        self.right = None
        self.left = None
        self.next =None

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
node1.right = Node(3) 

node1.left.left = Node(4)
node1.left.right = Node(5)
node1.right.right = Node(6)
node2 = None
# node1.in_order()

from collections import deque
from sqlite3 import paramstyle


''' 
zig-zag

'''

parent = {}
def helper(root,x,y):

    parent[root.val] = None
    if not root:
        return []

    q = deque()
    q.append(root)

    while q:
        
        len_q = len(q)
        for x,y in enumerate( range(len_q)):

            node= q.popleft()

            if x != len_q-1:
                node.next = q[0]
            else:
                node.next = None
                pass
            print(x, len_q-1, node.val)


            if node.left :
                q.append(node.left)
            
            if node.right:
                q.append(node.right)
        
    return root
        


store = helper(node1,2,3)
print(store.next)