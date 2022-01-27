import collections


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


def bfs(root):

    if root is None:
        return []

    result = []

    q = collections.deque()
    q.append((root,[]))

    while q:
        (node, slate) = q.popleft()

        slate += [node.val]
        if node.left :
            q.append((node.left, slate[:]))

        if node.right:
            q.append((node.right, slate[:]))
        
        if not node.left and not node.right:
            result.append(slate[:])
    
    return result


store = bfs(node1)

for item in store:
    print(item)
