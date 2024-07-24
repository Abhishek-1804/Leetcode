class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        dp = [[1 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        print(dp)

        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[0])):

                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                
                else:
                    if row == 0:
                        dp[row][col] = dp[row][col-1]
                    
                    elif col == 0:
                        dp[row][col] = dp[row-1][col]
                    
                    else:
                        dp[row][col] = dp[row-1][col] + dp[row][col-1]
        
        return dp[-1][-1]