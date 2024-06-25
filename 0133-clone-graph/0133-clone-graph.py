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

        if not node:
            return
        
        clone_map = {}
        queue = [node]
        clone_map[node] = Node(node.val)

        while queue:
            n = queue.pop(0)

            for neighbor in n.neighbors:
                if neighbor not in clone_map:
                    clone_map[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                
                clone_map[n].neighbors.append(clone_map[neighbor])

        return clone_map[node]