class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        if not matrix or not matrix[0]:
            return 0
        
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        max_sq = 0

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row == 0 or col == 0:
                    dp[row][col] = int(matrix[row][col])
                
                else:
                    if matrix[row][col] == '1':
                        dp[row][col] = min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1]) + 1
                    
                    # else:
                    #     dp[row][col] = 0
                max_sq = max(max_sq, dp[row][col])
        
        return max_sq*max_sq