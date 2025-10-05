class Solution:
    def maxA(self, n: int) -> int:
        
        # n = 1   1   A
        # n = 2   2   AA
        # n = 3   3   AAA
        # n = 4   4   AAAA
        # n = 5   5   AAAAA
        # n = 6   6   AAA ca cc cv
        # n = 7   9   AAA ca cc cv cv
        # n = 8   12  AAA ca cc cv cv cv
        # n = 9   15  AAA ca cc cv cv cv cv
        # n = 10  18  AAA ca cc cv ca cv cv cv

        dp = [0 for _ in range(n+1)]

        for i in range(1, n+1):
            dp[i] = dp[i-1] + 1
            for j in range(1, i-2):
                dp[i] = max(dp[i], dp[j] * (i-j-1))
        
        return dp[-1]
