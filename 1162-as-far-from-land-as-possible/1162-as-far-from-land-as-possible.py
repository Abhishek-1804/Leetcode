from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        q = deque()

        # Enqueue all land cells
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    q.append((r, c))

        if len(q) == 0 or len(q) == rows * cols:
            return -1

        distance = -1
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while q:
            # for level order traversal
            # calc distance at end of each level
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                        grid[nr][nc] = 2  # Mark as visited water
                        q.append((nr, nc))
            distance += 1
            
        return distance
