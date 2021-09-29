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

        

tree = Node(input[0])

for item in range(1,len(input)):
    tree.insert(input[item])


# def dfs (node):
#     result = []
#     if not node.left and not node.right:
#         return []

#     if node.left:
#         dfs(node.left)
#     if node.right:
#         dfs(node.right)
    
#     result.append(node.val)
#     return result


def overall(root, sum):
    if not root: return False

    box = [False]




    def dfs(node,target):
        if not node.left and not node.right:
            if target == node.val:
                box[0] = True
            return
            
        if node.left:
            dfs(node.left, target-node.val)
        
        if node.right:
            dfs(node.right, target-node.val)

    dfs(root,sum)
    return box


print(overall(tree, 14))