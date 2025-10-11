class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = [[0 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]
        
        for row in range(len(dp)):
            for col in range(len(dp[0])):

                if row == 0:
                    dp[row][col] = col
                
                elif col == 0:
                    dp[row][col] = row
                
                elif word1[col-1] == word2[row-1]:
                    dp[row][col] = dp[row-1][col-1]
                    
                else:
                    dp[row][col] = min(dp[row-1][col] + 1, dp[row][col-1] + 1, dp[row-1][col-1] + 1)
        
        return dp[-1][-1]