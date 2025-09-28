class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        from collections import deque
        
        seen = set()
        rows = len(grid)
        cols = len(grid[0])
        unique_shapes = set()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for row in range(rows):
            for col in range(cols):
                if (row, col) in seen:
                    continue
                if grid[row][col] == 1:
                    q = deque([])
                    q.append((row, col))
                    start_row, start_col = row, col
                    shape = []  # collect relative coordinates of all island cells
                    while q:
                        r, c = q.popleft()
                        if (r, c) in seen:
                            continue
                        seen.add((r, c))
                        shape.append((r - start_row, c - start_col))
                        for dr, dc in directions:
                            nr, nc = r+dr, c+dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in seen:
                                q.append((nr, nc))
                    unique_shapes.add(tuple(shape))  # add the island shape after BFS
        
        return len(unique_shapes)