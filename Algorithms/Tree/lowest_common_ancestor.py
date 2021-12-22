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


tree = Node(6)
tree.left = Node(2)
tree.right = Node(8)
tree.right.right = Node(8)
tree.right.left = Node(0)

tree.left.left = Node(6)
tree.left.right = Node(2)
tree.left.right.left = Node(7)
tree.left.right.right = Node(4)

tree.in_order()


def helper(root, p, q):

    cur = root

    while cur:
        if p.val > cur.val and q.val > cur.val:
            cur = cur.val

        elif p.val < cur.val and q.val < cur.val:
            cur = cur.left
        else:
            return cur


store = helper(tree, 2, 8)

print(store)