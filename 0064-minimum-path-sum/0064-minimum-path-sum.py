class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        # Initialize first row
        for col in range(1, cols):
            grid[0][col] += grid[0][col-1]
        
        # Initialize first column
        for row in range(1, rows):
            grid[row][0] += grid[row-1][0]
        
        # Fill remaining cells
        for row in range(1, rows):
            for col in range(1, cols):
                grid[row][col] += min(grid[row-1][col], grid[row][col-1])
        
        return grid[-1][-1]
