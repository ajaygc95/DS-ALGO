from collections import deque 


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
        elements.append(self.val)
        print(self.val)
        if self.right:
            elements += self.right.in_order()
        return(elements)

node1 = Node(100)
node1.right = Node(120)
node1.left = Node(50)
node1.left.left = Node(40)
node1.left.right = Node(45)
node1.left.left.left = Node(20)


def overall(root):
    if not root: return 0
    globaldia = [[0]]

    def helper(root):
        if not root.left and not root.right:
            return 0
        mydia = 0
        if root.left:
            LH = helper(root.left)
            myheight = 1 + LH
            mydia = 1 + LH

        if root.right:
            RH = helper(root.right)
            myheight = max(myheight, 1+RH)
            mydia += RH + 1

        globaldia[0][0] = max(globaldia[0][0] ,mydia) 

        return myheight

    helper(root)

    return globaldia


store = overall(node1)
print(store)