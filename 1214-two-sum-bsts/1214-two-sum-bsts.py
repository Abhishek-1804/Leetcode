# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:

        def dfs(node, node_set):
            if not node:
                return False
            dfs(node.left, node_set)
            node_set.add(node.val)
            dfs(node.right, node_set)

        node_set1 = set()
        node_set2 = set()

        dfs(root1, node_set1)
        dfs(root2, node_set2)

        for val1 in node_set1:
            if target - val1 in node_set2:
                return True
        return False