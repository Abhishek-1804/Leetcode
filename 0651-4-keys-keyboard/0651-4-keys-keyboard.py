class Solution:
    def maxA(self, n: int) -> int:

        dp = [a for a in range(1, n+1)]

        for i in range(4, n):
            for j in range(2, i-2):
                dp[i] = max(dp[i], dp[j] * (i-j-1))

        return dp[-1]
