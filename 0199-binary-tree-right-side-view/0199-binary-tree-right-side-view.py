# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        return self.rightSideView_dfs(root)
        # return self.rightSideView_bfs(root)
        
    def rightSideView_dfs(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        
        def dfs(node, depth):
            if not node:
                return
            
            # First time visiting this depth level
            if depth == len(output):
                output.append(node.val)
            
            # Visit right first, then left
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root, 0)
        return output


    def rightSideView_bfs(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        
        output = []
        q = deque([])

        if not root:
            return output
        
        q.append(root)

        while q:
            prev = None
            for _ in range(len(q)):
                node = q.popleft()
                prev = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            output.append(prev)
        
        return output