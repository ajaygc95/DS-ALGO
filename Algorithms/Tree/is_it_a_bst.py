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

input = [5,4,7,1,11,12,15,3]

tree = Node(5)

# for item in range(1,len(input)):
#     tree.insert(input[item])

tree.right = Node(5)
tree.right.right = Node(5)
tree.left = Node(5)
tree.left.left = Node(5)


box = [[True]]
def helper(node):

    if not node.left and not node.right: 
        print("last step")
        box[0] = True
        return 

    if node.left:
        print(f"node: {node.val}, left: {node.left.val}")

        if node.left.val > node.val:
            box[0] = False
            return
        else:
            helper(node.left)

    if node.right:
        print(f"node: {node.val}, right: {node.right.val}")
        if node.right.val < node.val:
           box[0] = False
           return
        else:
            helper(node.right)
    
# tree.in_order()

helper(tree)
print(box[0])
