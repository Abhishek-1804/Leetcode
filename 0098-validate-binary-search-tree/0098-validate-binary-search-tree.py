# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node, upper = float('inf'), lower = float('-inf')):

            if not node:
                return True
            
            if node.val <= lower or node.val >= upper:
                return False
            
            l = helper(node.left, node.val, lower)
            r = helper(node.right, upper, node.val)

            return l and r

        return helper(root)