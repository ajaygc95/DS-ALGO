from hashlib import new
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

        elements.append(self.val)
        print(self.val)
        if self.left:
            elements += self.left.in_order()

        if self.right:
            elements += self.right.in_order()

        return (elements)

node1 = Node(1)
node1.left = Node(2)
node1.left.left = Node(4)
node1.left.right = Node(5)
node1.right = Node(3)
node1.right.left = Node(6)
node1.right.right = Node(7)

def outer(root):


    new_root = [None]

    def helper(node, parent, rightsibling):

        oldleft = node.left
        oldright = node.right

        node.right = parent
        node.left = rightsibling


        if not oldleft and not oldright:
            new_root[0] = node
        
        if oldleft:
            helper(oldleft, node, oldright)

        
    helper(root, None, None)

    return new_root[0]
    # return final[0]


store = outer(node1)



store.in_order()
# store.in_order()


