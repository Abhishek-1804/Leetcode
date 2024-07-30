# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        min_diff = float('inf')

        def inorder(node):
            if not node:
                return []
            
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        sorted_values = inorder(root)

        for i in range(1, len(sorted_values)):
            min_diff = min(min_diff, abs(sorted_values[i] - sorted_values[i-1]))
        
        return min_diff
