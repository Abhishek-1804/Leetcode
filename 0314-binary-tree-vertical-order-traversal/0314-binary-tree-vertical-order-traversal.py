# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = {}

        if not root:
            return

        q = [(root, 0)]

        while q:
            node, ind = q.pop(0)
            if ind not in d:
                d[ind] = []
            d[ind].append(node.val)

            if node.left:
                q.append((node.left, ind-1))
            if node.right:
                q.append((node.right, ind+1))

        
        ans = []

        for i in sorted(d.keys()):
            ans.append(d[i])
        
        return ans


        