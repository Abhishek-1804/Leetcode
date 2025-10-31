class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        
        rows, cols = len(grid), len(grid[0])

        total = 0
        q = deque([])
        directions = ((0,1), (1, 0), (-1, 0), (0, -1))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    q.append((row, col))
                    grid[row][col] = '#'
                    while q:
                        r, c = q.popleft()
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                                grid[nr][nc] = '#'
                                q.append((nr, nc))
                    
                    total += 1
        
        return total