class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = 0

        q = deque([])
        rows, cols = len(grid), len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    q.append((row, col))
                    grid[row][col] = '0'
                    while q:
                        r, c = q.popleft()
                        for dr, dc in directions:
                            nr, nc = dr + r, dc + c
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                                q.append((nr, nc))
                                grid[nr][nc] = '0'
                    
                    islands += 1
        
        return islands

