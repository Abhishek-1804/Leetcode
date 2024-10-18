class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        q = collections.deque([(0, 0, 1)])
        seen = {(0, 0)}
        min_dist = float('inf')

        while q:
            row, col, dist = q.popleft()
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                min_dist = min(min_dist, dist)
                continue
            
            dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
            for r, c in dirs:
                nr = r + row
                nc = c + col
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in seen and grid[nr][nc] == 0:
                    seen.add((nr, nc))
                    q.append((nr, nc, dist+1))
        
        return min_dist if min_dist != float('inf') else -1

