class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s3) != len(s1) + len(s2):
            return False
        
        dp = [[False] * (len(s1) + 1)] * (len(s2) + 1)

        for row in range(len(dp)):
            for col in range(len(dp[0])):
                if row == 0 and col == 0:
                    dp[row][col] = True
                
                elif row == 0:
                    dp[row][col] = dp[row][col-1] and s1[col-1] == s3[row + col - 1]

                elif col == 0:
                    dp[row][col] = dp[row-1][col] and s2[row-1] == s3[row + col - 1]
                
                else:
                    dp[row][col] = (dp[row][col-1] and s1[col-1] == s3[row + col - 1]) or (dp[row-1][col] and s2[row-1] == s3[row + col - 1])
        
        return dp[-1][-1]