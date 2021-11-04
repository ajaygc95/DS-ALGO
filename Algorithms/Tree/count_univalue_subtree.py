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
        print(self.val)
        if self.left:
            elements += self.left.in_order()

        elements.append(self.val)
        if self.right:
            elements += self.right.in_order()
        return(elements)

node1 = Node(5)
node1.left = Node(1)
node1.right = Node(5)
node1.right.right = Node(5)
node1.left.left = Node(5)
node1.left.right = Node(5)

def overall(root):

    globalcount = [0]

    def helper(node):

        if not node.left and not node.right:
            globalcount[0] += 1
            return True
        amiunival = True
        if node.left:

            LH = helper(node.left)

            if not LH or node.val != node.left.val:
                amiunival = False


        if node.right:
            RH = helper(node.right)

            if not RH or node.val != node.right.val:
                amiunival = False

        if amiunival:
            globalcount[0] += 1


        return amiunival
    helper(root)

    return globalcount[0]

store = overall(node1)
print(store)