# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        output = []

        if not root:
            return output
        
        q = collections.deque([])
        q.append(root)
        flag = False

        while q:
            n = len(q)
            temp_arr = []
            for _ in range(n):
                node = q.popleft()
                temp_arr.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if not flag:
                output.append(temp_arr)
                flag = True
            else:
                output.append(temp_arr[::-1])
                flag = False
        
        return output
