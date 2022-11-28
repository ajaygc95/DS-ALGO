class TreeNode:
    def __init__(self, val=0) -> None:
        self.val = val
        self.left = None
        self.right = None
    

    def insert(self,key):   
        print("Inserting:", key)
        
        curr = self
        prev = None
        while curr:
            if key == curr.val:
                return
            elif key < curr.val:
                prev = curr
                curr = curr.left
            else:
                prev = curr
                curr = curr.right
    
        new_node = TreeNode(key)

        if key < prev.val:
            prev.left = new_node
        else:
            prev.right = new_node


    def view(self, node, res):
        res.append(node.val)
        if node.left:
            self.view(node.left,res)
        if node.right:
            self.view(node.right,res)
        return res

    def tree_min(self):
        curr = self
        while curr.left:
            curr = curr.left
        
        return curr.val
    
    def max_tree(self):
        curr = self
        while curr.right:
            curr = curr.right
        return curr.val
    
    
def succesor(root, node):
    if not root:
        return 
    curr = root
    prev = None

    while curr:
        print(curr.val)
        if curr == node:
            break

        if node.val < curr.val:
            print("left", curr.val)
            prev = curr
            curr = curr.left
        else:
            curr = curr.right
    print("after while loop", curr.val, prev.val)
    if curr.right:
        while curr.right:
            curr = curr.right
        return curr.val
    
    return prev.val



    
def predecessor(root, node):
    print("pred")
    if not root:
        return 
    curr = root
    ancester = None
    while curr:
        print(curr.val)
        if curr == node:
            break
        if node.val < curr.val:
            curr = curr.left
        else:
            print("last right", curr.val)
            ancester = curr
            curr = curr.right
    if curr.left:
        while curr.left:
            curr = curr.left
        return curr.val
    
    return ancester.val
    


       
tree = TreeNode(17)

tree.insert(10)
tree.insert(5)
tree.insert(0)
tree.insert(15)
tree.insert(16)
tree.insert(11)
tree.insert(20)
tree.insert(25)
tree.insert(18)
tree.insert(22)
tree.insert(23)
tree.insert(24)
result = tree.view(tree, [])
print(result)
# print(tree.tree_min())
# print(tree.max_tree())
two_two = tree.right.right.left.right.right
succ = succesor(tree, two_two)
pred = predecessor(tree, two_two)
print(f"pred: {pred} succ: {succ}")
