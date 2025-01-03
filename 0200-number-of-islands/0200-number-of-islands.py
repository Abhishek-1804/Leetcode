class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        seen = set()
        q = collections.deque([])
        count = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row, col) not in seen:
                    q.append((row, col))
                    while q:
                        r, c = q.popleft()
                        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
                        for dr, dc in directions:
                            nr, nc = r+dr, c+dc
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == '1' and (nr, nc) not in seen:
                                q.append((nr, nc))
                                seen.add((nr, nc))

                    count += 1
        
        return count