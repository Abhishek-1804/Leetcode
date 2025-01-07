class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        q = deque([])
        fresh_oranges = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        minutes = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        while q and fresh_oranges > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # If adjacent orange is fresh, rot it and add to the queue
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh_oranges -= 1
            
            minutes += 1
        
        return minutes if fresh_oranges == 0 else -1