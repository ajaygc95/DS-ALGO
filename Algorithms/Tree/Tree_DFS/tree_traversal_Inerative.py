from collections import deque
from difflib import restore
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

        return(elements)

node1 = Node(1)
node1.left = Node(3)
node1.right = Node(2)

node1.left.left = Node(5)
node1.right.right = Node(9)

node1.left.left.left = Node(6)
node1.right.right.right = Node(7)


def helper(root):

    if root is None:
        return []

    result = []

    stack = [(root, None)]


    while len(stack) !=0:
        (node, zone) = (stack[-1])

        if zone is None:
            stack[-1] = (node, "arrival")

            if node.left:
                stack.append((node.left, None))
        elif zone == "arrival":
            stack[-1] = (node, "interim")

            if node.right:
                stack.append((node.right, None))

        elif zone == "interim":
            stack[-1] = (node, "departure")
            result.append(node.val)
            stack.pop()
    return result


# node1.in_order()
store = helper(node1)
print(store)