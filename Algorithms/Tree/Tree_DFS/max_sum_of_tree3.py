def maxPathSum(self, root: Optional[TreeNode]) -> int:
    
    
    if not root: return 
    
    max_path = [root.val]
    
    def dfs(node):
        
        my_max = node.val
        mytotal = node.val
        
        if node.left:
            left = dfs(node.left)
            my_max = max(my_max, left + node.val)
            mytotal = my_max
            
        if node.right:
            right = dfs(node.right)
            my_max = max(my_max, right + node.val)
            
            mytotal = max(mytotal, node.val + right, mytotal + right)
    
        max_path[0] = max(mytotal, max_path[0])
        
        return my_max
    
    dfs(root)
    return max_path[0]