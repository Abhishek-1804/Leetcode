# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        largest_bst = 0

        def dfs(node):
            nonlocal largest_bst

            # Empty subtree: valid BST, size 0, min=+inf, max=-inf for easy comparison
            if not node:
                return True, 0, float('inf'), float('-inf')

            l_bst, l_count, l_min, l_max = dfs(node.left)
            r_bst, r_count, r_min, r_max = dfs(node.right)

            # Check BST validity: left and right are BST and their max/min are in range
            if l_bst and r_bst and l_max < node.val < r_min:
                size = 1 + l_count + r_count
                largest_bst = max(largest_bst, size)
                # Update min and max for this subtree
                return True, size, min(l_min, node.val), max(r_max, node.val)
            else:
                return False, 0, 0, 0  # size is 0 if not a BST

        dfs(root)
        return largest_bst

