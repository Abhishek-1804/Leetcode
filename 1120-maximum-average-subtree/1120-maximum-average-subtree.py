# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        
        self.max_avg = float('-inf')  # Global variable

        def dfs(node):

            if not node:
                return 0, 0 # curr sum, number of nodes
            
            left_sum, left_nodes = dfs(node.left)
            right_sum, right_nodes = dfs(node.right)

            self.max_avg = max(self.max_avg, (node.val + left_sum + right_sum) / (1 + left_nodes + right_nodes))

            return left_sum + right_sum + node.val, 1 + left_nodes + right_nodes
        
        dfs(root)

        return self.max_avg