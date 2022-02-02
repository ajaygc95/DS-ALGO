
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

        elements.append(self.val)
        print(self.val)
        if self.left:
            elements += self.left.in_order()

        if self.right:
            elements += self.right.in_order()

        return (elements)

node1 = Node(10)
node1.left = Node(5)
node1.left.left = Node(4)
node1.left.right = Node(6)
node1.right = Node(15)
node1.right.left = Node(12)
node1.right.right = Node(20)


def is_it_a_bst(root):

    if not root:
        return 

    isItBST = [True]

    def helper(node):

        amibst = True
        smallest, largest = node.val, node.val

        if node.left:
            (s,l,b) = helper(node.left)
            smallest = min(smallest, s)
            largest = max(largest, l)
            if not b or l >= node.val:
                amibst = False

        if node.right:
            (s, l, b) = helper(node.right)
            smallest = min(smallest, s)
            largest = max(largest, l)

            if not b or s <= node.val:
                amibst = False
        
        if amibst == False:
            isItBST[0] = False
        
        return (smallest, largest, amibst)

    helper(root)
    return isItBST

store = is_it_a_bst(node1)
print(store)