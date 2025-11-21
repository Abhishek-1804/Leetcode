class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        dp = [0, 0, 0]

        for num in nums:
            prev = dp[:]
            # For ending with 1s: remove if not 1
            dp[0] = prev[0] + (num != 1)
            # For ending with <=2s: remove if not 2
            dp[1] = min(prev[0], prev[1]) + (num != 2)
            # For ending with <=3s: remove if not 3
            dp[2] = min(prev[0], prev[1], prev[2]) + (num != 3)

        return min(dp)