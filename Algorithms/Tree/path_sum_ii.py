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

node1 = Node(1)
node1.left = Node(2)
node1.right = Node(3)
node1.left.left = Node(4)
node1.left.right = Node(5)


def overall(root):

    globaldia = [0]
    def helper(node):

        if not node.left and not node.right:
            return 0

        mydia = 0
        if node.left:
            LH = helper(node.left)
            mydia = LH + 1
        if node.right:

            RH = helper(node.right)
            mydia += RH + 1


        globaldia[0] = max(globaldia[0], mydia)

        return mydia

    helper(root)
    return globaldia[0]

store = overall(node1)
print(store)


