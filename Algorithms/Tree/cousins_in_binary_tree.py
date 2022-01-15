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
node1.right = Node(3)
node1.left.left = Node(4)
node1.right.right = Node(5)
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
    count = 0
    while q:
        
        len_q = len(q)
        for _ in range(len_q):
            node= q.popleft()
            
            if node.left :
                parent[node.left.val] = (node.val, count)
                q.append(node.left)
            
            if node.right:
                parent[node.right.val] = (node.val, count)
                q.append(node.right)
            
            if node.val == x:
                x = (node.val, count)
            if node.val == y:
                y = (node.val, count)
            


        count += 1
    for key, val in parent.items():
        print(key,val)

    print(x[1],y[1])
    print(x,y)
    if x[1] == y[1] and parent[x[0]] != parent[y[0]]:
        return True

    return False

store = helper(node1,2,3)
print(store)