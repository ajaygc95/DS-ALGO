class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        inorder = sorted(preorder)

        hash_map = {}

        for index, item in enumerate(inorder):
            hash_map[item] = index

        def dfs(pre_start, pre_end, in_start, in_end):

            if pre_start > pre_end:
                return None
            elif pre_start == pre_end:
                return TreeNode(preorder[pre_start])

            
            root_number = preorder[pre_start]

            inorder_index = hash_map[root_number]

            left_length = inorder_index-in_start

            new_root = TreeNode(root_number)

            new_root.left = dfs(pre_start+1, pre_start+left_length, in_start, inorder_index-1)
            new_root.right = dfs(pre_start+1+left_length, pre_end, inorder_index+1, in_end)

            return new_root

        return dfs(0, len(preorder)-1, 0, len(inorder)-1)