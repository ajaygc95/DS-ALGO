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


node1 = Node(1)
node1.left = Node(2)
node1.right = Node(3)
node1.left.right = Node(5)
node1.left.left = Node(4)
# node1.left.right = Node(5)

def helper(root):

    if not root.left:
        return root
    
    new_root = helper(root.left)
    
    root.left.left = root.right
    root.left.right = root

    root.right = None
    root.left = None

    # new_root.left = root.right
    # new_root.right = root
    # root.right = None
    # root.left = None

    return new_root



store = helper(node1)
store.in_order()
