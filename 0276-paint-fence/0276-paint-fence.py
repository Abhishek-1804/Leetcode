class Solution:
    def numWays(self, n: int, k: int) -> int:
        
        if n == 0:
            return 0
        if n == 1:
            return k
        if n == 2:
            return k * k
        
        dp = [0 for _ in range(n)]
        dp[0] = k
        dp[1] = k * k
        
        for i in range(2, n):
            dp[i] = (dp[i-1] + dp[i-2]) * (k - 1)
        
        return dp[n-1]