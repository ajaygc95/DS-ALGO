from turtle import left


class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None 
        self.extra = None

root = Node(5)
root.left = Node(3)
root.right =Node(8)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(9)
res1 = []

class Clone:

    def clone_tree(self, root):
        
        hash_map = {}
        def dfs(node):

            copy = Node(node.val)
            hash_map[node] = copy
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

        dfs(root)

        for keys, clone_copy in hash_map.items():
            clone_copy.left = hash_map[keys].left
            clone_copy.right = hash_map[keys].right
            clone_copy.extra = hash_map[keys].extra

        return hash_map[root]

clone1 = Clone()

return_value = clone1.clone_tree(root)
res2 = []

def view(node, res):

    res.append(node.val)
    if node.left:
        view(node.left,res)
    
    if node.right:
        view(node.right,res)
view(root,res1)
view(return_value, res2)
print(res1)
print(res2)

