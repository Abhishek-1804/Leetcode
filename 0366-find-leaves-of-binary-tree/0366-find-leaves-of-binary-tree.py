# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        output = []

        def dfs(node):
            
            if not node:
                return -1
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            curr_height = 1 + max(left_height, right_height)

            if len(output) == curr_height:
                output.append([])
            
            output[curr_height].append(node.val)
            return curr_height
        
        dfs(root)

        return output