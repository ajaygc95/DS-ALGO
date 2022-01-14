from collections import deque
class Node:
    def __init__(self, val ) -> None:
        self.val = val
        self.children = None

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

node1.children = Node(9)
node1.children = Node(20)
node1.children = Node(15)

node1.children.children = Node(27)

result = []
def helper(root):

    q = deque()
    q.append(root)

    while q:
        node = q.popleft()
        for child in node.children:
            result.append(child)
        q.append(node)



helper(node1)

print(result)