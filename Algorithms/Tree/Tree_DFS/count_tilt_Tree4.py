class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        result= [0]
        def helper(node):
            
            if not node.left and not node.right:
                return node.val

            leftval = 0
            rightval = 0

            if node.left:
                leftval = helper(node.left)
                
            if node.right: 
                rightval = helper(node.right)
            
            mytilt = abs(leftval-rightval)
            result[0] += mytilt
            
            return node.val + rightval + leftval
        
        helper(root)
        return result[0]
        