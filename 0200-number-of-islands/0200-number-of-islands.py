class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        visited = set()
        islands = 0

        def bfs(row, col):
            queue = deque([(row, col)])
            while queue:
                r, c = queue.popleft()
                if (r, c) not in visited:
                    visited.add((r, c))
                    # Check all four directions
                    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited and grid[nr][nc] == "1":
                            queue.append((nr, nc))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1
        
        return islands
    
    