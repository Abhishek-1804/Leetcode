"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        hmap = {}

        def helper(node):
            if not node:
                return
            
            if node in hmap:
                return hmap[node]
            
            hmap[node] = Node(node.val)
            
            for neighbor in node.neighbors:
                hmap[node].neighbors.append(helper(neighbor))
            
            return hmap[node]
        
        return helper(node)
