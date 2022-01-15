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

node1 = Node(3)
node1.left = Node(9)
node1.right = Node(20)
node1.right.left = Node(15)

node1.right.right = Node(7)
node2 = None
# node1.in_order()

from collections import deque


''' 
zig-zag

'''
def helper(root):
    
    if not root:
        return []

    q = deque()
    q.append(root)
    result = deque()
    flag = True
    total = (0,None)
    count = -1
    while q:
        count +=1 
        len_q = len(q)
        temp = []

        for _ in range(len_q):
            node = q.popleft()

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)
            temp.append(node.val)

        if sum(temp) > total[0]:
            total = (sum(temp),count)
        
    return total[1]

store = helper(node1)
print(store)