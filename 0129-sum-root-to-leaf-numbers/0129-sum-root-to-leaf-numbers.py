# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        sum_ = 0

        def dfs(node, curr_num):
            nonlocal sum_

            if not node:
                return

            curr_num += str(node.val)

            if not node.left and not node.right:
                sum_ += int(curr_num)
                curr_num = curr_num[:-1]
                return

            dfs(node.left, curr_num)
            dfs(node.right, curr_num)

        dfs(root, '')
        return sum_