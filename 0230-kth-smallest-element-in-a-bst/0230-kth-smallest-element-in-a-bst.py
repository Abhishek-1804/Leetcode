# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        counter = 0
        result = 0

        def inorder(node):
            nonlocal counter, result

            if not node:
                return
             
            inorder(node.left)
            counter += 1
            if counter == k:
                result = node.val
                return
            inorder(node.right)

        inorder(root)
        return result