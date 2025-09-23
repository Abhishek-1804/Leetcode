# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        def dfs(node, parent_val, l):
            if not node:
                return l
            
            if node.val == parent_val + 1:
                l += 1
            else:
                l = 1

            left = dfs(node.left, node.val, l)
            right = dfs(node.right, node.val, l)
            return max(l, left, right)

        if not root:
            return 0
        return dfs(root, root.val - 1, 0)