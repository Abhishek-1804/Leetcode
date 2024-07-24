class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        dp = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row == 0 and col == 0:
                    dp[row][col] = grid[row][col]
                
                elif row == 0:
                    dp[row][col] = grid[row][col] + dp[row][col-1]
                
                elif col == 0:
                    dp[row][col] = grid[row][col] + dp[row-1][col]
                
                else:
                    dp[row][col] = grid[row][col] + min(dp[row-1][col], dp[row][col-1])
        
        print(dp)
        return dp[-1][-1]