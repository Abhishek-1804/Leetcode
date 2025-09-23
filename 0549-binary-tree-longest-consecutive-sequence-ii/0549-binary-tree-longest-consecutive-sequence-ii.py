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
                return (0, 0)  # (inc, dec)

            left_inc, left_dec = dfs(node.left)
            right_inc, right_dec = dfs(node.right)
            inc = dec = 1

            if node.left:
                if node.left.val == node.val + 1:
                    inc = max(inc, left_inc + 1)
                elif node.left.val == node.val - 1:
                    dec = max(dec, left_dec + 1)
            if node.right:
                if node.right.val == node.val + 1:
                    inc = max(inc, right_inc + 1)
                elif node.right.val == node.val - 1:
                    dec = max(dec, right_dec + 1)

            # The path can combine an incrementing and a decrementing path at node
            max_len = max(max_len, inc + dec - 1)
            return (inc, dec)

        dfs(root)
        return max_len