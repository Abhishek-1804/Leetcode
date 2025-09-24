# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:

        count = 0

        def is_unival_tree(node):
            nonlocal count
            
            if not node:
                return True
            
            left_uni = is_unival_tree(node.left)
            right_uni = is_unival_tree(node.right)

            if not left_uni or not right_uni:
                return False
            
            if node.left and node.left.val != node.val:
                return False

            if node.right and node.right.val != node.val:
                return False
            
            count += 1
            return True
        
        is_unival_tree(root)
        return count