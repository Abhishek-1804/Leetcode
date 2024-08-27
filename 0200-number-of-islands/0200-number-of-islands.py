class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        seen = set()
        counter = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) in seen or grid[row][col] == '0':
                    continue
                else:
                    q = collections.deque([(row, col)])
                    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                    while q:
                        r, c = q.popleft()
                        for nr, nc in directions:
                            new_row = r + nr
                            new_col = c + nc
                            if (new_row, new_col) in seen:
                                continue
                            if new_row >= 0 and new_row < len(grid) and new_col >= 0 and new_col < len(grid[0]) and grid[new_row][new_col] == '1':
                                q.append((new_row, new_col))
                                seen.add((new_row, new_col))
                    counter += 1
        
        return counter