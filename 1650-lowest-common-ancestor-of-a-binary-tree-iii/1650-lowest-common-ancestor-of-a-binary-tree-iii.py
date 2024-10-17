"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        p_path = []
        while p:
            p_path.append(p)
            p = p.parent
        
        while q:
            if q in p_path:
                return q
            q = q.parent