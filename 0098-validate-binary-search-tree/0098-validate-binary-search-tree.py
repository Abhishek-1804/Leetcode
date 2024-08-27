# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root.left and not root.right:
            return True
        
        if not root.left:
            return root.val < root.right.val and self.isValidBST(root.right)

        elif not root.right:
            return root.left.val < root.val and self.isValidBST(root.left)
        
        return root.left.val < root.val < root.right.val and self.isValidBST(root.left) and self.isValidBST(root.right)