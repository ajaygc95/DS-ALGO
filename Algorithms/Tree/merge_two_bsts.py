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
        if self.right:
            elements += self.right.in_order()
        return(elements)


node1 = Node(3)
node1.left = Node(2)
node1.left.left = Node(1)
node1.right = Node(4)

node2 = Node(6)
node2.left = Node(5)
node2.right = Node(7)

store1 = node1.in_order()
store2 = node2.in_order()

final = store1 + store2

print(final)