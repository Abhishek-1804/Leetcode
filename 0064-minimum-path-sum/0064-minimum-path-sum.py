class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        dp = [[float('inf') for _ in range(cols)] for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if row == 0 and col == 0:
                    dp[row][col] = grid[row][col]
                elif row == 0:
                    dp[row][col] = grid[row][col] + dp[row][col-1]
                elif col == 0:
                    dp[row][col] = grid[row][col] + dp[row-1][col]
                else:
                    dp[row][col] = grid[row][col] + min(dp[row-1][col], dp[row][col-1])

        return dp[row][col]
