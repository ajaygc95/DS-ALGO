class TreeNode:

    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None

    def insert(self, root, item):

        if not root:
            return TreeNode(item)
        
        if root.val == item :
            return root
        if item < root.val:
            root.left = self.insert(root.left, item)
        else:
            root.right= self.insert(root.right, item)
        
        return root

    def get_level(self):
        level = 0
        curr = self

        while curr.left:
            level += 1
            curr = curr.left
        level+= 1
        return level


    def view(self, node):
        print(node.val)
        if node.left:
            self.view(node.left)
        if node.right:
            self.view(node.right)
        

tree = TreeNode(10)
tree.insert(tree, 20)
tree.insert(tree, 30)
tree.insert(tree, 40)
tree.insert(tree, 8)
tree.insert(tree, 6)
tree.insert(tree, 2)
tree.insert(tree, 7)

tree.view(tree)
class SearchTarget:
    def searchBST(self, root, target):

        res = [False]
        def search(node):
            if not node:
                return 
            if node.val == target:
                res[0] = True

            
            if target < node.val:
                search(node.left)
            else:
                search(node.right)
 
            
        search(root)
        return res[0]

searchTarget = SearchTarget()
return_value =searchTarget.searchBST(tree, 19)
print(return_value)
    
    


    


