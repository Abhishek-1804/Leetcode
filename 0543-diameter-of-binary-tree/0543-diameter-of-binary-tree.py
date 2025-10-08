# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        max_diameter = float('-inf')
        
        def diameter(node):
            nonlocal max_diameter

            if not node:
                return
            
            left = diameter(node.left)
            right = diameter(node.right)
            max_diameter = max(max_diameter, left + right)

            return 1 + max(left, right)
        
        diameter(root)
        
        return max_diameter