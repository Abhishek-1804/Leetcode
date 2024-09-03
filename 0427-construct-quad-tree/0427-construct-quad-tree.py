"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        n = len(grid)
        head = Node(grid[0][0], 1)

        for row in range(n):
            for col in range(n):
                if grid[row][col] != grid[0][0]:
                    head.isLeaf = 0
                    break
        if head.isLeaf:
            return head

        mid = n // 2
        topLeftGrid = [row[:mid] for row in grid[:mid]]
        topRightGrid = [row[mid:] for row in grid[:mid]]
        bottomLeftGrid = [row[:mid] for row in grid[mid:]]
        bottomRightGrid = [row[mid:] for row in grid[mid:]]

        head.topLeft = self.construct(topLeftGrid)
        head.topRight = self.construct(topRightGrid)
        head.bottomLeft = self.construct(bottomLeftGrid)
        head.bottomRight = self.construct(bottomRightGrid)

        return head