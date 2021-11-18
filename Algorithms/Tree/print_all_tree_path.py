def allPathsOfABinaryTree(root):
    if not root:return
    
    
    result = []
    def helper(root, slate):
        
        if not root.left_ptr and not root.right_ptr:
            slate.append(root.val)
            result.append(slate[:])
            slate.pop()
            return
        
        slate.append(root.val)
        if root.left_ptr:
            helper(root.left_ptr,slate)
        
        if root.right_ptr:
            helper(root.right_ptr, slate)
        slate.pop()
            
    helper(root, [])
    return result