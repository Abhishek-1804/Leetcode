class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        fresh_oranges = 0
        q = deque([])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh_oranges += 1
                elif grid[row][col] == 2:
                    q.append((row, col))

        ans = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q and fresh_oranges > 0:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        fresh_oranges -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            
            ans += 1
        
        return ans if fresh_oranges == 0 else -1