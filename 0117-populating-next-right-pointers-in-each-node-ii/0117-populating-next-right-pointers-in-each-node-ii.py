"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return
        
        q = collections.deque([root])
        
        while q:
            n = len(q)
            temp = None
            for i in range(n):
                node = q.pop()
                node.next = temp
                temp = node
                if node.right:
                    q.appendleft(node.right)
                if node.left:
                    q.appendleft(node.left)

        return root