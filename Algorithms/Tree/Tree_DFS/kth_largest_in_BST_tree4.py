class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        kth = [0]
        
        def dfs(node, pred, k):
            
            if pred >= k:
                return pred
            
            # Base Case     
            if not node.left and not node.right:
                
                pred += 1 
                
                if pred == k:
                    kth[0] = node.val
                return pred
            
            # Recursion 
            if node.left:
                pred = dfs(node.left,pred, k)
            
            pred +=1 
            if pred == k:
                kth[0] = node.val
                
            if node.right:
                pred = dfs(node.right, pred, k)
                
            return pred
        
        dfs(root, 0, k)
        
        return kth[0]