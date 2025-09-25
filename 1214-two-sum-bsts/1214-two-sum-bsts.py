# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        d = {}

        def search(root, val):
            if not root:
                return False
            if root.val == val:
                return True
            elif val < root.val:
                return search(root.left, val)
            else:
                return search(root.right, val)
        
        def traverse(root1):
            if not root1:
                return False
            # search for complement in root2
            if root1 not in d:
                d[root1] = search(root2, target - root1.val)
            if d[root1]:
                return True
            # traverse both subtrees
            return traverse(root1.left) or traverse(root1.right)

        return traverse(root1)