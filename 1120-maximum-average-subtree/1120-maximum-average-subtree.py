# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        
        max_avg = 0

        def dfs(node):

            nonlocal max_avg
            
            if not node:
                return 0, 0 # curr sum, number of nodes
            
            left_sum, left_nodes = dfs(node.left)
            right_sum, right_nodes = dfs(node.right)

            max_avg = max(max_avg, (node.val + left_sum + right_sum) / (1 + left_nodes + right_nodes))

            return left_sum + right_sum + node.val, 1 + left_nodes + right_nodes
        
        dfs(root)

        return max_avg