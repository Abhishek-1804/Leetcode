# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        max_len = 0
        
        def dfs(node):
            nonlocal max_len

            if not node:
                return 0
            
            left_len = dfs(node.left)
            right_len = dfs(node.right)
            
            curr = 1
            if node.left and node.left.val == node.val + 1:
                curr = max(curr, 1 + left_len)
            if node.right and node.right.val == node.val + 1:
                curr = max(curr, 1 + right_len)
            
            max_len = max(max_len, curr)
            return curr

        dfs(root)
        return max_len